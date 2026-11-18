#blackjack
import cardHandler
import pygame

#this will be converted to pygame once i figgure out how to use it. this is just for testing

def game():
    #Stores used cards
    deltSuit = []
    deltValue = []

    #Draw initial four cards
    for i in range(4):
        newCard = cardHandler.deal()
        deltSuit.append(newCard[0])
        deltValue.append(cardHandler.cardValue(newCard[1]))

    card1 = [deltSuit[0], deltValue[0]] #player
    upcard = [deltSuit[1], deltValue[1]] #dealer, face up
    card2 = [deltSuit[2], deltValue[2]] #player
    holeCard = [deltSuit[3], deltValue[3]] #dealer, face down

#ISSUE: if an ace is drawn initiialy, the player needs the option to alter this

    playerHand = [card1, card2]
    playerSum = deltValue[0] + deltValue[2]
    dealerHand = [upcard, holeCard]
    dealerSum = deltValue[1] + deltValue[3]

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blackjack")
    clock = pygame.time.Clock()
    screen.fill((0, 128, 0))  #makes screen green
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 400)) 

    #Begin game
    print("Player Hand: ", playerHand) 
    print("Dealer's Upcard: ", upcard)

    #Gameplay
    choice = input("Would you like to hit or stand? (Enter h or s): ")
    while choice.lower() == 'h':
        newCard = cardHandler.deal()
        playerSum += cardHandler.cardValue(newCard[1])
        playerHand.append(newCard)
        print("Player Hand: ", playerHand)
        if newCard[1] == 'A':  
            aceChoice = input("You drew an ace: Would you like it to be worth 1 or 11? (Enter 1 or 11): ")
            if aceChoice == "1":
                playerSum -= 10  #Equivilent of changing the value of the ace from 11 to 1
        if playerSum > 21:
            print("Bust: Game Over!")
            break
        choice = input("Would you like to hit or stand? (h/s): ")

    #If stand, dealer's portion begins now
    if playerSum <= 21:
        print("Dealer's Hand - Upcard:", dealerHand[0], "Hole Card:", dealerHand[1])

        while dealerSum < 17:
            newCard = cardHandler.deal()
            dealerSum += cardHandler.cardValue(newCard[1])
            dealerHand.append(newCard)
            print("Dealer draws: ", newCard)

        #Determine the winner
        print("Player's Total: ", playerSum)
        print("Dealer's Total: ", dealerSum)

        if dealerSum > 21:
            print("Dealer Bust: You Win!")
        elif playerSum > dealerSum:
            print("You Win!")
        else:
            print("Dealer Wins!")

    pygame.quit()

    pass



print("Welcome to Blackjack!")
startGame = input("Do you want to start a new game? (yes/no): ")
if startGame.lower() == "yes" or startGame.lower() == "y": #will ultimatly become a while loop (or something else to allow multiple games)
    game()
else:
    print("Game ended.")