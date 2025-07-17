import deckClass
import cardClass


def readFile(deck):
    file = open("test.txt", "r")

    for line in file:
        lineWords = line.split()
        print(line.split()[0])
        tempCard = cardClass.Card(lineWords[0], lineWords[1])
        #tempCard.wordOne = lineWords[0]
        #tempCard.wordTwo = lineWords[1]

        deck.cards.append(tempCard)

    file.close()

