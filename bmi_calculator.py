weight =  float(input("Enter your weight in kg :   "))
height =  float(input("Enter your height in m : "))

bmi =  round(weight/(height**2))

if bmi<= 18.5 :
    print(f" your bmi is  {bmi} You are underwight")
elif bmi<= 25 :
    print(f" your bmi is  {bmi} you are normal weight")
elif bmi<= 30 :
    print(f" your bmi is  {bmi} you are slighly overweight")
elif bmi<= 35 :
    print(f" your bmi is  {bmi} you are obese")
else:
    print(f" your bmi is  {bmi} you are clinically obese")
    

