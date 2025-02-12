def div_num(n):
    for i in range(0, n):
        if i%3==0 and i%4==0:
            yield i
n = 50
a = div_num(n)
for k in a:
    print(k)
