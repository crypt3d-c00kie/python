#day2
#bmi calc

height = input("height in m : ")
weight = input("weight in kg : ")

h2 = float(height) ** 2 # ** goes for exponents
bmi = round(float(weight)/h2,2)

print("\nyour bmi is ", bmi)

if bmi <= 18.5:
  print("and also, you are underweight")
elif bmi <= 24.9:
  print("and you are just fine")
elif bmi <= 29.9:
  print("and you are overweight")
else:
  print("you are obese")