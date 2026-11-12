# Sales Git Practice

A beginner Git and GitHub project using eight synthetic sales order lines.

## Run the baseline

Use Python 3, open a terminal in this project, then run:

```text
python app.py
python checks.py
```

Use python3 instead if that is your Python 3 launcher. No external packages.
Expected: 8 order lines, revenue $251.47, and Baseline checks passed.

## Data dictionary

- order_id: text identifier for an order line
- product: product name
- category: exact, case-sensitive category label
- units: whole-number quantity, read from CSV as text
- unit_price: price per unit, read from CSV as text

The CSV is a small synthetic fixture, not real customer information.
Do not edit the fixture to make a failing check pass.

## Day 14 feature tasks

Implement total_units and revenue_for_category in analysis.py.
Their supplied checks intentionally fail before implementation:

```text
python check_units.py
python check_category.py
```

Run only the checks for the completed task until both features are merged.
The baseline checks must continue to pass throughout.

## Analysis limits

One row is one order line. This small fixture cannot establish market trends.
Floating-point arithmetic is used for teaching; display money to two decimals.

## Team workflow

Use a feature branch, inspect the diff, test, commit, push, open a pull request,
and have a classmate review before merging. Keep generated output in output/.

## Reproducibility notes

The dataset contains eight synthetic order lines.
Each row represents one order line.
All commands are executed using Python 3.

