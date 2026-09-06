#THIS IS THE MAIN PROGRAM INDEX
import modules.addCard as addCard
import modules.owner as owner
import modules.readFile as readFile
import modules.play as play
import modules.deckClass as deckClass
import modules.errorHandling as errorHandling
import modules.formatting as formatting
import sqlite3
from colorama import Fore
import os

clear = lambda: os.system('clear')
#Loads in decks from database
readFile.readFile(owner.owner1)

#Database connection
connection = sqlite3.connect("decks.db")
cursor = connection.cursor()

#MAIN GAME LOOP
while True:
    
    clear()

    print(Fore.WHITE + "Welcome to FlashCards!\n")
    print("Please choose an option below")

    print("1.Play deck")
    print("2.Add Card to deck")
    print("3.Remove cards")
    print("4.Exit programme")
    print("________________")

    
    selection = (input("Select option: "))
    try:
        selection = int(selection)
    except:
        #THE CODE COULDNT PARSE TO INT AND THUS RETURNS TO MAIN LOOP
        clear()
   
    match selection:
        case 1: #PLAY GAME
            clear()

            #PRINTS DECKS
            print("Decks: \n")
            for i in range(0, len(owner.owner1.decks)):
                print(f"{i + 1}. {owner.decks[i].name} {owner.decks[i].id}")

            print(          "_____________________________")

            #CHOOSE AND PLAYS A DECK
            inp = int(input("Type number of deck to play: "))           
            play.play(owner.owner1.decks[inp - 1]) 

            hold = input("Press enter to continue.. ")
        case 2: #ADD CARD
            clear()

            print("Please choose an option below")

            print("1. Add new deck (CURRENTLY BEING DEVELOPED)")
            print("2. Add cards to existing deck")          
            print("_____________________________")

            selection = input("Select Option: ")
            selection = errorHandling.trySelection(selection)
            match selection:
                case 1:
                    clear()
                    #INPUTS NAME 
                    inpName = input("Please enter name of new deck: ")

                    clear()
                    #INPUTS LANGUAGE
                    inpLang = input("Please enter language to learn in deck")

                    #WRITE TO DATABASE
                    query = cursor.execute(f"INSERT INTO decks VALUES (NULL, {owner.owner1.id}, '{inpName}', '{inpLang}', 1500)")
                    newID = cursor.lastrowid
                    connection.commit()
                    

                    #ADD TO LOCAL LIST OF DECKS
                    newDeck = deckClass.Deck(newID, tempDeck[0], inpName, [])
                    owner.decks.append(newDeck)

                case 2: #ADD CARD TO EXISTING DECK
                    clear()
                    formatting.printDecks(owner.owner1.decks)
                    inpDeck = int(input("Enter number of deck to modify: "))

                    #ENTER VALUES OF NEW CARD
                    while(True):
                        clear()
                        print("Write first word")
                        wordOne = input()
                        clear()
                        print("Write second word")
                        wordTwo = input()
                        #ADD NEW CARD TO SELECTED DECK
                        addCard.addCard(owner.owner1.decks[inpDeck-1], wordOne, wordTwo)

                        #ADD TO DATABASE
                        cursor.execute(f"INSERT INTO cards VALUES (NULL, {owner.owner1.decks[inpDeck-1].id}, '{wordOne}', '{wordTwo}')")
                        connection.commit()
                        #USER CHOOSES TO ADD ANOTHER CARD OR GO BACK TO MAIN MENU
                        clear()
                        print("1. Add another card")
                        print("2. Exit")
                        selection = input("Select option: ")    
                        errorHandling.trySelection(selection)  
                        match selection:
                            case 1:
                                clear()
                            case 2:
                                break


        case 3: #REMOVE CARD/DECK        
            clear()
            #PRINTS DECKS
            print("Decks:")
            print("")
            formatting.printDecks(owner.filip.decks)   
            print("_____________________________")

            #USER SELECTS DECK
            inpDeck = int(input("Type number of deck to modify: "))   

            #PRINTS CARDS IN DECK       
            clear()
            formatting.printCards(owner.filip.decks[inpDeck - 1].cards)
            print("_________________________________________________________________________")

            #USER SELECTS CARD
            inpCard = input("Type number of card to remove (type 'DELETE ALL' to delete entire deck): ")

            #USER SELECTED TO DELETE ENTIRE DECK
            if inpCard == "DELETE ALL":
                removed = owner.filip.decks.pop(inpDeck -1)
                print(f"Removed deck {removed.name}")
                os.remove(f"./decks/{removed.name}.txt")
            #USER SELECTED TO REMOVED SPECIFIC CARD
            else:
                inpCard = int(inpCard)
                removed = owner.filip.decks[inpDeck - 1].cards.pop(inpCard - 1)
                print("Removed card: " + removed.wordOne + " / " + removed.wordTwo)
            
            hold = input("Press enter to continue.. ")
        case 4:
            clear()
            print("Goodbye and thanks for playing")
            break
