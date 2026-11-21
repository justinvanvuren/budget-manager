"""The menu. This is the only module that uses input() and print()."""
import os

from budget_manager.services import add_transaction, next_id, summarize, undo_last
from budget_manager.storage import load, save
from budget_manager.validation import validate

DATA_FILE = "data/transactions.csv"
SAMPLE_FILE = "data/sample_transactions.csv"


def main():
    # First run: start from the sample file. Later runs: use the saved file.
    if os.path.exists(DATA_FILE):
        transactions, errors = load(DATA_FILE)
    else:
        transactions, errors = load(SAMPLE_FILE)
        save(DATA_FILE, transactions)
    print("Loaded", len(transactions), "transactions.")
    for message in errors:
        print("Skipped:", message)

    while True:
        choice = input("\n1) Add  2) List  3) Report  4) Undo  q) Quit: ").strip()

        if choice == "1":
            raw = {
                "id": next_id(transactions),
                "date": input("Date (YYYY-MM-DD): "),
                "kind": input("Kind (expense/income): "),
                "category": input("Category: "),
                "amount": input("Amount: "),
                "currency": "EUR",
            }
            try:
                tx = validate(raw)
            except ValueError as error:
                print("Not added:", error)
                continue
            add_transaction(transactions, tx)
            save(DATA_FILE, transactions)
            print("Added", tx.id)

        elif choice == "2":
            for tx in transactions:
                print(tx.id, tx.date, tx.kind, tx.category, tx.signed_amount(), tx.currency)

        elif choice == "3":
            report = summarize(transactions)
            print("Income:  ", report["income"])
            print("Expenses:", report["expenses"])
            print("Balance: ", report["balance"])

        elif choice == "4":
            removed = undo_last(transactions)
            if removed is None:
                print("Nothing to undo.")
            else:
                save(DATA_FILE, transactions)   # keep the file in sync
                print("Removed", removed.id)

        elif choice == "q":
            print("Goodbye.")
            break

        else:
            print("Please choose 1, 2, 3, 4 or q.")


if __name__ == "__main__":
    main()