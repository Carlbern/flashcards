import random
import deckClass
import readFile
import os
clear = lambda: os.system('clear')
readFile.readFile(deckClass.deck)

     
def play(deck):
    points = 0
    tempCards = deck.cards.copy()
    random.shuffle(tempCards)

    for card in tempCards:
        clear()
        print(card.wordOne)
        inp = input()

        clear()
     
        print(card.wordTwo)

        print(inp.lower() + " " + card.wordTwo.lower())
        print(inp.lower() == card.wordTwo.lower())

        if inp.lower() == card.wordTwo.lower():
            print("här")
            points += 1
        
        print(points)
        hold = input()

       
           

    