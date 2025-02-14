# Take input from the user
password = input("Enter your password: ")

# Initialize flags to check conditions
has_upper = False
has_lower = False
has_digit = False
is_long = len(password) >= 8

# Check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

# Check if all conditions are met
if is_long and has_upper and has_lower and has_digit:
    print("Strong password!")
else:
    print("Weak password. Please ensure your password:")
    if not is_long:
        print("- Is at least 8 characters long.")
    if not has_upper:
        print("- Contains at least one uppercase letter.")
    if not has_lower:
        print("- Contains at least one lowercase letter.")
    if not has_digit:
        print("- Contains at least one digit.")
