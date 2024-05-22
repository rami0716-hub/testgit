import sqlite3

sqliteConnection = sqlite3.connect('first_practice.db')
print("Database connection established")

cursor = sqliteConnection.cursor()
print("Database initalization")

insert_table_query = """
INSERT INTO STUDENTS(name, age, address) VALUES ("Shyam", 21, "Patan")
"""
cursor.execute(insert_table_query)

insert_table_query = """
INSERT INTO STUDENTS(name, age, address) VALUES ("Ram", 22, "Bhaktapur")
"""
cursor.execute(insert_table_query)

insert_table_query = """
INSERT INTO STUDENTS(name, age, address) VALUES ("Hari", 23, "Kavre")
"""
cursor.execute(insert_table_query)

sqliteConnection.commit()

sqliteConnection.close()