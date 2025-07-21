from art import logo  # art.py must be in the same folder


# Operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2


# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# Calculator main function
def calculator():
    print(logo)
    continue_calculating = True
    num1 = float(input("What is the first number?: "))

    while continue_calculating:
        # Display all operators
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        # Retrieve function and call it
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"\nType 'y' to continue calculating with {result}, or 'n' to start a new calculation, or 'q' to quit: ").lower()

        if choice == "y":
            num1 = result
        elif choice == "n":
            print("\n" * 3)
            calculator()
            break
        else:
            print("Goodbye! 👋")
            continue_calculating = False


calculator()
