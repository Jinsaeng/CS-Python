def print_month_calendar(num_of_days, starting_day):
    print("Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun", sep = "\t")
    empty = starting_day - 1
    for i in range(empty):
        print(" ", end = "\t")
    for j in range (1,(9-starting_day)):
        print(j, end = "\t") #counting days
    change_of_week = 0;
    for k in range(9- starting_day, num_of_days +1 ): #note
        print(k, end = "\t")
        change_of_week += 1
        if change_of_week == 7:
            print("\n") #reset week
            change_of_week = 0;
        last_day = (num_of_days - (8-starting_day)) %7
    print("\n")
    return last_day

def check_leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def print_year_calendar(year, starting_day):
    leap = check_leap(year)
    for month in range(1,13):
        if month < 9 and month % 2 == 1:
            num_of_days = 31
            if month == 1:
                print("January", year, "\n")
            elif month == 3:
                print("March", year, "\n")
            elif month == 5:
                print("May", year, "\n")
            elif month == 7:
                print("July", year, "\n")
        elif month >= 8 and month % 2 == 0:
            num_of_days = 31
            if month == 8:
                print("August", year, "\n")
            elif month == 10:
                print("October", year, "\n")
            elif month == 12:
                print("December", year, "\n")
        elif month == 2:
            print("February", year, "\n")
            if leap:
                num_of_days = 29
            else:
                num_of_days = 28
        elif month != 2 and month % 2 == 0 and month >= 9:
            num_of_days = 30
            if month == 4:
                print("April", year, "\n")
            elif month == 6:
                print("June", year, "\n")
        elif month >= 8 and month % 2 == 1:
            num_of_days= 30;
            if month == 9:
                print("September", year, "\n")
            elif month == 11:
                print("November", year, "\n")
        last_day= print_month_calendar(num_of_days, starting_day)
        if (last_day + 1) <= 7:
            starting_day = last_day + 1
        else:
            starting_day = 1
            print()

#def main():
year =  int(input("Enter a year: "));
starting_day = int(input("Enter the starting day with numbers 1-7: "));
print(print_year_calendar(year,starting_day))

#note: makes the first week of every month extend for 2 weeks in one line when it should stop at SUN and reset the week to 0
