johnd = int(input("Please enter the number of days John has worked: "));
johnh = int(input("Please enter the number of hours John has worked: "));
johnm = int(input("Please enter the number of minutes John has worked: "));
billd = int(input("Please enter the number of days Bill has worked: "));
billh = int(input("Please enter the number of hours Bill has worked: "));
billm = int(input("Please enter the number of minutes Bill has worked: "));

johnMinutes = (johnd* 24 * 60)+ (johnh * 60) + (johnm)
billMinutes = (billd * 24 * 60) + (billh * 60) + (billm)

totalMinutes = johnMinutes + billMinutes

totalHours = totalMinutes // 60
totalMinutes = totalMinutes % 60
totalDays = totalHours // 24
totalHours = totalHours % 24

print("They've worked together for a grand total of ",totalDays,"days,", totalHours,"hours, and", totalMinutes, "minutes.");
