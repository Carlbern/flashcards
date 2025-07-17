def writeToFile(deck):
    with open(deck.name+".txt", "w") as f:        
        for card in deck.cards:    
            f.write(card.wordOne + " " + card.wordTwo + "\n")
