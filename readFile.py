import cardClass
import deckClass
import os
import owner


def readFile(owner):

    
    path = "./decks"
    dir_list = os.listdir(path)

    for i in range(0, len(dir_list)):
        
        tempCards = []
        
        file = open(f"{path}/{dir_list[i]}", "r")
        for line in file:
            line = line.strip() #Removes trailing whitespaces and newlines
            lineWords = line.split("|")
            tempCard = cardClass.Card(lineWords[0],lineWords[1])

            tempCards.append(tempCard)
            print("Added ", tempCard)

        deckName = dir_list[i].removesuffix(".txt")
        deck = deckClass.Deck(deckName, tempCards)

        owner.decks.append(deck)
        print("Added deck: ", deck.name, "To ", owner.name)
        file.close()


