import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("400x300")

#adding label
label = tk.Label(root, text="Hello Python")
label.pack()

#button click function 
def on_summit():
    print("Button Clicked!")

#adding button 
button = tk.Button(root, text="Summit", command=on_summit)
button.pack()

#adding Input Entry
entry = tk.Entry(root)
entry.pack()

#adding Text area 
text = tk.Text(root, height = 5, width =40) 
text.pack()

frame = tk.Frame(root, bg="black")

check = tk.IntVar()
check1 = tk.IntVar()
checkbutton = tk.Checkbutton(frame, text ="check me", variable=check)
checkbutton1 = tk.Checkbutton(frame, text ="check me too", variable=check1)
checkbutton.pack()
checkbutton1.pack()

radio_var = tk.StringVar()
radiobutton1 = tk.Radiobutton(frame, text ="Female", variable= radio_var, value = "F") 
radiobutton2 = tk.Radiobutton(frame, text ="Male", variable= radio_var, value = "M")
radiobutton1.pack()
radiobutton2.pack()

frame.pack()

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

tree = ttk.Treeview(root)
tree["columns"]=("Name","Age")
tree.column("#0", width = 150)
tree.column("#1", width = 150)


root.mainloop()
