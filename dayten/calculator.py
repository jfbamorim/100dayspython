from dayten.calculator_art import logo


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


def calculator():
    repeat = 'y'
    num1 = int(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    while repeat == 'y':
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the next number? "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        repeat = input(f"Type y to continue calculating with {answer}, or n to start a new calculation: ").lower()
        if repeat == 'y':
            num1 = answer
        else:
            calculator()

# Body
print(logo)
calculator()

#operation_symbol = input("Pick another operation: ")
#num3 = int(input("What's the next number? "))
#calc_function = operations[operation_symbol]
#second_answer = calc_function(calc_function(num1, num2), num3)
#print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
