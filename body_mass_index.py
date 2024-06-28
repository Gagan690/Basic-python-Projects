def body_mass():
    h = float(input("Enter your Height in Meter : "))
    # "The Height Should be in meter"
    w = float(input("Enter your Weight in kilogram : "))
    # "The Weight Should be in kilogram"
    bmi = w / (h*h)
    print(f"Your BMI score is : {bmi}")
    if bmi < 18.5:
        print("You are Underweight...")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You are in Normal Weight...")
    elif bmi >= 25.0 and bmi <= 29.9:
        print("You are in Overweight... ")
    elif bmi >= 30.0 and bmi <= 34.9:
        print("You are in Obesity 1...")
    elif bmi >= 35.0 and bmi <= 39.9:
        print("You are in Obesity 2...")
    elif bmi > 40:
        print("You are in Obesity 3...")
    else :
        return 0

body_mass() 