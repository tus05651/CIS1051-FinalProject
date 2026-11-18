#cardHandler
import random

def deal():
    #deal a card from the deck
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suit = random.choice(suits)
    value = random.choice(values)
    return suit, value

#Value will be what is on the card, points is what it is worth in the game.

#This function returns the points of a card based on its value.
def cardValue(value):
    if value in ["J", "Q", "K"]:
        return 10
    if value == "A":
        #This will count aces as 11, the user can change this to 1 as part of the game function
        return 11
    return int(value) #If number card, the value does not change, but this makes it an int