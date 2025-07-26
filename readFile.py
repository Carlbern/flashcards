import deckClass
import cardClass


def readFile(deck):
    file = open("test.txt", "r")

    for line in file:
        line = line.strip() #Removes trailing whitespaces and newlines
        lineWords = line.split("|")
        tempCard = cardClass.Card(lineWords[0],lineWords[1])
        

        deck.cards.append(tempCard)

    file.close()

