import random
import sqlite3


conn = sqlite3.connect('task2.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')

x = random.randint(1, 9)
y = random.randint(1, 9)

cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES(?, ?)""", (x, y))

conn.commit()
cursor.execute("""SELECT * FROM tab_1""")

k = cursor.fetchall()
print(k)
s = 0

for i in k:
    for j in i:
        print(j)
        s += j

print('SUM', s)

sr = (s/(len(k) * 2))
print(sr)
if sr > len(k):
    cursor.execute("""DELETE FROM tab_1 WHERE id=4""")
conn.commit()
cursor.execute("""SELECT * FROM tab_1""")
k = cursor.fetchall()
print(k)


t = 3
cursor.execute("""UPDATE tab_1 SET col_1='world' WHERE id=?""", (t,))
conn.commit()
k = cursor.fetchall()
print(k)




