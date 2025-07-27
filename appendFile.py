import deckClass

def appendFile(wordOne, wordTwo):
    with open("decks/"+deckClass.deck.name+".txt", "a") as f:        
            f.write(wordOne + "|" + wordTwo + "\n")
