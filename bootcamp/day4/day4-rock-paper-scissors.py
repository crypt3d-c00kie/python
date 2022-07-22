#day4
#rock paper scissors game
#based on randomization
#player vs computer

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
#rock 0 paper 1 scissors 2

user_choice = int(input("\nwhat do you choose? 0 for Rock, 1 for Paper or 2 for Scissors : "))
print(game_images[user_choice])


# rules of rock paper scissors game
# 0 (rock) beats 2 (scissors)
# 1 (paper) beats 0 (rock)
# 2 (scissors) beats 1 (paper)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!\n")
else:
    computer_choice = random.randint(0,2)
    print(f"Computer chose :")
    print(game_images[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        print("You win!\n")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!\n")
    elif computer_choice > user_choice:
        print("You lose!\n")
    elif user_choice > computer_choice:
        print("You win!\n")
    elif computer_choice == user_choice:
        print("It's a draw!!\n")


    



