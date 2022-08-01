#day7
#guess the word to save the man!

import os
import random
import hangman_wordlist
import hangman_ascii


print(hangman_ascii.logo)
end_game = False
word_list = ["lotus", "tulip", "sunflower", "dandelion", "rose"]
chosen_word = random.choice(hangman_wordlist.word_list)
word_length = len(chosen_word)

#print(chosen_word) #Randomly chosen word

lives = 6 #if life goes 0 you fail

#Blanks for guessing spaces
blank_list = []
for _ in range(word_length):
    blank_list += "_"


while not end_game:
    guess = input("Guess a letter  : ").lower()#input
    os.system('cls') #clear screen
    if guess in blank_list:
        print(f"You already guessed {guess}")
    #checking guessed letters
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        #print(f'''Position : {i} || Letter : {letter} || Guessed letter : {guess} ''')
        if letter == guess:
          blank_list[i] = letter
   
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed the letter {guess} that's not in the word. You lose a life!")
        if lives == 0:
            end_game = True
            print("You lose!")

    print(f"{' '.join(blank_list)}")


    if "_" not in blank_list:
        end_game = True
        print("You win!")
    print(hangman_ascii.stages[lives])