cat > README.md << 'EOF'
# Interactive Personal Budget Manager — Release 1

Owner: Justin Van Vuren

## Setup
Install uv, then in the project folder run:
```bash
uv sync
```

## Run
From the project folder:
```bash
uv run budget-manager
```
The first run loads `data/sample_transactions.csv` (3 valid rows, 4 rejected rows with messages).
Changes are saved to `data/transactions.csv` straight away.

## Example
```
1) Add  2) List  3) Report  4) Undo  q) Quit: 3
Income:   2500.0
Expenses: 968.5
Balance:  1531.5
```

## Test
```bash
uv run python -m budget_manager.services
uv run python -m budget_manager.validation
```
3 tests: a normal report (services.py) and two boundary cases (validation.py):
amount 0 rejected, unknown category rejected.

## Files
- `models.py`: the Transaction class (checks its own values in `__init__`)
- `validation.py`: turns raw text into a Transaction, clear error messages
- `services.py`: add, undo, report
- `storage.py`: load/save CSV
- `cli.py`: menu

## Known limitations
- Only EUR; no currency conversion.
- The date check only looks at the format (YYYY-MM-DD), not whether the day exists.
- IDs are based on the number of transactions.
- Undo only removes the most recent transaction.
- Must be run from the project folder.
EOF