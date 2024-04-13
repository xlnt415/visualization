import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

creat_table = '''
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
  )
'''

cursor.execute(creat_table)

conn.commit()
conn.close()


