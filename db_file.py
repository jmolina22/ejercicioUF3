import sqlite3
 
db_file = 'database.db'
with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
print('Automatically closed the connection!')