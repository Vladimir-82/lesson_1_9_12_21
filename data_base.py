import sqlite3

conn = sqlite3.connect('name.db')

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS genre(id INTEGER PRIMARY KEY AUTOINCREMENT, name_genre VARCHAR(30))""")
cursor.execute("""INSERT INTO genre (name_genre) VALUES (book_1)""")