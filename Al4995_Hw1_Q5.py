print("Please enter the number of coins for the following:");
quarters = int(input("Number of quarters:"));
dimes = int(input("Number of dimes:"));
nickels = int(input("Number of nickels:"));
pennies = int(input("Number of pennies:"));

money = (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies);
dollars = int(money/100)
cents = money % 100

#print(money)
#print(dollars)
#print(cents)

print("The total is", dollars, "dollars and", cents, "cents");
