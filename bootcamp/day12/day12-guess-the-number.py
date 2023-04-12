
from random import randint

ezTurns = 10
hardTurns = 5

def set_difficulty():
    level = input("Choose a difficulty! Type 'easy' or 'hard' :: ")
    if level == 'easy':
        return ezTurns
    elif level == 'hard':
        return hardTurns
    else:
        print("Incorrect, options! Read the caption-")
        quit()

def checkAnswer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("Too low")
        return turns-1
    else:
        print(f"Voila! You got it!, The correct answer was {answer} ")

def main():
    print("The Number Guessing Game!")
    print("Lemme think of a number between 1 - 100 >.<")

    answer = randint(1,100)
  
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess it correctly!!")
        guess = int(input("Make a guess :: "))

        turns = checkAnswer(guess, answer, turns)
        if turns == 0:
            print("You lose!, Ran outta guesses")
            print(f"Oof, the correct answer was {answer}")
            return
        elif guess != answer:
            print("Try again! ")


    
if __name__ == '__main__':
    main()