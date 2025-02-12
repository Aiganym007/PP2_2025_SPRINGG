def nums(N):
    while N>=0:
        yield N
        N-=1
N = 10
a = nums(N)
for k in a:
    print(k)