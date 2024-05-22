
import sqlite3

sqliteConnection = sqlite3.connect('first_practice.db')
print("Database connection established")

cursor = sqliteConnection.cursor()
print("Database initalization")

create_table_query = """
CREATE TABLE IF NOT EXITS STUDENTS(id integer primary key AUTOINCREMENT, name text, age integer,address text)
"""
cursor.execute(create_table_query)