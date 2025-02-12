import math
def area(a,b):
    return int((a * b**2) / (4 * math.tan(math.pi / a)))
a = int(input("Input number of sides: "))
b = int(input("Input the length of a side: "))
s = area(a,b)
print(f"The area of the polygon is: {s}")