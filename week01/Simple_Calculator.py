import sys

def display_header():
    """Display the program header."""
    print("=" * 30)
    print(" " * 5, "Simple Calculator V1")
    print("=" * 30)

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error! Please enter a valid number.")

def get_operator():
    """Get a valid operator from the user."""
    valid_operators = {'+', '-', '*', '/'}
    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator in valid_operators:
            return operator
        print("Error! Please enter a valid operator.")

def calculate(first_number, second_number, operator):
    """Perform the calculation based on the operator."""
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        if second_number == 0:
            raise ValueError("Division by zero is not allowed.")
        return first_number / second_number

def main():
    """Main function to run the calculator."""
    display_header()

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")
    operator = get_operator()

    try:
        result = calculate(first_number, second_number, operator)
        print(f"{first_number} {operator} {second_number} = {result}")
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()