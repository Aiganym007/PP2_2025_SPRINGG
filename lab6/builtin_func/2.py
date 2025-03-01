import math
a = input()
b = 0
c = 0
for char in a:
    if char.isupper():
        b += 1
for char in a:
    if char.islower():
        c += 1
print("upper: ", b)
print("lower: ", c)
