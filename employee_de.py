#1.create a database employee
#2.create menu: (add,list,delete,exit)
#3.add(take input of employee detail) then store employee detail in database
#4.list(list all records stored in database)

'''
import sqlite3

sqliteConnection = sqlite3.connect('first_practice.db')
print("Database connection established")

cursor = sqliteConnection.cursor()
print("Database initalization")

create_table_query = """
CREATE TABLE IF NOT EXISTS EMPLOYEE(id integer primary key AUTOINCREMENT,
              name text,
              age integer,
              address text, 
              department text, 
              salary real,
              email text,
              phone_number text,
              gender text
              )
"""
cursor.execute(create_table_query)
print("Table created successfully")

try:
    add_column="""
    ALTER TABLE EMPLOYEE ADD COLUMN email text
    """
    cursor.execute(add_column)
except sqlite3.OperationalError:
    pass

try:
    add_column="""
    ALTER TABLE EMPLOYEE ADD COLUMN phone_number text
    """
    cursor.execute(add_column)
except sqlite3.OperationalError:
    pass

try:
    add_column="""
    ALTER TABLE EMPLOYEE ADD COLUMN gender text
    """
    cursor.execute(add_column)
except sqlite3.OperationalError:
    pass

def add_employee():
    name = input("Enter employee name:")
    age = input("Enter employee age:")
    address = input("Enter employee address:")
    department = input("Enter employee department:")
    salary = input("Enter employee salary:")
    email = input("Enter employee email:")
    phone_number = input("Enter employee contact number:")
    gender = input("Enter employee gender:")
    insert_table_query = """
    INSERT INTO EMPLOYEE(name, age, address, department, salary, email, phone_number, gender) VALUES (?, ?, ?, ?, ?, ? , ?, ?)
    """
    cursor.execute(insert_table_query,(name, age, address, department, salary, email, phone_number, gender))
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

def update():
    update_query ="""
    UPDATE EMPLOYEE set name=?, age=?, address=?, department=?, email=?, phone_number=?, gender=?) where id=?
    """
    cursor.execute(update_query,(name, age, address, department, salary, email, phone_number, gender, id))
    sqliteConnection.commit()
'''
'''
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
'''
import sqlite3

class Database:
    def __init__(self, first_practice):
        self.conn = sqlite3.connect(first_practice)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS EMPLOYEE(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            age INTEGER,
            address TEXT, 
            department TEXT, 
            salary REAL, 
            email TEXT, 
            phone_number TEXT,
            gender TEXT
        )
        """)
        self.conn.commit()

    def insert(self, name, age, address, department, salary, email, phone_number, gender):
        self.cursor.execute("INSERT INTO EMPLOYEE (name, age, address, department, salary, email, phone_number, gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (name, age, address, department, salary, email, phone_number, gender))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM EMPLOYEE")
        rows = self.cursor.fetchall()
        return rows

    def update(self, id, name, age, address, department, salary, email, phone_number, gender):
        self.cursor.execute("UPDATE EMPLOYEE SET name=?, age=?, address=?, department=?, salary=?, email=?, phone_number=?, gender=? WHERE id=?",
                            (name, age, address, department, salary, email, phone_number, gender, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM EMPLOYEE WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

