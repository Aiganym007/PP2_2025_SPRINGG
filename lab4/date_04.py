from datetime import datetime
d1 = datetime(year=2025, month=2, day=12, hour=11, minute=40, second=9)
d2 = datetime(year=2025, month=2, day=12, hour=12, minute=40, second=1)
a = d2 - d1
b = a.total_seconds()
print(b)