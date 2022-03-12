import sqlite3

conn = sqlite3.connect('homework2_2.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

class Base:
    def method(self, *args):
        params = [*args]
        print(params)
        if len(params) == 1:
            cursor.execute("""INSERT INTO tab_1(col_1) VALUES(3)""")
        elif len(params) == 2:
            if isinstance(params[1], int):
                cursor.execute("""DELETE FROM tab_1 WHERE id=1""")
        elif params[0] == None and params[1] == None and isinstance(params[2], int):
            cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
        conn.commit()

base = Base()
base.method(None, None, 100)
print(cursor.execute("""SELECT * FROM tab_1""").fetchall())

