H=float(input("Enter your height:"))
W=float(input("Enter your weight:"))

bmi=W/(H/100)**2
       
print("Your BMI:", bmi)

if bmi<=18.5:
    print("You are underweight!")

elif bmi<=24.6:
    print("You are healthy!")

elif bmi<=29.4:
    print("You are overweight!")

elif bmi<=40:
    print("You are obese! Get some exercise!")
else:
    print("GET HEALTHY!!!")