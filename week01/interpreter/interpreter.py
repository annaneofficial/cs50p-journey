# Step 1: Ask the user for a math problem
expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

# Step 2: Split the input into three parts
x, y, z = expression.split(" ")

# Step 3: Convert x and z from strings to numbers
x = int(x)
z = int(z)

# Step 4: Do the math based on the operation (y)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    print("Invalid operation!")
    exit()

# Step 5: Print the result as a floating-point number with one decimal place
print(f"Result: {float(result):.1f}")
