import sqlite3

sqliteConnection = sqlite3.connect('first_practice.db')
print("Database connection established")

cursor = sqliteConnection.cursor()
print("Database initalization")

sql_read_query = "SELECT * FROM STUDENTS"
cursor.execute(sql_read_query)
print(cursor.fetchall())

sqliteConnection.close()
