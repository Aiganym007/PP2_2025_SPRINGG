from tasks import ounces, F_to_C, solve, filter_prime, print_permutations, sphera
grams = 1000
ounce = ounces(grams)
print(f"{grams} grams is {ounce} ")

F = 150
C = F_to_C(F)
print(f"{F}F is {C:.2f}C.")

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(f"Chickens: {result[0]}, Rabbits: {result[1]}")

numbers = [11, 13, 2, 5, 24, 7, 6]
primes = filter_prime(numbers)
print(primes)

b = 'abc'
print_permutations(b)

R = 5
V = sphera(R)
print(V)