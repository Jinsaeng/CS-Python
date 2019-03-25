##def print_shifted_triangle(n,m,symbol):
##    matrix = "";
##    for i in range(2*n):
##        if i % 2 == 0:
##            j = 0
##        else:
##            j = i
##        line = (" " * m) + ((2* n-i) * " ")+ (j * symbol) + "\n"
##        matrix +=line
##    return matrix
##def print_pine_tree(n, symbol):
##    pine = "";
##    for i in range(1, n+1):
##        result = print_shifted_triangle(i+1, n-i, symbol) + "\n"
##        pine += result
##    return pine
##def main():
##    print(print_pine_tree(n, symbol))
##
##
##def print_month_calendar(num_of_days, starting_day):
##    print("Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun", sep = "\t")
##    empty = starting_day - 1
##    for i in range(empty):
##        print(" ", end = "\t")
##    for j in range (1,9-starting_day):
##        print(j, end = "\t")
##    change_of_week = 0;
##    for k in range(9- starting_day, num_of_days +1 ):
##        print(k, end = "\t")
##        change_of_week += 1
##        if change_of_week == 7:
##            print()
##            change_of_week = 0;
##        last_day = (num_of_days - (8-starting_day) %7)
##    return last_day
##
##def check_leap(year):
##    if year % 400 == 0:
##        return True
##    elif year % 4 == 0 and year % 100 != 0:
##        return True
##    else:
##        return False
##
##def print_year_calendar(year, starting_day):
    leap = check_leap(year)
    for month in range(1,13):
            if month == 1:
                print("January", year)
                num_of_days = 31
            elif month == 2:
                print("February", year)
                if leap:
                    num_of_days = 29
                else:
                    num_of_days = 28
            elif month == 3:
                print("March", year)
                num_of_days = 31
            elif month == 4:
                print("April", year)
                num_of_days = 30
            elif month == 5:
                print("May", year)
                num_of_days = 31
            elif month == 6:
                print("June", year)
                num_of_days = 30
            elif month == 7:
                print("July", year)
                num_of_days = 31
            elif month == 8:
                print("August", year)
                num_of_days = 31
            elif month == 9:
                print("September", year)
                num_of_days = 30
            elif month == 10:
                print("October", year)
                num_of_days = 31
            elif month == 11:
                print("November", year)
                num_of_days = 30
            elif month == 12:
                print("December", year)
                num_of_days = 31
            

##        last_day= print_month_calendar(num_of_days, starting_day)
##        if l(ast_day + 1) <= 7:
##            starting_day = last_day+1
##        else:
##            starting_day = 1
##
##def main():
##   year =  input("Enter a year: ");
##   starting_day = int(input("Enter the starting day with numbers 1-7: "));
##   print_year_calendar(year,starting_day)
##
##
##
def first_word(phrase):
    first = phrase.find(" ");
    word = phrase[0 : first]
    return word

def rest_of_it(phrase):
    first = phrase.find(" ");
    rest = phrase[first + 1:]
    return rest
##
##def main():
##    phrase = "the quick brown fox"
##
phrase = input("String:")
first = 0
newstring2 = ""
word1 = first_word(phrase)
while phrase.find(" ") != -1:
    first = phrase.find(" ");
    word = phrase[0: first+1]
    rest = rest_of_it(phrase)
    phrase = rest
    newstring = word
    newstring3 = newstring + newstring2
    newstring2 = newstring3
newstring2 = rest + " " + newstring3
print(newstring2)

