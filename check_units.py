from copy import deepcopy
from analysis import load_sales, total_units

rows = load_sales()
before = deepcopy(rows)
assert total_units(rows) == 36
assert total_units([]) == 0
assert total_units([{"units": "0"}]) == 0
assert rows == before
print("Total-units checks passed")
