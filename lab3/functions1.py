#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = 1000
ounces = grams_to_ounces(grams)
print(ounces)

#2
def F_to_C(F):
    C = (5 / 9) * (F - 32)
    return C
F = 150
C = F_to_C(F)
print(f"{C:.2f}")

#3
def solve(numheads, numlegs):
    #ch + rab = numheads
    #2ch + 4rab = numlegs
    rabbit = numlegs // 2 - numheads
    chicken = numheads - rabbit
    if chicken >= 0 and rabbit >= 0:
        return(chicken, rabbit)
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)

#4
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(number):
    return [num for num in number if is_prime(num)]  
number = [11, 13, 2, 5, 24, 7, 6]
primes = filter_prime(number)
print(primes)

#5


#6
def str_revv():
    str = "We are ready"
    word = str.split()
    rev_str = ' '.join(reversed(word))
    return rev_str
print(str_revv())

#7
def arr(num):
    for i in range(len(num)-1):
        if num[i] == 3 and num[i+1] == 3:
            return True
    return False
print(arr([1,3,3]))
print(arr([1,3,1,3]))
print(arr([3,1,3]))

#8


#9
import math
def volume_sph(R):
    V = (4/3)*math.pi*R**3
    return V 
R = 5
V = volume_sph(R)
print(V)

#10

#13
import random
def guess_the_num():
    a = random.randint(1,20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    k = 0
    while True:
        print("Take a guess.")
        g = int(input())
        k += 1
        if g < a:
            print("Your guess is too low.")
        elif g > a:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {a} guesses!")
            break
print(guess_the_num())