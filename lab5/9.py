import re
with open(r"C:\Users\Gulistan\Downloads\row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)
def spaces(word):
    return ' '+ word.group(0)
p = re.sub(r'[A-Z]', spaces, s)
print(p)