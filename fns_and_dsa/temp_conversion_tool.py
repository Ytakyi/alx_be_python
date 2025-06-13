
# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion function: Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Explicitly referencing the global variable
    factor = FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * factor

# Conversion function: Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Explicitly referencing the global variable
    factor = CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * factor) + 32

# Main user interaction
def main():
    temp_str = input("Enter the temperature: ")
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Validate numeric temperature
    try:
        temp_value = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Handle unit conversion
    if unit == "C":
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted:.2f}°F")
    elif unit == "F":
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()


