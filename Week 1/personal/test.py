import random
moves=['scissor','paper','rock']


player_score=0
computer_score=0

counter = 0
while counter <5:
    random_choice = random.randint(0,2)
    computer =moves[random_choice]
    player = input('Enter the choice:').lower()

    if player not in moves:
        print('Invalid moves')
        break

    print(computer,player)

    if computer == player:
        print('*'*60)
        print('Its a tie')
        print('*'*60)
    elif computer == 'rock':
        if player == 'paper':
            print('*'*60)
            print('Player wins')
            print('*'*60)
            player_score+=1
    elif computer == 'rock':
        if player == 'scissor':
            print('*'*60)
            print('Computer wins')
            print('*'*60)
            computer_score+=1   
    elif computer == "paper":
        if player == 'scissor':
            print('*'*60)
            print('Player wins')
            print('*'*60)
            player_score+=1
    elif computer == 'paper':
        if player == 'rock':
            print('*'*60)
            print('Computer wins')
            print('*'*60)
            computer_score+=1
    elif computer == 'scissor':
        if player == 'rock':
            print('*'*60)
            print('Player wins')
            print('*'*60)
            player_score+=1
    elif computer == 'scissor':
        if player == 'paper':
            print('*'*60)
            print('Computer wins')
            print('*'*60)
            computer_score+=1   

    counter+=1


