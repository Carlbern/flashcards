import random
import modules.formatting as formatting
from colorama import Fore
import os
clear = lambda: os.system('clear')
  
def play(deck):
    points = 0
    tempCards = deck.cards.copy()
    random.shuffle(tempCards)

    for card in tempCards:
        asterisks = formatting.printCardBorder(card.wordOne)
 
        clear()
        print(Fore.WHITE + asterisks)
        print(f"** {card.wordOne} **")
        print(asterisks)
        inp = input("Guess: ")

        ##CREATES ASTERISKS FOR BORDER##
        asterisks = formatting.printCardBorder(card.wordTwo)

        #PLAYER GETS IT RIGHT
        if inp.lower() == card.wordTwo.lower():
            points += 1
            clear()
            print(Fore.GREEN + asterisks)
            print(f"** {card.wordTwo} **")
            print(asterisks)
            hold = input("Press enter to continue.. ")
        #PLAYER GETS IT WRONG
        else:
            clear()
            print(Fore.RED + asterisks)
            print(f"** {card.wordTwo} **")
            print(asterisks)
            hold = input("Press enter to continue.. ")

        #GAME IS OVER
    clear()
    print(Fore.WHITE + f"Game is over, you knew {points} out of {len(tempCards)} answers")

       
           

    