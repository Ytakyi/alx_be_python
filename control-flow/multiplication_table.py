# prompting user for input for multiplication table

number  = int(input("Enter a number to see its multiplication table: "))

# generate multiplication table 
for num in range(1, 11):
    z = num * number
    print(f"{number} * {num} = {z}")




