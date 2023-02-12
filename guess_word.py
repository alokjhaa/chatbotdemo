import random
name = input("Enter your name =   ")

print("Good Luck !  ", name)

words = [ 'rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print(" Please enter the charatcter : ")

guesses =' '
chance = 12

while chance > 0 :
    failed = 0
    for char in word :
        if char in guesses :
         print(char)
        else :
         print('_')
         failed += 1
    if failed == 0 :
        print(" Congratulation ! you win ")
        print(f" The word is {word}")
        break
   
    guess = input("Enter the character : ")
    guesses += guess
    if guess not in word :
        chance -= 1
        print("Wrong !!")
        print(f'you have {chance} more chances')
        if chance == 0 :
            print("you loose !!")

    

