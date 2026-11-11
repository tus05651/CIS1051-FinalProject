#cardHandler
import random

def deal():
    #deal a card from the deck
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suit = random.choice(suits)
    value = random.choice(values)
    return suit, value

'''There will need to be a way to keep track of what is delt to prevent duplicate draws.
probably not in this file 
'''
def cardValue(value):
    if value in ["J", "Q", "K"]:
        return 10
    if value == "A":
        #Ace can be 11 or 1 depending on the hand
        #For now it will be 11, though there will be a way to change it to 1
        return 11
    return int(value) #If number card, the value does not change