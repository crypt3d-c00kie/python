#blackjack card game

import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calc_score(cards):
    """takes a list of cards and returns the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(userScore, computerScore):
    """if else conditions that compares who wins"""
    if userScore == computerScore:
        return "-- Draw --"
    elif computerScore == 0:
        return "-- Lost -- Opponent has Blackjack!"
    elif userScore == 0:
        return "-- Win -- with a Blackjack"
    elif userScore > 21:
        return "-- Lost -- You went over"
    elif computerScore > 21:
        return "-- Win -- Opponent went over"
    elif userScore > computerScore:
        return "-- Win --"
    else:
        return "-- Lose --"

def main():
    user = []
    computer = []
    gameOver = False

    for _ in range(2): #looping without iterator
        user.append(deal_card())
        computer.append(deal_card())

    while not gameOver:
        userScore = calc_score(user)
        computerScore = calc_score(computer)
        print(f"Your cards :: {user}, current score :: {userScore}")
        print(f"Computer's first card :: {computer[0]}")
        
        if userScore == 0 or computerScore == 0 or userScore > 21:
            gameOver = True
        else:
            hitCard = input("Type 'hit' to get card or 'stand' to hold :: ")
            if hitCard.lower() == 'hit':
                user.append(deal_card())         
            else:
                gameOver = True
    while computerScore != 0 and computerScore < 17:
        computer.append(deal_card())
        computerScore = calc_score(computer)

    print(f"Your final hand :: {user} <> final score :: {userScore}")
    print(f"Opponent's final hand :: {computer} <> final score :: {computerScore}")
    print(f"{compare(userScore,computerScore)}")

if __name__ == '__main__':
    main()
