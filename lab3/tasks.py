def ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

def F_to_C(F):
    C = (5 / 9) * (F - 32)
    return C

def solve(numheads, numlegs):
    rabbit = numlegs // 2 - numheads
    chicken = numheads - rabbit
    if chicken >= 0 and rabbit >= 0:
        return(chicken, rabbit)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(number):
    return [num for num in number if is_prime(num)]  

from itertools import permutations
def print_permutations(s):
    a = permutations(s)
    for k in a:
        print(''.join(k))

def str_revv():
    s = "We are ready"
    word = s.split()
    rev_str = ' '.join(reversed(word))
    return rev_str

def arr(num):
    for i in range(len(num)-1):
        if num[i] == 3 and num[i+1] == 3:
            return True
    return False

def spy_game(a):
    c = ""
    for i in range(len(a)):
        if a[i] == 0 or a[i] == 7:
            c += str(a[i])
    if c == '007':
        return True
    return False

import math
def sphera(R):
    V = (4/3) * math.pi * R**3
    return V 

def unique(a):
    c = []
    for b in a:
        if b not in c:
            c.append(b)
    return c

def palindrome(a):
    b = a[::-1]
    if a == b:
        return "palindrome"
    return "not palindrome"

def histogram(n):
    for i in n:
        print('*' * i)

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
            print(f"Good job, {name}! You guessed my number in {k} guesses!")
            break
