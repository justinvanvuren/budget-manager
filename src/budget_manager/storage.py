"""Load and save transactions in a CSV file."""
import csv
import os

from budget_manager.models import FIELDS
from budget_manager.validation import validate


def load(path):
    """Read the CSV. Return (valid transactions, error messages)."""
    transactions = []
    errors = []
    if not os.path.exists(path):
        return transactions, errors
    with open(path, encoding="utf-8", newline="") as f:
        row_number = 1
        for row in csv.DictReader(f):
            row_number += 1
            try:
                transactions.append(validate(row, "Row " + str(row_number)))
            except ValueError as error:
                errors.append(str(error))
    return transactions, errors


def save(path, transactions):
    """Write all transactions to the CSV (overwrites the file)."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for tx in transactions:
            writer.writerow(tx.to_dict())