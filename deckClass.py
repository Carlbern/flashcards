import cardClass
#Define class Deck
class Deck:
    def __init__(self, name, card):
        self.name = name
        self.cards = cards
#Creates cards and deck
cards = cardClass.cards
deck = Deck("test", cards)

print("Write first one")
wordOne = input()
print("Write second one")
wordTwo = input()

cardClass.addCard(deck.cards, wordOne, wordTwo)

for card in deck.cards:
    print(card.wordOne + " | " + card.wordTwo)
