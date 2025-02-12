def generator_num(N):
    for i in range(1, N+1):
        yield i*i
N = 5
a = generator_num(N)
for k in a:
    print(k)

