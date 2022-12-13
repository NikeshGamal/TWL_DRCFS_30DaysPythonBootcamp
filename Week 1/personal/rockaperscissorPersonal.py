import random 
computer_score = 0
player_score = 0

moves = ["rock","scissor","paper"]

counter=0

while counter<5:
    random_choice = random.randint(0,2)
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
    elif computer=="rock":  #computer =rock   bhane player == paper or scissor  
        if player == "paper":  #player = paper
            player_score+=1
            print("Player wins!!!!!")
        else:   # automaticallay player= scissor
            print("Computer wins!!!!")
            computer_score+=1
    elif computer=="paper":         #computer == paper   so player =rock or scissor
        if player=="rock": #rock
            print("Computer wins!!!")
            computer_score+=1
        else: #scissor
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
