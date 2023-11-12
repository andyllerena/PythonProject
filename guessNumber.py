#Write a program where the computer randomly generates a number between 1 and 100.
#The user needs to guess what the number is. If the user's guess is wrong, tell them if 
#they guessed too high or too low.
#Count the number of attempts taken for the user to guess the number correctly.

import random

randomNumber = random.randint(1,100)
guess = None
attempts = 0
print(randomNumber)

while guess != randomNumber:
    guess = int(input("Enter a number between 0 and 100 "))
    attempts +=1
    if guess < randomNumber:
        print("Higher!")
        
    elif guess > randomNumber:
        print("Lower!")
        
    else:
        print("You guessed the number in " + str(attempts) + " attempts. ")

    

