def appendFile(deck, card):
    with open(deck.name+".txt", "a") as f:        
            f.write(card.wordOne + "|" + card.wordTwo + "\n")
