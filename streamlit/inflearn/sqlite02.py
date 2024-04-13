import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

insert_query = '''
  INSERT INTO users (name, email)
  VALUES (?, ?)
'''

data = ('hong', 'hong@a.com')

cursor.execute(insert_query, data)

conn.commit()
conn.close()