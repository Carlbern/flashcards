import deckClass

class Owner:
     def __init__(self, name, decks):
        self.name = name
        self.decks = decks

franska = deckClass.deck
decks = [deckClass.deck, deckClass.deck2]
filip = Owner("Filip", decks)
