import modules.deckClass as deckClass
import modules.cardClass as cardClass
import sqlite3


def readFile(owner):
    

    connection = sqlite3.connect("decks.db")
    cursor = connection.cursor()

    query_decks = cursor.execute(f"SELECT * FROM decks WHERE owner_id = '{owner.id}'")
    decks = query_decks.fetchall() 

    print("zqdqzd")
    for i in range(0, len(decks)):
        query_cards = cursor.execute(f"SELECT * FROM cards WHERE deck_id = '{decks[i][0]}'")
        cards = query_cards.fetchall()
      

        tempCards = []
        for j in range(0, len(cards)):
           
            tempCard = cardClass.Card(cards[j][2], cards[j][3])
            tempCards.append(tempCard)

        deck = deckClass.Deck(decks[i][0],decks[i][2], tempCards)
        owner.decks.append(deck)

