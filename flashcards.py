#THIS IS THE MAIN PROGRAM INDEX
import addCard
import deckClass
import readFile
import os
clear = lambda: os.system('clear')
readFile.readFile(deckClass.deck)



while True:
    clear()

    print("Welcome to FlashCards!\n")
    print("Please choose an options below")

    print("1.Play deck")
    print("2.Add Card to deck")
    print("3.Exit programme")
    print("________________")






    selection = int(input())
    match selection:
        case 1:
            clear()
            for card in deckClass.deck.cards:
                print(card.wordOne + " " + card.wordTwo)

            
            hold = input()
        case 2:
            clear()
            print("Write first word")
            wordOne = input()
            clear()
            print("Write second word")
            wordTwo = input()

            addCard.addCard(deckClass.deck.cards, wordOne, wordTwo)
        case 3:
            break
