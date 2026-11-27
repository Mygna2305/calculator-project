# Simple calculator - UCS 745 Git lab


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: divide by zero"
    return a / b


def power(a, b):
    return a ** b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide, "^": power}


def calculate(a, op, b):
    if op not in OPERATIONS:
        return "Unknown operator"
    return OPERATIONS[op](a, b)


if __name__ == "__main__":
    a = float(input("First number: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Second number: "))
    print("Result:", calculate(a, op, b))
