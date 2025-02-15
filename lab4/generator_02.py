def even_num(n):
    for i in range(0, n):
        if i%2==0:
            yield i
a = int(input())
print(*even_num(a))
