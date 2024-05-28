import tkinter as tk
from tkinter import ttk
from employee_de import Database 

employee_de = Database("first_practice.db")
root = tk.Tk()
root.title("Employees Details")
#root.configure(bg='lightgray')
root.geometry("1100x900")

name = tk.StringVar()
age = tk.StringVar()
address = tk.StringVar()
department = tk.StringVar()
salary = tk.StringVar() 
email = tk.StringVar()
phone_number = tk.StringVar()
gender = tk.StringVar()


frame = tk.Frame(root, bg="grey")
frame.pack()
title = tk.Label(frame, text="Employees Data", font=("Times roman",18,"bold"), bg="grey")
title.grid()

label_Name= tk.Label(frame, text="Name", font=("Times roman",12), bg = "grey")
label_Name.grid(row=1, column=0, padx=10, pady=10)
text_Name = tk.Entry(frame, textvariable=name, font=("Times roman",12),width =20)
text_Name.grid(row=1, column=1, padx=10, pady=10)

label_Age= tk.Label(frame, text="Age", font=("Times roman",12), bg = "grey")
label_Age.grid(row=1, column=2, padx=10, pady=10)
text_Age = tk.Entry(frame, textvariable=age, font=("Times roman",12),width =20)
text_Age.grid(row=1, column=3, padx=10, pady=10)

label_Address= tk.Label(frame, text="Address", font=("Times roman",12), bg = "grey")
label_Address.grid(row=2, column=0, padx=10, pady=10)
text_Address = tk.Entry(frame, textvariable=address, font=("Times roman",12), width =20)
text_Address.grid(row=2, column=1, padx=10, pady=10)

label_Department= tk.Label(frame, text="Department", font=("Times roman",12), bg = "grey")
label_Department.grid(row=2, column=2, padx=10, pady=10)
text_Department = tk.Entry(frame, textvariable=department, font=("Times roman",12), width =20)
text_Department.grid(row=2, column=3, padx=10, pady=10)

label_Salary= tk.Label(frame, text="Salary", font=("Times roman",12), bg = "grey")
label_Salary.grid(row=3, column=0, padx=10, pady=10)
text_Salary = tk.Entry(frame, textvariable=salary, font=("Times roman",12), width =20)
text_Salary.grid(row=3, column=1, padx=10, pady=10)

label_Email= tk.Label(frame, text="Email", font=("Times roman",12), bg = "grey")
label_Email.grid(row=3, column=2, padx=10, pady=10)
text_Email = tk.Entry(frame, textvariable=email, font=("Times roman",12), width =20)
text_Email.grid(row=3, column=3, padx=10, pady=10)

label_Phone_number= tk.Label(frame, text="Phone_number", font=("Times roman",12), bg = "grey")
label_Phone_number.grid(row=4, column=0, padx=10, pady=10)
text_Phone_number = tk.Entry(frame, textvariable=phone_number, font=("Times roman",12), width =20)
text_Phone_number.grid(row=4, column=1, padx=10, pady=10)

label_Gender= tk.Label(frame, text="Gender", font=("Times roman",12), bg = "grey")
label_Gender.grid(row=5, column=0, padx=5, pady=5)
radio_var = tk.StringVar()
radiobutton1 = tk.Radiobutton(frame, text ="Female", font=("Times roman",12), bg = "grey", variable= radio_var, value = "F") 
radiobutton2 = tk.Radiobutton(frame, text ="Male", font=("Times roman",12), bg = "grey", variable= radio_var, value = "M")
radiobutton1.grid(row=5, column=1)
radiobutton2.grid(row=5, column=2)

def getData(event):
    selected_row = tree.focus()
    data = tree.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    address.set(row[3])
    department.set(row[4])
    salary.set(row[5])
    email.set(row[6])
    phone_number.set(row[7])
    gender.set(row[8])

def displayAll():
    tree.delete(*tree.get_children())
    for rows in employee_de.fetch_all():
        tree.insert("","end",values=rows)

def add_employee():
    if text_Name.get() == " " or text_Age.get() == " " or text_Address.get() == " " or \
        text_Department.get() == " " or text_Salary.get() == " " or text_Email.get() == " " or \
        text_Phone_number.get() == " " or radio_var.get() == " ":
        return 
    employee_de.insert(text_Name.get(), text_Age.get(), text_Address.get(),\
                        text_Department.get(), text_Salary.get(), text_Email.get(),\
                        text_Phone_number.get(), radio_var.get())
    clearAll()
    displayAll()

def update_employee():
    selected_item = tree.selection()[0]
    selected_id = tree.item(selected_item)['values'][0]
    if text_Name.get() == " " or text_Age.get() == " " or text_Address.get() == " " or \
        text_Department.get() == " " or text_Salary.get() == " " or text_Email.get() == " " or\
        text_Phone_number.get() == " " or radio_var.get() == " ":
        return 
    employee_de.update(selected_id, text_Name.get(), text_Age.get(), text_Address.get() \
                        ,text_Department.get(),text_Salary.get(), text_Email.get() \
                        ,text_Phone_number.get(), radio_var.get())
    clearAll()
    displayAll()

def delete_employee():
    selected_item = tree.selection()[0]
    selected_id = tree.item(selected_item)['values'][0]
    employee_de.delete(selected_id)
    clearAll()
    displayAll()


def clearAll():
    name.set(" ")
    age.set(" ")
    address.set(" ")
    department.set(" ")
    salary.set(" ") 
    email.set(" ")
    phone_number.set(" ")
    gender.set("")

button_frame = tk.Frame(frame, bg="grey")
button_frame.grid(row=1, column=4, rowspan=4, padx=10, pady=10, sticky="w")

buttonAdd = tk.Button(button_frame, command=add_employee, text="Add", font=("Times roman",12), width=10)
buttonAdd.grid(row=2, column=0)

buttonEdit = tk.Button(button_frame, command=update_employee, text="Edit", font=("Times roman",12), width=10)
buttonEdit.grid(row=3, column=0, pady= 10)

buttonDelete = tk.Button(button_frame, command=delete_employee, text="Delete", font=("Times roman",12), width=10)
buttonDelete.grid(row=4, column=0, pady=10)

buttonClear = tk.Button(button_frame, command=clearAll, text="Clear", font=("Times roman",12), width=10)
buttonClear.grid(row=5, column=0, pady=10)


tree = ttk.Treeview(root)
tree["columns"] = (1,2,3,4,5,6,7,8,9)
tree.column("0", width=100)
tree.column("1", width=100)
tree.column("2", width=100)
tree.column("3", width=100)
tree.column("4", width=100)
tree.column("5", width=100)
tree.column("6", width=100)
tree.column("7", width=110)
tree.column("8", width=100)
tree.column("9", width=100)
tree.heading("1", text="ID" )
tree.heading("2", text="Name")
tree.heading("3", text="Address")
tree.heading("4", text="Age")
tree.heading("5", text="Department")
tree.heading("6", text="salary")
tree.heading("7", text="Email")
tree.heading("8", text="Phone_number")
tree.heading("9", text="Gender")
tree.bind("<ButtonRelease-1>", getData)
tree.pack()

displayAll()
root.mainloop()
