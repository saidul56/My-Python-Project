w=int(input("Enter your weight(Kg) : "))
h=int(input("Enter your height(Feet) : "))
h1=int(input("Enter your height(Inchi) : "))
h2=(h*12)+h1
h_m=h2*0.0254  
bmi=w/(h_m*h_m)
print("Your Body Mass Index (BMI) is : ",bmi)

print("Comments:")
if bmi<18.5:
    print("OH, You are underweight.")
elif 18.5 <= bmi <= 24.9:
    print("You have a normal weight.")
elif 25 <= bmi <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
