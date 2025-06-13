from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date  # ✅ Return instead of just print

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        return formatted_future  # ✅ Return formatted date
    except ValueError:
        return "Invalid input. Please enter a valid integer."

def main():
    current = display_current_datetime()
    print("Current date and time:", current)

    future = calculate_future_date()
    print("Future date:", future)

if __name__ == "__main__":
    main()

