# Part 1: Remove commas (and spaces) from a string

def remove_commas(string: str) -> str:
    string = string.replace(',', '')
    return string


def remove_spaces(string: str) -> str:
    string = string.replace(' ', '')
    return string


# Part 2: Negative signs

def check_valid_negative_sign(string: str) -> bool:
    negative = string.find('-')
    if string.count('-') > 1:
        # If more than 1 negative is in string, return false
        return False
    else:
        # If 1 or fewer negatives are in string, return if negative is not found or at first character
        return negative == -1 or negative == 0


# Part 3: Check if at most 1 decimal point

def check_valid_decimal_point(string: str) -> bool:
    decimals = 0

    for x in string:
        if x == '.':
            decimals += 1

    return decimals == 0 or decimals == 1


# Part 4: Check if string is only decimals, negative signs, or digits

def check_only_digits_others(string: str) -> bool:
    if len(string) == 0:
        # If string is empty, return false.
        return False
    else:
        # If string is not empty, assume string is valid until character is not a digit, '.', or '-'
        for x in string:
            valid = x.isdigit() or x == '.' or x == '-'
            if valid == False:
                return False

        return True


# Part 5: Check if string has digit

def check_has_digit(string: str) -> bool:
    # Return true if any character in the string is a digit
    return any(chr.isdigit() for chr in string)


# Part 6: Check if string is a valid number

def is_number(string: str) -> bool:
    # Run all checks in previous parts, return True if all checks pass
    string = remove_commas(string)
    string = remove_spaces(string)

    if not (check_valid_negative_sign(string)):
        return False

    if not (check_valid_decimal_point(string)):
        return False

    if not (check_only_digits_others(string)):
        return False

    if not (check_has_digit(string)):
        return False

    return True


# Part 7: Ask user for valid number until valid number is given

def get_number(message_to_output: str) -> float:
    # Loop forever until a valid number is given
    while True:
        number = input("Input: ")
        if is_number(input):
            break

    return float(number)


# Part 8: Ask user for valid number between min and max until valid number is given

def get_number_bounded(message_to_output: str, min_value: float, max_value: float) -> float:
    while True:
        number = float(input("Input: "))
        if is_number(input) and min_value <= number <= max_value:
            break

    return float(number)


# Part 9: Checks if a given equation (comparing two numbers) is true

# Checks if there is exactly one '=' in a string
def check_valid_equal(string: str) -> bool:
    return string.count('=') == 1


def is_valid_equation(string: str) -> bool:
    string = remove_commas(string)
    string = remove_spaces(string)

    # Check if input contains exactly one '='
    if not string.count('=') == 1:
        return False

    exp = string.split('=')

    # If a side of the equation is not numerical, return False
    if not is_number(exp[0]) or not is_number(exp[1]):
        return False

    exp = [float(x) for x in exp]

    if exp[0] == exp[1]:
        return True
    else:
        return False
while True: print(is_valid_equation(input("Input:")))