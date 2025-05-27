"""Create a Python program that acts as a basic
calculator. It should prompt the user to
enter two numbers and an operator (+
, -,
*
, /,
%), and then display the result of the
operation."""

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /, %): ").strip()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    else:
        return "Invalid operator. Please use +, -, *, /, or %."

    return f"The result of {num1} {operator} {num2} is: {result}"

print(calculator())