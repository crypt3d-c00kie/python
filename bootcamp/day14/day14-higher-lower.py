
from gameData import data
import random
import os #os.system('cls')


def getRandom():
    return random.choice(data)

def formatData(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def checkAnswer(guess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        return guess == "a"
    else:
        return guess == "b"
    


def main():
    print("Welcome to the higher/lower game~!")
    score = 0

    gameContinue = True
    aAccount = getRandom()
    bAccount = getRandom()

    while gameContinue:
        aAccount = bAccount
        bAccount = getRandom()

        while aAccount == bAccount:
            bAccount = getRandom()

        print(f"Compare A :: {formatData(aAccount)}.")
        print(f"Against B :: {formatData(bAccount)}.")

        guess = input("Who has the most followers? Type 'A' or 'B' :: ").lower()
        aFollowerCount = aAccount["follower_count"]
        bFollowerCount = bAccount["follower_count"]

        isCorrect = checkAnswer(guess, aFollowerCount, bFollowerCount)
        os.system('cls')

        if isCorrect:
            score += 1
            print(f"You're right! Keep going!! Current Score :: {score}")
        else:
            gameContinue = False
            print(f"You have failed. Final Score :: {score} ")

if __name__ == '__main__':
    main()