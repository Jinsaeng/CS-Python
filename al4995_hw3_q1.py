weight = float(input("Please enter your weight in kilograms:"));
height = float(input("Please enter your height in meters:"));

BMI = weight / (height ** 2)


if (BMI < 18.5):
    status = ("Underweight")
elif (BMI < 24.9 ):
    status = ("Normal")
elif (BMI <29.9):
    status = "Overweight"
else:
    status = "Obese"
print("Your BMI is", BMI, ". Status:",status);
