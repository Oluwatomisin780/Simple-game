
import random


def play_game():
    choices=["R","S","P"]
    user_input =  input('Enter the correct choice ').upper()
    while user_input not in choices:
        print (input('Enter a valid choice'))
    if  user_input =="R":
        user_choice = 'rock'
    elif user_input == "S":
        user_choice = 'scissors'
    elif user_input =="P":
        user_choice = 'paper'
    computer = random.choice(choices)
    if computer =="R":
        computer_choice= 'rock'
    elif computer =="S":
        computer_choice = 'scissors'
    elif computer == "P":
        computer_choice ='paper'
    print(f'players choice is {user_choice} : computer choice is {computer_choice}')
    if user_input == computer:
        return play_game()
    elif  user_input =='R' and computer =='p' or user_input == 'P' and computer =='S' or user_input == 'S' and computer =='R':
        return 'computer wins'
    else:
        return 'player won'



print(play_game())