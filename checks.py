from math import isclose
from analysis import load_sales, total_revenue

rows = load_sales()
assert len(rows) == 8
assert rows[0]["order_id"] == "101"
assert isclose(total_revenue(rows), 251.47, abs_tol=0.001)
assert total_revenue([]) == 0
print("Baseline checks passed")
