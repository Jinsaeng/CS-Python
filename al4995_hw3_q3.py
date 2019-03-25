
day = input("Please enter the day the call started (Mon/ Tue/ Wed/ Thr/ Fri/ Sat/ Sun): ");
time = int(input("Please enter the time the call started at (hhmm): "));
minutes = int(input("Please enter the duration of the call (in minutes): "));

if (day == "Sun" or day == "Sat"):
    cost = 0.15 * minutes
else:
    if (time < 800 or time > 1800):
        cost = 0.25 * minutes
    else:
        cost = 0.4 * minutes
print("The call will cost ", cost)
