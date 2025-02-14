# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Perform the operation based on the operator
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    case _:  # Default case for invalid operators
        result = "Error: Invalid operator."

# Print the result
print(f"Result: {result}")