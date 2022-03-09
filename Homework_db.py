import sqlite3

data_list = [3, 6, 'spam', 8, 'eags', 9, 'python']

conn = sqlite3.connect('homeworkDB.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

for element in data_list:
    if isinstance(element, str):
        cursor.execute("""INSERT INTO tab_1(col_1) VALUES(?)""", (element,))
        cursor.execute("""INSERT INTO tab_2(col_1) VALUES(?)""", (len(element), ))

    if isinstance(element, int):
        if not element % 2:
            cursor.execute("""INSERT INTO tab_2(col_1) VALUES(?)""", (element, ))
        else:
            cursor.execute("""INSERT INTO tab_1(col_1) VALUES(?)""", ('Нечетное',))
    conn.commit()

if cursor.execute("""SELECT COUNT(col_1) FROM tab_2""").fetchall()[0][0] > 5:
    cursor.execute("""DELETE FROM tab_1 WHERE id=1""")
else:
    cursor.execute("""UPDATE tab_1 SET col_1='Hello' WHERE id=1""")

conn.commit()