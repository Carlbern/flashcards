def printDecks(decks):
    for i in range(0, len(decks)):
        print(f"{i + 1}. {decks[i].name}")

def printCards(cards):
    for i in range(0, len(cards)):
        print(f"{i + 1}. {cards[i].wordOne} {cards[i].wordTwo}")

def printCardBorder(word):
    asterisks = ""
    i = 0
    while i < len(word) + 6:
        if i == 0 or i == (len(word) + 5):
            asterisks+=" "
        else:
            asterisks+="*"
        i+=1
    return asterisks