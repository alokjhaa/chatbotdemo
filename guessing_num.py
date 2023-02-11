import math
import random

# imput the values 
lower = int(input("Enetr the minimum range :  "))
upper = int(input("Enetr the maximum range :  "))

x = random.randint(lower,upper)
chances = round(math.log(upper-lower+1,2))
print(f'Number of chances to guess the number is {chances}')

count = 0 
while count < chances:
   count+=1
   guess = int(input("Enter your guess :"))
   if guess == x :
    print(f" Congratulation you have guess correctly in {count} chances")
    break
   elif guess > x :
    print("you guess too large number !!!!")
   elif guess < x :
    print("you guess too small number !!!!")

if count >= chances :
    print(f"Better luck next time . The number is {x}")





   

