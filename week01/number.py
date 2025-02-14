# Take input from the user
number = int(input("Enter a number: "))

# Classify the number
if number > 0:
    print("Positive")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif number < 0:
    print("Negative")
else:
    print("Zero")