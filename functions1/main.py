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
    for i in range(1, 50):
        if (factorial(i - 1) + 1) % i == 0:
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
    if 0 <= n <= 25:
        return chr(n + 97)


# Part G

def alphabet() -> list:
    alpha = []
    for i in range(26):
        alpha.append(give_char(i))
    return alpha


# Part H

def equalfunky(m):
    for n in range(m):
        if funky(n) == m:
            return n
        elif funky(n) > m:
            return -1

# Part I
def most_frequent(string: str):
    old_count = 0
    frequent_letter = ''
    for x in alphabet():
        current_count = count_letter(string, x)
        if current_count > old_count:
            frequent_letter = x
            old_count = current_count

    return alphabet()[int(frequent_letter)]

most_frequent("AABBCCC")