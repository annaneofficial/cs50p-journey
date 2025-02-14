# Take input from the user
score = float(input("Enter your score: "))

# Check the grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"Your grade is: {grade}")