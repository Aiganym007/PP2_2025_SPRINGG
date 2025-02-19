import re
with open(r"C:\Users\Gulistan\Downloads\row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)
p = re.compile('[a-z]+_[a-z]+')
m = p.findall(s)
if m:
    print(m)
else:
    print("error")