#THIS IS THE MAIN PROGRAM INDEX
import addCard
import writeToFile
import owner
import readFile
import play
from colorama import Fore
import os
clear = lambda: os.system('clear')
readFile.readFile(owner.filip.decks[0])

while True:
    clear()

    print(Fore.WHITE + "Welcome to FlashCards!\n")
    print("Please choose an options below")

    print("1.Play deck")
    print("2.Add Card to deck")
    print("3.Remove cards")
    print("4.Exit programme")
    print("________________")

    selection = int(input("Select option: "))
    match selection:
        case 1: #PLAY GAME
            clear()
            i = 0
            print("Decks:")
            print("")
            for decks in owner.filip.decks:
                print(f"{i + 1}. {decks.name}")

                i+=1
                
            print(          "_____________________________")
            inp = int(input("Type number of deck to play: "))           
            play.play(owner.filip.decks[inp - 1]) 

            
            hold = input()
        case 2: #ADD CARD
            clear()
            print("Write first word")
            wordOne = input()
            clear()
            print("Write second word")
            wordTwo = input()

            addCard.addCard(owner.filip.decks[0].cards, wordOne, wordTwo)

        case 3:
            clear()

            #PRINTS DECKS
            print("Decks:")
            print("")
            i = 0
            for decks in owner.filip.decks:
                print(f"{i + 1}. {decks.name}")

                i+=1
                
            print(          "_____________________________")
            inpDeck = int(input("Type number of deck to modify: "))   

            #PRINTS CARDS IN DECK
            i = 0
            clear()
            for card in owner.filip.decks[inpDeck - 1].cards:
                print(f"{i + 1}. {card.wordOne} {card.wordTwo}")

                i+=1
            print(      "_________________________________________________________________________")
            inpCard = int(input("Type number of card to remove (type 'DELETE ALL' to delete entire deck): "))

            removed = owner.filip.decks[inpDeck - 1].cards.pop(inpCard - 1)
            print("Removed card: " + removed.wordOne + " / " + removed.wordTwo)

            writeToFile.writeToFile(owner.filip.decks[inpDeck - 1])
            hold = input()

        case 4:
            break
