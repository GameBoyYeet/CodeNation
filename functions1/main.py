from math import factorial


# Part A

# Prompts for a positive integer forever until a positive integer is inputted

def partA():
    while True:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            break
    return num


# Part B

# This function takes a number, squares it, then returns the squared number.

def square(num: float):
    num *= num
    return num


# Part C

def count_letter(string, char):
    occurrences = 0
    for i in string:
        if i == char:
            occurrences += 1
    return occurrences


# Part D
def primes():
    primes = []
    for i in range(50):
        if factorial(i - 1) + 1 % i == 0:
            primes.append(i)
    return primes


# Part E

def funky(n):
    nums = []
    for i in range(1, n, 1):
        i = square(i)
        nums.append(i)
    return sum(nums)


# Part F

def give_char(n):
    if n >= 0 and n <= 25:
        return chr(n + 97)


# Part G

def alphabet():
    alpha = []
    for i in range(25):
        alpha.append(give_char(i))
    return alpha


# Part H

def equalfunky(m):
