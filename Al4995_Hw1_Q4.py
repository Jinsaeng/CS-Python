year = int(input("Please enter the year:")) - 2017;
births = (3600 * 24 * 365) / 7;
# adding 1/7 per second, * 60seconds/min * 60minutes/hr * 24hours/day * 365days/yr
deaths = (3600 * 24 * 365) / 13;
immigrant = (3600 * 24 * 365) / 35;
population_17 = 307357870;

population =  ((year * (births + immigrant)) - (year * deaths)) + population_17;

#should calculate the change based on inputted year then add to 2017's population count
#If year is less than 2017, should be smaller number due to subtraction
# this program seems to do the rate of change as a constant since rates of b/d/i are constant

print((population));
