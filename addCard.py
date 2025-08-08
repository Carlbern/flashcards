import cardClass
import deckClass
import appendFile




def addCard(deck, wordOne, wordTwo):
    tempCard = cardClass.Card(wordOne, wordTwo)
    deck.cards.append(tempCard)
    appendFile.appendFile(deck, wordOne, wordTwo)

def addDeck(owner, name):
    tempCards = []
    tempDeck = deckClass.Deck(name, tempCards)

    owner.decks.append(tempDeck)




