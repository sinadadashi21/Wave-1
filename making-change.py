cost = int(input("Enter the number of cents: "))

toonies = cost // 200
after_toonies = cost % 200

loonies  = after_toonies // 100
after_loonies = after_toonies % 100

quarters = after_loonies // 25
after_quarters = after_loonies % 25

dimes = after_quarters // 10
after_dimes = after_quarters % 10

nickels = after_dimes // 5
after_nickels = after_dimes % 5

pennies = after_nickels // 1

print("Your change is")
print("Toonies:", toonies)
print("Loonies:", loonies)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
