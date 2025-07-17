#THIS IS THE MAIN PROGRAM INDEX
import addCard
import deckClass
import readFile

readFile.readFile(deckClass.deck)


print("Welcome to FlashCards!")
print("Please choose an options below")

print("1.Play deck")
print("2.Add Card to deck")




selection = int(input())
match selection:
    case 1:
        for card in deckClass.deck.cards:
            print(card.wordOne + " " + card.wordTwo)

    case 2:
        print("Write first one")
        wordOne = input()
        print("Write second one")
        wordTwo = input()

        addCard.addCard(deckClass.deck.cards, wordOne, wordTwo)
