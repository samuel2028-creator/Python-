weight = float(input("How much do you weigh? Enter you weight in kilograms!"))
height = float(input("How tall are you? Enter your height in Meters!"))

BMI = weight / (height ** 2) 

if BMI < 18.5:
    print(f"{BMI:.2f} Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print(f"{BMI:.2f} Normal Weight")
elif BMI >= 25 and BMI <= 29.9:
    print(f"{BMI:.2f} OverWeight")
elif BMI >= 30:
    print(f"{BMI:.2f} Obese")
else:
    print("Invalid Input")
