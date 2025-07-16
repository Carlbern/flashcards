import cardClass
import deckClass
import writeToFile
import appendFile

print("Write first one")
wordOne = input()
print("Write second one")
wordTwo = input()


def addCard(cards, wordOne, wordTwo):
    tempCard = cardClass.Card(wordOne, wordTwo)
    cards.append(tempCard)

addCard(deckClass.deck.cards, wordOne, wordTwo)

appendFile.appendFile(wordOne, wordTwo)


for card in deckClass.deck.cards:
    print(card.wordOne + " | " + card.wordTwo)


