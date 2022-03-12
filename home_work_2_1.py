import sqlite3
from random import randint, choice

conn = sqlite3.connect('homework2_1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')


for _ in range(3):
    x, y = randint(1, 9), randint(1, 9)
    cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES(?, ?)""", (x, y))
conn.commit()

k = cursor.execute("""SELECT id FROM tab_1""").fetchall()
print(k)
ch = choice(k)

cursor.execute("""SELECT col_1, col_2 FROM tab_1 WHERE id=?""", (ch))

select = cursor.fetchall()
print(select)

for i in select:
    if not i[0] % 2 and not i[1] % 2:
        cursor.execute("""DELETE FROM tab_1 WHERE id=?""", (ch))
        conn.commit()
    else:
        cursor.execute('''UPDATE tab_1 SET col_1=2, col_2=2 WHERE id=?''', (ch))
        conn.commit()

cursor.execute("""SELECT * FROM tab_1""")
result = cursor.fetchall()
print(result)