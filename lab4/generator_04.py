def squares(a, b):
    for i in range(a, b+1): 
        yield i ** 2
a = 2
b = 8
s = squares(a,b)
for k in s:
    print(k)