import cardClass
import deckClass
import appendFile




def addCard(cards, wordOne, wordTwo):
    tempCard = cardClass.Card(wordOne, wordTwo)
    cards.append(tempCard)
    appendFile.appendFile(wordOne, wordTwo)


for card in deckClass.deck.cards:
    print(card.wordOne + " | " + card.wordTwo)


