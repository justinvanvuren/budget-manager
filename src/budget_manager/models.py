"""The domain model: the Transaction class and its allowed values."""

FIELDS = ["id", "date", "kind", "category", "amount", "currency"]
KINDS = ["expense", "income"]
CATEGORIES = ["food", "transport", "housing", "leisure", "salary", "other"]


class Transaction:
    """One money movement. An invalid Transaction can never be created."""

    def __init__(self, id, date, kind, category, amount, currency="EUR"):
        # Validate BEFORE storing anything (Session 8: __init__ protects the object)
        if kind not in KINDS:
            raise ValueError("kind must be expense or income.")
        if category not in CATEGORIES:
            raise ValueError("unknown category '" + category + "'.")
        if amount <= 0:
            raise ValueError("amount must be > 0.")
        self.id = id
        self.date = date
        self.kind = kind
        self.category = category
        self.amount = amount
        self.currency = currency

    def signed_amount(self):
        """Income is positive, an expense is negative."""
        if self.kind == "income":
            return self.amount
        return -self.amount

    def to_dict(self):
        """Return the transaction as a dictionary (used to save it to the CSV)."""
        return {
            "id": self.id,
            "date": self.date,
            "kind": self.kind,
            "category": self.category,
            "amount": self.amount,
            "currency": self.currency,
        }