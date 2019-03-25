#file to compute payment amount after purchasing two items
#bogo, lower price item is halved
#club card = 10% off
#tax is added (8.25 %)

item1 = int(input("Please enter the price of the first item: "));
item2 = int(input("Please enter the price of the second item: "));
club = (input("Do you have a club card? (Y/N or y/n) "));
tax = float(input("Please enter the tax rate percentage as a number (e.g. 5.5 is 5.5%): "));

base = item1 + item2
tax = tax / 100

if (item1 > item2):
    item2 = item2 * 0.5
elif (item1 < item2):
    item1 = item1 * 0.5
        
discount = item1 + item2

if(club == "Y" or club == "y"):
    discount -= discount *0.1;

    
total =  (discount * tax) 
total = round(discount + total, 2)


print( "Base price  = ",base)
print("Price after discounts = ", discount)
print("Total price = ", total)
