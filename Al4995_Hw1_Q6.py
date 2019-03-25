#print("Please enter the number of coins for the following:");
#quarters = int(input("Number of quarters:"));
#dimes = int(input("Number of dimes:"));
#nickels = int(input("Number of nickels:"));
#pennies = int(input("Number of pennies:"));

print("Please enter the amount in two separate lines:");
dollars = int(input());
cents = int(input());

money = (dollars * 100) + cents;
NumQ = int(money / 25)
NewNumQ = NumQ * 25;
money2 = money - NewNumQ ;
NumD = int(money2/ 10);
NewNumD = NumD * 10
money3 = money2 - NewNumD
NumN = int(money3 / 5);
NewNumN = (NumN * 5);
money4 = money3 - NewNumN
NumP = money4

#print(money, money2, money3, money4);
#print(NumQ, NumD, NumN, NumP)

print(dollars, "dollars and", cents, "cents are:")
print(NumQ, "quarters,", NumD, "dimes, ", NumN, "nickels, and", NumP, "pennies.");
