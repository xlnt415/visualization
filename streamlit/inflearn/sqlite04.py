import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

delete_query = '''
    DELETE FROM users WHERE id = ?
'''

data = (1,)
cursor.execute(delete_query, data)

conn.commit()
conn.close()