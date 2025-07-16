class Card:
    def __init__(self, wordOne, wordTwo):
        self.wordOne = wordOne
        self.wordTwo = wordTwo


def addCard(cards, wordOne, wordTwo):
    tempCard = Card(wordOne, wordTwo)
    cards.append(tempCard)
    

cards = []

cards.append(Card("Bonjour","Hej"))
cards.append(Card("Au revoir","Hej Då"))





