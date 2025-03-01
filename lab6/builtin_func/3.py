import math
a = input()
def func(a):
    a = a.replace(" ", "").lower()
    return a == a[::-1]
if func(a):
    print("palindrom")
else:
    print("not palindrom")