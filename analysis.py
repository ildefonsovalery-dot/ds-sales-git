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
    total = 0.0                            # Empezamos con ingresos de cero

    for row in rows:                       # Recorremos cada venta
        if row["category"] == category:     # Comprobamos si coincide la categoría
            units = int(row["units"])       # Convertimos las unidades a número
            price = float(row["unit_price"]) # Convertimos el precio a número
            total += units * price          # Sumamos los ingresos de esa venta

    return total                           # Devolvemos los ingresos de la categoría

