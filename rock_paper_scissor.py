"""
This is a python game of rock, paper, scissor that interacts with the terminal command line.
"""

import random

user_W, computer_W = 0, 0

selected = ["rock", "paper", "scissor"]

while True:
    user_input = input("\nType Rock, Paper, Scissor or Q to quit: ")
    if user_input == "q":
        break
    
    if computer_W == 2 or user_W == 2:
        break


    if user_input not in selected:
        continue

    #index represented by 0-2 for 3 options
    random_num = random.randint(0,2)

    computer = selected[random_num]
    print(f"\nComputer chose {computer}.")

    if user_input == "rock" and computer == "scissors":
        print("you won this round!, goodluck best out out of 3!")
        user_W += 1
        continue

    elif user_input == "paper" and computer == "rock":
        print("you won this round!, goodluck best out out of 3!")
        user_W += 1
        continue

    elif user_input == "scissor" and computer == "paper":
        print("you won this round!, goodluck best out out of 3!")
        user_W += 1
        continue

    elif user_input == computer:
        print("Tie!\n")
        continue

    else:
        print("you lost this round!\n")
        computer_W += 1


print(f"\nThe game results are You: {user_W} to Computer: {computer_W}")   
print("Take care, goodbye!")