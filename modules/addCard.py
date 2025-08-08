import modules.cardClass as cardClass
import modules.deckClass as deckClass
import modules.appendFile as appendFile

def addCard(deck, wordOne, wordTwo):
    tempCard = cardClass.Card(wordOne, wordTwo)
    deck.cards.append(tempCard)
    appendFile.appendFile(deck, wordOne, wordTwo)

def addDeck(owner, name):
    tempCards = []
    tempDeck = deckClass.Deck(name, tempCards)

    owner.decks.append(tempDeck)



