'''

Anthony Lam
CS 1114
al4995

Purpose of program- To do stuff
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    file = open(complete_weather_filename, "r")
    inside = file.readline()
    newfile = open(cleaned_weather_filename, "w")
    for line in file:
        if len(line) != 0:
            part = line.split(",")
            city = part[0]
            date = part[1]
            high = part[2]
            low = part[3]
            precipitation= part[8]
            combined = city + "," + date + "," + high + "," + low + "," + precipitation + "\n"
            newfile.write(combined)
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    
# Part B
def f_to_c(f_temperature):
    ls = f_temperature
    ls = int(ls)
    cel = float((ls - 32) * (5/9))
    return cel # modify this

def in_to_cm(inches):
    ls = inches
    precipitation = ls[:-1]
    if precipitation == "T":
        precipitation = 0
    precipitation = float(precipitation)
    cm =  precipitation *2.54
    return cm # modify this

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    file = open(imperial_weather_filename, "r")
    file2 = open(metric_weather_filename, "w")
    for line in file:
        if len(line) !=0:
            part = line.split(",")
            city = part[0]
            date = part[1]
            c_temperature_high = str(f_to_c(part[2]))
            c_temperature_low = str( f_to_c(part[3]))
            centimeters = in_to_cm(part[4])
            combined = city + "," + date + "," + c_temperature_high + "," + c_temperature_low + "," + str(centimeters) + "\n"
            file2.write(combined)
    # Similar to clean_data() - read in the file and make a new file with metric values.



# Part C
def print_average_temps_per_month(city, weather_filename, unit_type):
    file = open(weather_filename, "r")
    high = []
    low = []
    count = 0;
    high1= 0;high2= 0;high3= 0;high4= 0; high5= 0;high6= 0;
    high7= 0;high8= 0;high9= 0;high10= 0;high11= 0;high12= 0;
    low1 = 0;low2 = 0;low3 = 0;low4 = 0;low5 = 0;low6 = 0;
    low7 = 0;low8 = 0;low9 = 0;low10 = 0;low11= 0;low12 = 0;
    monthcount1 = 0;monthcount2 = 0;monthcount3 = 0;monthcount4 = 0;monthcount5 = 0;
    monthcount6 = 0;monthcount7 = 0;monthcount8 = 0;monthcount9 = 0;monthcount10 = 0;
    monthcount11 = 0;monthcount12 = 0;
    for line in file:
        part = line.split(",")
        name = part[0]
        if name == city:
            count+=1
            date = part[1]
            component = date.split("/")
            month = component[0]
            high = part[2]
            low = part[3]
            if month == "1":
                month = "January"
                monthcount1 += 1
                high1 += float(high)
                low1 += float(low)
            elif month == "2":
                month = "February"
                monthcount2 += 1
                high2 += float(high)
                low2 += float(low)
            elif month == "3":
                month = "March"
                monthcount3 += 1
                high3 += float(high)
                low3 += float(low)
            elif month == "4":
                month = "April"
                monthcount4 += 1
                high4 += float(high)
                low4 += float(low)
            elif month == "5":
                month = "May"
                monthcount5 += 1
                high5 += float(high)
                low5 += float(low)
            elif month == "6":
                month = "June"
                monthcount6 += 1
                high6 += float(high)
                low6 += float(low)
            elif month == "7":
                month = "July"
                monthcount7 += 1
                high7 += float(high)
                low7 += float(low)
            elif month == "8":
                month = "August"
                monthcount8 += 1
                high8 += float(high)
                low8 += float(low)
            elif month == "9":
                month = "September"
                monthcount9 += 1
                high9 += float(high)
                low9 += float(low)
            elif month == "10":
                month = "October"
                monthcount10 += 1
                high10 += float(high)
                low10 += float(low)
            elif month == "11":
                month = "November"
                monthcount11 += 1
                high11 += float(high)
                low11 += float(low)
            elif month == "12":
                month = "December"
                monthcount12 += 1
                high12 += float(high)
                low12 += float(low)
    avghigh1 = int(high1/monthcount1)
    avghigh2 = int(high2/monthcount2)
    avghigh3 = int(high3/monthcount3)
    avghigh4 = int(high4/monthcount4)
    avghigh5 =int( high5/monthcount5)
    avghigh6 = int(high6/monthcount6)
    avghigh7 = int(high7/monthcount7)
    avghigh8 = int(high8/monthcount8)
    avghigh9 =int( high9/monthcount9)
    avghigh10 =int( high10/monthcount10)
    avghigh11 = int(high11/monthcount11)
    avghigh12 =int( high12/monthcount12)
    avglow1 = int(low1/monthcount1)
    avglow2 =int( low2/monthcount2)
    avglow3 =int( low3/monthcount3)
    avglow4 = int(low4/monthcount4)
    avglow5 = int(low5/monthcount5)
    avglow6 = int(low6/monthcount6)
    avglow7 = int(low7/monthcount7)
    avglow8 = int(low8/monthcount8)
    avglow9 = int(low9/monthcount9)
    avglow10 = int(low10/monthcount10)
    avglow11= int(low11/monthcount11)
    avglow12 = int(low12/monthcount12)
    if unit_type == "metric":
        temp = "C"
    else:
        temp = "F"
    print("Average Temperatures for " , city)
    print()
    print("January:", avghigh1, temp, "high", avglow1, temp, "low")
    print("February:", avghigh2, temp, "high", avglow2, temp, "low")
    print("March:", avghigh3, temp, "high", avglow3, temp, "low")
    print("April:", avghigh4, temp, "high", avglow4, temp, "low")
    print("May:", avghigh5, temp, "high", avglow5, temp, "low")
    print("June:", avghigh6, temp, "high", avglow6, temp, "low")
    print("July:", avghigh7, temp, "high", avglow7, temp, "low")
    print("August:", avghigh8, temp, "high", avglow8, temp, "low")
    print("September:", avghigh9, temp, "high", avglow9, temp, "low")
    print("October:", avghigh10, temp, "high", avglow10, temp, "low")
    print("November:", avghigh11, temp, "high", avglow11, temp, "low")
    print("December:", avghigh12, temp, "high", avglow12, temp, "low")
    print()
    
    # prints average highs and lows in each month for the given city

    
# Part D
# Write your question (as a comment), and implement a function to answer it
#Highest temperature in given city?


def print_hotter_city(city, weather_filename, data_type):
    file = open(weather_filename, "r")
    numbers = []
    for line in file:
        part = line.split(",")
        name = part[0]
        date = part[1]
        if name == city:
            high = part[2]
            high = float(high)
            numbers.append(high)
    if data_type == "imperial":
        temp = "F"
    else:
        temp = "C"
    print("The highest recorded temperature in", city, " was:" , max(numbers), temp, "on", date)

def main():
    print ("Running Part A")
    clean_data("weather.csv", "cleanedweather.csv")
    
    print ("Running Part B")
    convert_data_to_metric("cleanedweather.csv", "weatherinmetric.csv")
#weather in imperial will be changed to cleanedweather.csv
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "cleanedweather.csv", "imperial")
    print_average_temps_per_month("New York", "weatherinmetric.csv", "metric")
    print_average_temps_per_month("San Jose", "cleanedweather.csv", "imperial")

    print ("Running Part D")
    print_hotter_city("New York", "cleanedweather.csv", "imperial")
##    

    
main()


