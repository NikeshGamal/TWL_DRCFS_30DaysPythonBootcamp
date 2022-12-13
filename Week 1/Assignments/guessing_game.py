#import the module and generate the number

#take a player name as an input and store it in the variable 

#declare a counter variable and initialie the counter variable with 0 which will increase with each iteration

#before starting while loop print the name of the player

#give plaeyr atmost 5 attempts
#check for the 3 conditions

#if not succeeded in 5 attempts then print message for not being able to guess the number 

import random
# print(random_number)
username = input("How would you like to call yourself: ")
print(f"*"*50)
print(f"Player name: {username}")
play_status = True

#added option for the player whether the player wants to continue play the game 
while play_status:
    random_number = random.randint(1,10)
    attempts=0
    while attempts < 5:
        print(f"*"*50)
        guess = int(input("Enter your guess: "))
        if guess < random_number:
            print("Your guess is too low")
        elif guess > random_number:
            print("Your guess is too high")
        elif guess == random_number:
            print(f"Congratulation! You have successfully guessed the number i.e. {guess}  in {attempts+1} attempts")
            break

        attempts+=1
    if attempts ==5:
        print(f"Sorry! You couldn't guess the number in 5 tries.Number to be guessed is:{random_number}") 
    print(f"*"*50)
    ans = input("Do you want to coninue this game?(Y/y for yes) ")
    play_status = True if (ans == 'Y' or ans=='y') else False  #ternary operator 
