name = input("What's your name? ")

age = int(input("How old are you? "))

fav = int(input("What's your favorite number? "))

second = age - fav

print(f"{name}'s favorite number is {fav}\n")
print(f"Perhaps this is because they are {age} year(s) old, and {age}={fav}+{second}")