import re
with open(r"C:\Users\Gulistan\Downloads\row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)
p = re.sub(r'[,.]', ':', s)
print(p)