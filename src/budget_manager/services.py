"""Budget logic. No input(), print() or files in this module."""


def next_id(transactions):
    """Return the next id, e.g. T005 when there are 4 transactions."""
    return f"T{len(transactions) + 1:03d}"


def add_transaction(transactions, tx):
    """Add a transaction to the list."""
    transactions.append(tx)


def undo_last(transactions):
    """Remove the last transaction and return it (None if the list is empty)."""
    if len(transactions) == 0:
        return None
    return transactions.pop()


def summarize(transactions):
    """Return total income, total expenses and the balance."""
    income = 0
    expenses = 0
    for tx in transactions:
        if tx.kind == "income":
            income += tx.amount
        else:
            expenses += tx.amount
    return {"income": round(income, 2), "expenses": round(expenses, 2),
            "balance": round(income - expenses, 2)}

# ---- Test (normal case). Run with: uv run python -m budget_manager.services ----
if __name__ == "__main__":
    from budget_manager.models import Transaction

    transactions = [
        Transaction("T001", "2026-09-01", "income", "salary", 2500),
        Transaction("T002", "2026-09-02", "expense", "food", 18.5),
    ]
    assert summarize(transactions) == {"income": 2500, "expenses": 18.5, "balance": 2481.5}
    print("PASS normal case: report totals are correct")
