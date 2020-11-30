from calculator_art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    if n2 == 0:
        return "Divsion by zero"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
num1 = int(input("What's the first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number? "))

calc_function = operations[operation_symbol]
answer = calc_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
