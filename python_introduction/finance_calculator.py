# Variables naming

interest_rate = 0.05
user_monthly_income = float(input("Enter your monthly income: "))
user_total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# calculate monthly savings

monthly_savings = user_monthly_income - user_total_monthly_expenses

# calculate projectes savings after one year

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

# output of results

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
