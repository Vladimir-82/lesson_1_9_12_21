import sqlite3

conn = sqlite3.connect('homework2_2.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

class Base:
    def method(self, first=None, second=None, third=None):
        if first == None and second == None and third == None:
            cursor.execute("""INSERT INTO tab_1(col_1) VALUES(3)""")
        elif first != None and second != None and third == None:
            if isinstance(second, int):
                cursor.execute("""DELETE FROM tab_1 WHERE id=1""")
        elif first != None and second != None and isinstance(third, int):
            cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
    conn.commit()

base = Base(34)
print(cursor.execute("""SELECT * FROM tab_1""").fetchall())

