import re
with open(r"C:\Users\Gulistan\Downloads\row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)
def toCamel(snake):
    return snake.group(1).upper()
p = re.sub(r'_([a-z])', toCamel, s)
print(p)