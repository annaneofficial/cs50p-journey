def main():
    # Prompt the user for a time
    time_str = input("Enter a time in 24-hour format (e.g., 7:30 or 13:45): ")
    
    # Convert the time string to a float representing hours
    time_float = convert(time_str)
    
    # Determine which meal time it is
    if 7.0 <= time_float <= 8.0:
        print("breakfast time")  # Match exact expected output
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")  # Match exact expected output
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")  # Match exact expected output
    # If it's not meal time, do nothing

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")
    
    # Convert hours and minutes to float and calculate total hours
    total_hours = float(hours) + float(minutes) / 60.0
    
    return total_hours

if __name__ == "__main__":
    main()