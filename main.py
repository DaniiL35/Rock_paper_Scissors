import random

# username
username = input('what is your name? ')
print(f'Hello {username} and welcome to Rock paper Scissors')

# Initialize the user and computer scores
user_score = 0
computer_score = 0


def game():
    # computer choices
    options = ['rock', 'paper', 'scissors']

    # user move
    usermove = input('rock paper scissors: ')

    # computer move
    computermove = random.choice(options)

    # Display the moves
    print(f'You chose {usermove}. The computer chose {computermove}.')

    # winning conditions
    if usermove == computermove:
        print("It's a draw ")
    elif usermove == 'scissors' and computermove == 'paper':
        print('you win')
    elif usermove == 'paper' and computermove == 'rock':
        print('you win')
    elif usermove == 'rock' and computermove == 'scissors':
        print('you win')
    elif usermove == 'scissors' and computermove == 'rock':
        print('You loose ')
    elif usermove == 'paper' and computermove == 'scissors':
        print('You loose ')
    elif usermove == 'rock' and computermove == 'paper':
        print('You loose ')
    else:
        print("invalid input")

    # new game
    newgame = input('new game (y/n): ')
    if newgame == 'y':
        game()
    else:
        print('goodbye ')
        exit()


game()


