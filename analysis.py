import csv
from pathlib import Path


def load_sales():
    path = Path(__file__).resolve().parent / "data" / "sales.csv"
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def total_revenue(rows):
    total = 0.0
    for row in rows:
        total += int(row["units"]) * float(row["unit_price"])
    return total


def total_units(rows):
    total = 0

    for row in rows:
        units = int(row["units"])
        total += units

    return total


def revenue_for_category(rows, category):
    # Day 14: exact, case-sensitive category matching.
    raise NotImplementedError("Complete the category-revenue task")



