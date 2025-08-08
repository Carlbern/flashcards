import random
from colorama import Fore
import os
clear = lambda: os.system('clear')


     
def play(deck):
    points = 0
    tempCards = deck.cards.copy()
    random.shuffle(tempCards)

    for card in tempCards:

        ##CREATES ASTERISKS FOR BORDER##
        asterisks = ""
        i = 0
        while i < len(card.wordOne) + 6:
            if i == 0 or i == (len(card.wordOne) + 5):
                asterisks+=" "
            else:
                asterisks+="*"
            i+=1
                
        clear()
        print(Fore.WHITE + asterisks)
        print(f"** {card.wordOne} **")
        print(asterisks)
        inp = input("Guess: ")

        ##CREATES ASTERISKS FOR BORDER##
        asterisks = ""
        i = 0
        while i < len(card.wordTwo) + 6:
            if i == 0 or i == (len(card.wordTwo) + 5):
                asterisks+=" "
            else:
                asterisks+="*"
            i+=1

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

       
           

    