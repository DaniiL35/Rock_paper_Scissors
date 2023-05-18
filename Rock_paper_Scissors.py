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

    # input validation
    while usermove not in options:
        usermove = input("invalid move let's try again ")

    # computer move
    computermove = random.choice(options)

    # Display the moves
    print(f'You chose {usermove}. The computer chose {computermove}.')

    # Winning conditions
    if usermove == computermove:
        print("It's a draw")
    elif (usermove == 'rock' and computermove == 'scissors') or (usermove == 'paper' and computermove == 'rock') or (
            usermove == 'scissors' and computermove == 'paper'):
        print('You win')
        global user_score
        user_score += 1
    else:
        print('You lose')
        global computer_score
        computer_score += 1

    # Display scores
    print(f'{username}: {user_score} - Computer: {computer_score}')

    # new game
    newgame = input('new game (y/n): ')
    if newgame == 'y':
        game()
    else:
        print('goodbye ')
        exit()


game()

