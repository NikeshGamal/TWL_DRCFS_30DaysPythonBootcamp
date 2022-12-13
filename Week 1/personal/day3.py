#number guessing game

#1.generate a random number (random module)
#create-------(inside loop)-------------
#2.take input from user (int) (input())
#3.compare the number ( if else)
    #equals --> then end game
    #lower--> The number is greater
    #Greater-->The number is lower

#4. again take input from user (int)
#5. end the game and reveal the number after certain try

import random as rd

#include both number
random_number=rd.randint(1,10)


#logic build
#_ -->is a variable but the value is not saved
for i in range(3):
    guess = int(input("Enter you guess number: "))

    if random_number == guess:
        print("*"*50)
        #f string
        print(f"HURRAY!!! You got the correct guess in {i+1} attempts")
        print("*"*50)
        break
    elif guess > random_number:
        print("*"*50)
        print("Your guess is greater than the random number")
        print("*"*50)
    else:
        print("*"*50)
        print("Your guess is lower than the random number")
        print("*"*50)