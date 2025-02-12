def even_num(n):
    for i in range(0, n):
        if i%2==0:
            yield i
n = int(input())
a = even_num(n)
b = [str(k) for k in a]
print(", ".join(b))
