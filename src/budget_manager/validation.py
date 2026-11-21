"""Turn raw text (typed or from the CSV) into a Transaction, with clear error messages."""
from budget_manager.models import Transaction


def validate(raw, where="Input"):
    """Clean the raw text and return a Transaction, or raise ValueError."""
    tx_id = raw["id"].strip()
    if tx_id == "":
        raise ValueError(where + ": id is required.")

    date = raw["date"].strip()
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        raise ValueError(where + ": date must look like 2026-09-04.")

    try:
        amount = round(float(raw["amount"]), 2)
    except ValueError:
        raise ValueError(where + ": amount must be a number.")

    currency = raw.get("currency", "EUR").strip().upper() or "EUR"

    try:
        return Transaction(tx_id, date, raw["kind"].strip().lower(),
                           raw["category"].strip().lower(), amount, currency)
    except ValueError as error:
        raise ValueError(where + ": " + str(error))   # add the row number to the message


# ---- Tests (boundary cases). Run with: uv run python -m budget_manager.validation ----
if __name__ == "__main__":
    # Boundary 1: an amount of 0 must be rejected with a clear message
    raw = {"id": "T009", "date": "2026-09-04", "kind": "expense", "category": "food", "amount": "0"}
    try:
        validate(raw, "Row 4")
        assert False, "zero should be rejected"
    except ValueError as error:
        assert str(error) == "Row 4: amount must be > 0."
    print("PASS boundary: amount 0 is rejected")

    # Boundary 2: an unknown category must be rejected, not silently accepted
    raw = {"id": "T010", "date": "2026-09-04", "kind": "expense", "category": "crypto", "amount": "5"}
    try:
        validate(raw, "Row 5")
        assert False, "unknown category should be rejected"
    except ValueError as error:
        assert str(error) == "Row 5: unknown category 'crypto'."
    print("PASS boundary: unknown category is rejected")