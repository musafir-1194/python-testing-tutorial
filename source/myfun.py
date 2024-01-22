def add(number1, number2) -> any:
    return number1 + number2

def divide(number1, number2) -> any:
    return number1 / number2

def divide2(number1, number2) -> any:
    if number2 == 0:
        raise ValueError
    return number1 / number2