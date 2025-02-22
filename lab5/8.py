import re
with open(r"C:\Users\Gulistan\Downloads\row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)
def spl(word):
    word = re.findall(r'[A-Z][a-z]*', s)
    return word
p = ' '.join(spl(s))
print(p)