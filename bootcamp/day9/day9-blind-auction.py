# blind auction 
import os

def findMaxBid(bidDict):
    #bidDict = {"Alicia" : 222, "Jamie" : 121}
    maxBid = 0
    for bidder in bidDict:
        if bidDict[bidder] > maxBid:
            maxBid = bidDict[bidder]
            winner = bidder
    print(f"The Winner is {winner} with the highest bid of ${maxBid}")
    
def main():
    print("Welcome to the secret auction!")
    bids = {}
    finish = False
    while not finish:
        name = input('What is your name? :: ')
        money = int(input('What is your bid? :: $'))
        bids[name] = money
        
        choice = input('Are there any other bidders? Type "Yes" or "No" :: ')
        if choice.lower() == "no":
            finish = True
            findMaxBid(bids)
        else:
            os.system('cls')
        
if __name__ == '__main__':
    main()
