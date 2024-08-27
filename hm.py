import sqlite3
with sqlite3.connect('users.db') as connection:
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL
    )''')
    cursor.execute('''INSERT INTO employees(name, salary)
        VALUES ('danya',0), ('tema', 3000),('eliza', 2000),
         ('ella',8000), ('alla',6000),('gulya',2000),
         ('ela',7000),('kolya', 700), ('dastan',300), ('akniet', 2000)''')
    cursor.execute('''SELECT * FROM employees''')
    for row in cursor.fetchall():
        print(row)