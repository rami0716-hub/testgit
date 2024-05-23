#1.create a database employee
#2.create menu: (add,list,delete,exit)
#3.add(take input of employee detail) then store employee detail in database
#4.list(list all records stored in database)


import sqlite3

sqliteConnection = sqlite3.connect('first_practice.db')
print("Database connection established")

cursor = sqliteConnection.cursor()
print("Database initalization")

create_table_query = """
CREATE TABLE IF NOT EXISTS EMPLOYEE(id integer primary key AUTOINCREMENT, name text, age integer,address text, department text, salary real)
"""
cursor.execute(create_table_query)
print("Table created successfully")

def add_employee():
    name = input("Enter employee name:")
    age = input("Enter employee age:")
    address = input("Enter employee address:")
    department = input("Enter employee department:")
    salary = input("Enter employee salary:")
    insert_table_query = """
    INSERT INTO EMPLOYEE(name, age, address, department, salary) VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(insert_table_query,(name, age, address, department, salary))
    sqliteConnection.commit()
    print("Details added to database")

def list_employee():
    sql_list_query = "SELECT * FROM EMPLOYEE"
    cursor.execute(sql_list_query)
    print(cursor.fetchall())

def delete_employee():
    emp_id = input("Enter employee id to delete:")
    sql_delete_query = "DELETE FROM EMPLOYEE WHERE id=?"
    cursor.execute(sql_delete_query,emp_id)
    sqliteConnection.commit()
    print("Deleted")
    

while True:
        print("Menu:")
        print("1.Add Employee")
        print("2.List Employee")
        print("3.Delete Employee")
        print("4.Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            add_employee()
        elif choice == '2':
            list_employee()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            print("Exit")
            break
        else:
            print("Error")

sqliteConnection.close()

