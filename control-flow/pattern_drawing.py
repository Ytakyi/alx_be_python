# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Ensure the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0  # Initialize row counter

    # Outer while loop for rows
    while row < size:
        # Inner for loop for columns
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after each row
        row += 1  # Increment the row counter
