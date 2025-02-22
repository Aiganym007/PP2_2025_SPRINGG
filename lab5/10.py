import re
with open(r"C:\Users\Gulistan\Downloads\row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)
def snake(camel):
    return '_' + camel.group(0).lower()
p = re.sub(r'[A-z][a-z]', snake, s)
print(p)