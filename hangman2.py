import random
import os

def create_splash():
    path = "art"

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    print(lines)


    print("////////Don't Flip the Table!\\\\\\\\")
    print("///////////(╯°□°)╯︵ ┻━┻\\\\\\\\\\\\\\\\")
    print("")

def get_puzzle():
    path = "data"

    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        print(str(i + 1) + ")" + f)
        
    choice = input('pick one ')
    choice = int(choice)

    file = path + "/" + file_names[choice]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    category_name = lines[0]
    puzzle = random.choice( lines[1:] )

    return puzzle

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    print("")
    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")

        if len(letter) < 2 and letter.isalpha():
            return letter
        else:
            print("")
            print("Enter one letter ya nub.")
        

def display_board(solved, guesses, strikes):
    print("")
    print(solved)
    print("(" + guesses + ")")

    if strikes == 1:
        print("(╯")
    elif strikes == 2:
        print("(╯°□°")
    elif strikes == 3:
        print("(╯°□°)╯")
    elif strikes == 4:
        print("(╯°□°)╯︵ ┻")
    elif strikes == 5:
        print("(╯°□°)╯︵ ┻━")
    elif strikes == 6:
        print("(╯°□°)╯︵ ┻━┻")
    else:
        print()

def show_result(strikes, limit):
    if strikes == limit:
        print("")
        print("ur not even good")
    else:
        print("")
        print("Noice job m8")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("")
            print("Please enter 'y' or 'n'.")

def credits_screen():
    print("")
    print("********Don't Flip the Table********")
    print("**********(╯°□°)╯︵ ┻━┻************")
    print("************************************")
    print("************By Tristan**************")

def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strikes = 0
    limit = 6

    print("")
    print(solved)

    while solved != puzzle and strikes < limit:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1
            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses, strikes)

    show_result(strikes, limit)
    

create_splash()

playing = True

while playing:
    play()
    playing = play_again()

credits_screen()

#


