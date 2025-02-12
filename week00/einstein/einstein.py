
def main():
    # Prompt the user for mass in kilograms
    mass = int(input("Enter mass in kilograms: "))

    # Speed of light in meters per second
    speed_of_light = 300000000  # meters per second

    # Calculate energy using E = mc^2
    energy = mass * (speed_of_light ** 2)

    # Output the equivalent energy in Joules
    print(f"Equivalent energy in Joules: {energy}")


main()
