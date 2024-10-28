import random

EXPANDED_USER_CHOICES = ['r', 'p', 's', 'l', 'S']
DEFAULT_USER_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
ones = []
twos = []
SCORE_ONE = 0
SCORE_TWO = 0

print("Welcome to the Lizard Spock game, the best of three tries wins the game!")

while True:
    print(f'Let us begin! For the following options rock, paper, scissors, lizard, or spock enter: {", ".join(EXPANDED_USER_CHOICES)}')
    CHOICE = input()
    COMPUTER_CHOICE = random.choice(EXPANDED_USER_CHOICES)

    while CHOICE not in EXPANDED_USER_CHOICES:
        print("You did not type in the appropriate choices (r,p,s,l,S), please re-type choice again:")
        CHOICE = input()
        break
	
    if CHOICE == 'r':
        CHOICE  = list(CHOICE)
        CHOICE [CHOICE .index('r')] = 'rock'
        CHOICE  = " ".join(CHOICE )
    if COMPUTER_CHOICE == 'r':
        COMPUTER_CHOICE = list(COMPUTER_CHOICE)
        COMPUTER_CHOICE[COMPUTER_CHOICE.index('r')] = 'rock'
        COMPUTER_CHOICE = " ".join(COMPUTER_CHOICE)
    if CHOICE  == 's':
        CHOICE  = list(CHOICE)
        CHOICE [CHOICE .index('s')] = 'scissors'
        CHOICE  = " ".join(CHOICE)
    if COMPUTER_CHOICE == 's':
        COMPUTER_CHOICE = list(COMPUTER_CHOICE)
        COMPUTER_CHOICE[COMPUTER_CHOICE.index('s')] = 'scissors'
        COMPUTER_CHOICE = " ".join(COMPUTER_CHOICE)
    if CHOICE  == 'p':
        CHOICE  = list(CHOICE)
        CHOICE [CHOICE .index('p')] = 'paper'
        CHOICE  = " ".join(CHOICE)
    if COMPUTER_CHOICE == 'p':
        COMPUTER_CHOICE = list(COMPUTER_CHOICE)
        COMPUTER_CHOICE[COMPUTER_CHOICE.index('p')] = 'paper'
        COMPUTER_CHOICE = " ".join(COMPUTER_CHOICE)
    if CHOICE  == 'l':
        CHOICE = list(CHOICE)
        CHOICE [CHOICE.index('l')] = 'lizard'
        CHOICE = " ".join(CHOICE)
    if COMPUTER_CHOICE == 'l':
        COMPUTER_CHOICE = list(COMPUTER_CHOICE)
        COMPUTER_CHOICE[COMPUTER_CHOICE.index('l')] = 'lizard'
        COMPUTER_CHOICE = " ".join(COMPUTER_CHOICE)
    if CHOICE == 'S':
        CHOICE = list(CHOICE)
        CHOICE[CHOICE.index('S')] = 'spock'
        CHOICE = " ".join(CHOICE)
    if COMPUTER_CHOICE == 'S':
        COMPUTER_CHOICE = list(COMPUTER_CHOICE)
        COMPUTER_CHOICE[COMPUTER_CHOICE.index('S')] = 'spock'
        COMPUTER_CHOICE = " ".join(COMPUTER_CHOICE)
	
    player = CHOICE
    computer = COMPUTER_CHOICE

    if ((player == 'rock' and computer == 'scissors') or 
        (player == 'paper' and computer  == 'rock') or
        (player == 'scissors' and computer  == 'paper') or
        (player == 'rock' and computer == 'lizard') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'spock' and computer == 'scissors') or 
        (player == 'scissors' and computer == 'lizard') or
        (player == 'lizard' and computer == 'paper') or 
        (player == 'paper' and computer == 'spock') or
        (player == 'spock' and computer == 'rock')):
        print(f'You chose {player}, and the computer chose {computer}')
        print('You win, you beat the computer!')
        SCORE_ONE = 1
    elif ((player == 'rock' and computer == 'paper') or 
        (player == 'paper' and computer == 'scissors') or
        (player == 'scissors' and computer == 'rock') or 
        (player == 'rock' and computer == 'spock') or
        (player == 'lizard' and computer == 'rock') or
        (player == 'spock' and computer == 'paper') or
        (player == 'scissors' and computer == 'spock') or
        (player == 'lizard' and computer == 'scissors') or
        (player == 'paper' and computer == 'lizard') or
        (player == 'spock' and computer == 'paper')):
        print(f'You chose {player}, and the computer chose {computer}')
        print('The computer wins, the computer beat you!')
        SCORE_TWO = 1
    else:
        print('Its a tie!')
        print(f'You chose {player}, and the computer chose {computer}')
        SCORE_ONE = 0
        SCORE_TWO = 0

    if SCORE_ONE == 1:
        SCOREO = 'win'
        if SCOREO == 'win':
            ones.append(SCOREO)
            print(f'your score is: {len(ones)}')
            if len(ones) == 3:
                print("You win the game!")
                break

    if SCORE_TWO == 1:
        SCORET = 'win'
        if SCORET == 'win':
            twos.append(SCORET)
            print(f'The computer score is: {len(twos)}')
            if len(twos) == 3:
                print("The computer wins the game!")
                break

