import random

options = ['rock', 'paper', 'scissors']  # game variables
outcome = ['win', 'loose', 'draw']  # game outcomes


def user_choice(u_choice):  # function to validate users input to one of 3 game variables
    if u_choice in options:  # if in options list
        return u_choice
    while u_choice not in options:  # if not in options list
        u_choice = input(options[0] + ", " + options[1] + " or " + options[2] + "?\n")
        u_choice = u_choice.lower()
        if u_choice in options:
            return u_choice


def determine_outcome(player, computer):
    if player == options[0]:  # player = rock
        if computer == options[0]:  # rock vs rock (draw)
            print(outcome[2])
        elif computer == options[1]:  # rock vs paper (loose)
            print(outcome[1])
        elif computer == options[2]:  # rock vs scissors (win)
            print(outcome[0])

    if player == options[1]:  # player = paper
        if computer == options[0]:  # paper vs rock (win)
            print(outcome[0])
        elif computer == options[1]:  # paper vs paper (draw)
            print(outcome[2])
        elif computer == options[2]:  # paper vs scissors (loose)
            print(outcome[1])

    if player == options[2]:  # player = scissors
        if computer == options[0]:  # scissors vs rock (loose)
            print(outcome[1])
        elif computer == options[1]:  # scissors vs paper (win)
            print(outcome[0])
        elif computer == options[2]:  # scissors vs scissors (draw)
            print(outcome[2])


while True:
    computer_choice = random.choice(options)  # random sequence, calls list [content]
    player_choice = input(options[0] + ", " + options[1] + " or " + options[2] + "?\n")
    player_choice = user_choice(player_choice)
    print("computer choose " + computer_choice + "\n")
    determine_outcome(player_choice, computer_choice)
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
