from copy import deepcopy
from math import isclose
from analysis import load_sales, revenue_for_category

rows = load_sales()
before = deepcopy(rows)
assert isclose(revenue_for_category(rows, "Stationery"), 89.50,
               abs_tol=0.001)
assert isclose(revenue_for_category(rows, "Bags"), 119.97,
               abs_tol=0.001)
assert revenue_for_category(rows, "Unknown") == 0
assert revenue_for_category([], "Stationery") == 0
assert rows == before
print("Category-revenue checks passed")
