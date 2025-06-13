from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")  # ✅ Return formatted date

def calculate_future_date(days_to_add):
    future_date = datetime.now() + timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")  # ✅ Return formatted future date

def main():
    # Part 1: Display current date and time
    current = display_current_datetime()
    print("Current date and time:", current)

    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add: "))
        future = calculate_future_date(days)
        print("Future date:", future)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

