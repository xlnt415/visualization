import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

select_query = '''
    SELECT * FROM users
'''

cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()