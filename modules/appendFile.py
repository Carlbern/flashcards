def appendFile(deck, wordOne, wordTwo):
    with open("decks/"+deck.name+".txt", "a") as f:        
            f.write(wordOne + "|" + wordTwo + "\n")
