weight = float(input("Please enter your weight in pounds:"));
height = float(input("Please enter your height in inches:"));

BMI = (weight*0.453592) / ((height*0.0254) ** 2)

#conversion using the note in the hw, pounds to kilo and inches to meters
#the example BMI is close to the one produced by the program but not exact?
#possible due to rounding issues?

print(BMI)

