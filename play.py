import random
import deckClass
import readFile
import os
clear = lambda: os.system('clear')
readFile.readFile(deckClass.deck)

     
def play(deck):
    tempCards = deck.cards
    random.shuffle(tempCards)

    for card in tempCards:
        clear()
        print(card.wordOne)
        hold = input()
        clear()
        print(card.wordTwo)
        hold = input()

play(deckClass.deck)
    