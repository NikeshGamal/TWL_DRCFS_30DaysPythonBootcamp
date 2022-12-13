#initialize the player's score and the number of times thery have played

#loop that continues until player has played 5 times

#conditions for win if-else

# incremented by one if player wins and loop we print final score

# import random 
# moves=["rock","paper","scissor"]
# player1_score =0
# player2_score =0
# counter=0
# play_status = True

# while play_status:

#     random_choice=random.randint(0,2)
#     player1 = moves[random_choice]
#     player2=input("Choose your armour? ").lower()
#     print(player1)
#     print(player2)
#     if player1=="rock" and player2=="paper":
#         print("Player2 wins")
#         player2_score+=1
#     elif player1=="rock" and player2=="scissor":
#         print("Computer wins") 
#         player1_score+=1
#     elif player1=="rock" and player2=="rock":
#         print("Tie")
#     elif player1=="paper" and player2=="paper":
#         print("Tie")
#     elif player1=="paper" and player2=="scissor":
#         print("Player2 wins") 
#         player2_score+=1
#     elif player1=="paper" and player2=="rock":
#         print("Computer wins")
#         player1_score+=1
#     elif player1=="scissor" and player2=="paper":
#         print("Player1 wins")
#         player1_score+=1
#     elif player1=="scissor" and player2=="scissor":
#         print("Tie") 
#     elif player1=="scissor" and player2=="rock":
#         print("Player2 wins") 
#         player2_score+=1
#     else:
#         print("Enter valid input")
#     counter+=1

#     play_status= True if counter<5 else False

# print("Total score")
# print(f"Computer score: {player1_score}")
# print(f"Player 2 score: {player2_score}")


# ******************************************************************************************
                                     #2nd Attempt
# ******************************************************************************************
import random 
computer_score = 0
player_score = 0

moves = ["rock","scissor","paper"]

counter=0

while counter<5:
    random_choice = random.randint(0,10)%3
    computer =moves[random_choice]
    # print(f"random number: {random_choice}")

    player = input("Choose your moves from rock, paper or scissor: ").lower()
    print("*"*50)
    print(computer)
    print(player)
    print("*"*50)
    
    if player not in moves:
        print("Enter valid inputs")
        continue

    if computer == player:
        print("It's a tie")
    elif computer=="rock":
        if player == "paper":
            player_score+=1
            print("Player wins!!!!!")
        else:
            print("Computer wins!!!!")
            computer_score+=1
    elif computer=="paper":
        if player=="rock":
            print("Computer wins!!!")
            computer_score+=1
        else:
            print("Player wins!!!!")
            player_score+=1
    elif computer=="scissor":
        if player == "paper":
            print("Computer wins!!!!!")
            computer_score+=1
        else:
            print("Player wins!!!!")
            player_score+=1
    counter+=1
    # print(computer,player)

print("Total scores:")
print(f"Computer score: {computer_score}")
print(f"Player score: {player_score}")

