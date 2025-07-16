import cardClass
import deckClass
import writeToFile

print("Write first one")
wordOne = input()
print("Write second one")
wordTwo = input()


def addCard(cards, wordOne, wordTwo):
    tempCard = cardClass.Card(wordOne, wordTwo)
    cards.append(tempCard)

addCard(deckClass.deck.cards, wordOne, wordTwo)



for card in deckClass.deck.cards:
    print(card.wordOne + " | " + card.wordTwo)


writeToFile.writeToFile(deckClass.deck)
