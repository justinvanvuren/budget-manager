cat > DESIGN.md << 'EOF'
# Design rationale

I split the program into small modules with one job each. All checks on raw input live in
`validation.py`, so typed input and the CSV file follow exactly the same rules and give the same
clear messages (e.g. "Row 5: amount must be > 0."). The Transaction class checks kind, category
and amount in `__init__`, so an invalid transaction can never exist anywhere in the program.
`services.py` does the budget maths without any `input()`, `print()` or file access, which is why
it can be tested directly. Unknown categories are rejected instead of being silently changed to
"other", so mistakes stay visible. The file is saved after every add and undo, so the CSV on disk
always matches what the program shows, even after a restart.
EOF