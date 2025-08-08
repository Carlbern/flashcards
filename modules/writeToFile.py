def writeToFile(deck):
    with open("decks/"+deck.name+".txt", "w") as f:        
        for card in deck.cards:    
            f.write(card.wordOne + "|" + card.wordTwo + "\n")
