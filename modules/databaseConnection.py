import sqlite3

connection = sqlite3.connect("decks.db")

cursor = connection.cursor()

create_table_owners_query = """
    CREATE TABLE owners (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
               )
"""

create_table_decks_query = """
    CREATE TABLE decks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id INTEGER,
        name VARCHAR(255) NOT NULL,
        language VARCHAR(255) NOT NULL,
        elo FLOAT NOT NULL        

               )
"""

create_table_cards_query = """
    CREATE TABLE cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deck_id INTEGER,
        word_1 VARCHAR(255),
        word_2 VARCHAR(255)

               )
"""

""" cursor.execute("INSERT INTO owners VALUES (NULL, 'filip', 123)")
cursor.execute("INSERT INTO decks VALUES (NULL, 1, 'test2', 'svenska', 1600)") """
""" cursor.execute("INSERT INTO cards VALUES (NULL, 2, 'testitest', 'testitest')") """
cursor.execute("DELETE from decks WHERE id = '8'")
connection.commit()