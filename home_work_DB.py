import sqlite3


conn = sqlite3.connect('homework.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT col_text TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT col_int INTEGER)''')