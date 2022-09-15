import sqlite3

connection = sqlite3.connect('data_base/example.sqlite3')

with open('best_selling.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
