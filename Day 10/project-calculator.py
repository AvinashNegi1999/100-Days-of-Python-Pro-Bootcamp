# 🧮 Simple Calculator with Continue Option

def calculator(previous_result, operator_input, continue_choice):
    # Inner functions for operations
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Cannot divide by zero"

    # Get next number from user
    next_number = float(input("Enter the next number: "))

    # Perform selected operation
    if operator_input == "+":
        result = add(previous_result, next_number)
    elif operator_input == "-":
        result = subtract(previous_result, next_number)
    elif operator_input == "*":
        result = multiply(previous_result, next_number)
    elif operator_input == "/":
        result = divide(previous_result, next_number)
    else:
        print("Invalid operator.")
        return

    print("Result:", result)

    # Ask if user wants to continue
    continue_choice = input("Do you want to continue? (y/n): ").lower()
    if continue_choice == "y":
        new_operator = input("Choose an operator (+, -, *, /): ")
        calculator(result, new_operator, continue_choice)
    else:
        print("Calculator ended.")


# ▶️ Initial Inputs
first_number = float(input("Enter your first number: "))
operator = input("Choose an operator (+, -, *, /): ")
second_number = float(input("Enter your second number: "))

# Basic operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Cannot divide by zero"

# Compute first result
if operator == "+":
    result = add(first_number, second_number)
elif operator == "-":
    result = subtract(first_number, second_number)
elif operator == "*":
    result = multiply(first_number, second_number)
elif operator == "/":
    result = divide(first_number, second_number)
else:
    print("Invalid operator.")
    result = None

if result is not None:
    print("Result:", result)
    choice = input("Do you want to continue? (y/n): ").lower()
    if choice == "y":
        next_operator = input("Choose an operator (+, -, *, /): ")
        calculator(result, next_operator, choice)
    else:
        print("Calculator ended.")
