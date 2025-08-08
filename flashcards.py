#THIS IS THE MAIN PROGRAM INDEX
import modules.addCard as addCard
import modules.writeToFile as writeToFile
import modules.owner as owner
import modules.readFile as readFile
import modules.play as play
from colorama import Fore
import os
clear = lambda: os.system('clear')
readFile.readFile(owner.filip)

while True:
    clear()

    print(Fore.WHITE + "Welcome to FlashCards!\n")
    print("Please choose an option below")

    print("1.Play deck")
    print("2.Add Card to deck")
    print("3.Remove cards")
    print("4.Exit programme")
    print("________________")

    selection = int(input("Select option: "))
    match selection:
        case 1: #PLAY GAME
            clear()

            #PRINTS DECKS
            print("Decks: \n")
            for i in range(0, len(owner.filip.decks)):
                print(f"{i + 1}. {owner.decks[i].name}")

            print(          "_____________________________")

            #CHOOSE AND PLAYS A DECK
            inp = int(input("Type number of deck to play: "))           
            play.play(owner.filip.decks[inp - 1]) 
 
            hold = input("Press enter to continue.. ")
        case 2: #ADD CARD
            clear()

            print("Please choose an option below")

            print("1. Add new deck")
            print("2. Add cards to existing deck")          
            print("_____________________________")

            selection = int(input("Select Option: "))

            match selection:
                case 1:
                    break

                case 2: #ADD CARD TO EXISTING DECK
                    clear()
                    #PRINTS ALL DECKS
                    i = 1
                    for deck in owner.filip.decks:
                        print(f"{i}. {deck.name}")
                        i+=1

                    inpDeck = int(input("Enter number of deck to modify: "))

                    clear()
                    print("Write first word")
                    wordOne = input()
                    clear()
                    print("Write second word")
                    wordTwo = input()

                    addCard.addCard(owner.filip.decks[inpDeck-1], wordOne, wordTwo)
                    writeToFile.writeToFile(owner.filip.decks[inpDeck - 1])
        case 3: #REMOVE CARD/DECK
            ##NEED TO ADD FEATURE TO REMOVE ENTIRE DECKS STILL
            
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
            inpCard = input("Type number of card to remove (type 'DELETE ALL' to delete entire deck): ")

            if inpCard == "DELETE ALL":
                removed = owner.filip.decks.pop(inpDeck -1)
                print(f"Removed deck {removed.name}")
                os.remove(f"./decks/{removed.name}.txt")
            else:
                inpCard = int(inpCard)
                removed = owner.filip.decks[inpDeck - 1].cards.pop(inpCard - 1)
                print("Removed card: " + removed.wordOne + " / " + removed.wordTwo)
                writeToFile.writeToFile(owner.filip.decks[inpDeck - 1])
            
            hold = input("Press enter to continue.. ")
        case 4:
            clear()
            print("Goodbye and thanks for playing")
            break
