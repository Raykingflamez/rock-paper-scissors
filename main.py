import random

choice = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

options = list(choice)


while True:
    user = input('\nPick "R" for rock, "P" for paper, "S" for scissors: ')
    CPU = random.choice(options)

    if user not in options:
        print("You didn't choose a valid option. Please try again\n")
    elif user == CPU:
        print("It's a tie. Try again.\n")
    else:
        print('\nPlayer ({}) : CPU ({})'.format( choice[user], choice[CPU]))
        win = user + CPU

        if win in ['RS', 'PR', 'SP']:
            print('{} beats {} \n\nYou Win!'.format(choice[user], choice[CPU],))
        elif win in ['SR', 'RP', 'PS']:
            print('{} beats {} \n\nYou Lose!'.format(choice[CPU], choice[user]))

        break
