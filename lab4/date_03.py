from datetime import datetime
a = datetime.now()
b = a.replace(microsecond=0)
print(b)