principal = float(input("Enter the principal amount deposited in dollars: " ))
first_year = principal * (4/100) + principal
second_year = first_year * (4/100) + first_year
third_year = second_year * (4/100) + second_year
print("You will have: $" + str(round(first_year, 2)) + " after one year.")
print("You will have: $" + str(round(second_year, 2)) + " after two years.")
print("You will have: $" + str(round(third_year, 2)) + " after three years.")

