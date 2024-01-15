from random import randint, choice
from numpy import prod

operations = ["+", "-", "*", "/"]

questions = {
    "arithmetic": 0,
    "algebra": 0,
    "geometry": 0
}

correct = {
    "arithmetic": 0,
    "algebra": 0,
    "geometry": 0
}

print("Round to the nearest tenth when required")

for i in range(10):
    questiontype = choice(["arithmetic", "algebra", "geometry"])

    if questiontype == "arithmetic":
        questions["arithmetic"] += 1

        a = randint(1, 100)
        b = randint(1, 100)
        operation = choice(operations)

        ans = input(str(a) + operation + str(b) + "=? ")

        ans = float(ans)
        ans = round(ans, 1)

        if operation == "+":
            res = a + b
        if operation == "-":
            res = a - b
        if operation == "*":
            res = a * b
        if operation == "/":
            res = round(a / b, 1)

        if ans == res:
            correct["arithmetic"] += 1

    elif questiontype == "algebra":
        questions["algebra"] += 1

        a = randint(1, 100)
        b = randint(1, 100)
        c = randint(1, 100)
        operation = choice(operations)

        ans = input(f"{a}x{operation}{b}={c}, x=? ")

        ans = float(ans)
        ans = round(ans, 1)

        if operation == "+":
            res = round((c - b) / a, 1)
        if operation == "-":
            res = round((c + b) / a, 1)
        if operation == "*":
            res = round(c / (a * b), 1)
        if operation == "/":
            res = round((c * b) / a, 1)

        if ans == res:
            correct["algebra"] += 1

    elif questiontype == "geometry":
        questions["geometry"] += 1

        sides = [randint(1, 10), randint(1, 10)]
        ans = round(float(input(
            f"A rectangle has an area of {prod(sides)}. One side length is {choice(sides)}. What is the perimeter of the rectangle? ")),
            1)

        ans = float(ans)
        ans = round(ans, 1)

        res = (2 * sides[0]) + (2 * sides[1])

        if ans == res:
            correct["geometry"] += 1

print(f"Score: {sum(correct.values())}/10")
print(f"Arithmetic: {correct['arithmetic']}/{questions['arithmetic']}")
print(f"Algebra: {correct['algebra']}/{questions['algebra']}")
print(f"Geometry: {correct['geometry']}/{questions['geometry']}")
