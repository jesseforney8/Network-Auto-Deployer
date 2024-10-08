import tkinter as tk
from tkinter import ttk, filedialog
import sqlite3
from db_startup import try_create_db
import os
import shutil



root = tk.Tk()
root.title("Network-Auto-Deployer (NAD)")
#root.iconbitmap()
root.geometry("800x500")

#Creates db if first boot

try_create_db()

#functions

def search_db():
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    devices = c.execute("SELECT *, oid FROM devices")
    return devices

def upload_config():

    #get filepath
    filepath = filedialog.askopenfilename(title="Select config", filetypes=[("txt files", "*.txt")])

    #gets just file name
    if filepath:
         filename = os.path.basename(filepath)

    #copy file to new directory
    shutil.copy(filepath, f"configs/{filename}")
      



#Submit form



#creates tabs
notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook, padx=20)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)

notebook.add(tab1, text='Configs')
notebook.add(tab2, text='Devices')
notebook.add(tab3, text='Push')

notebook.grid()


#tab1
add_new_device_label = tk.Label(tab1, text="Upload Configuration File (.txt)", pady=10).grid(row=1, column=0)
upload_btn = tk.Button(tab1, text="Upload", command=upload_config).grid(row=2, column=0)
delete_config_btn = tk.Button(tab1, text="Delete").grid(row=3, column=0)

my_ctree = ttk.Treeview(tab1)

my_ctree["columns"] = ("name", "date_uploaded")

my_ctree.column("#0", width=0, stretch="no")
my_ctree.column("name", width=120, minwidth=25, anchor="w")
my_ctree.column("date_uploaded", width=120, minwidth=25, anchor="w")

my_ctree.heading("#0", text="", anchor="w")
my_ctree.heading("name", text="Config Name", anchor="w")
my_ctree.heading("date_uploaded", text="Date Uploaded", anchor="w")

my_ctree.grid(row=0, column=0)

#tab2

#Treeview for devices

my_tree = ttk.Treeview(tab2)

my_tree["columns"] = ("name", "ip", "username")

my_tree.column("#0", width=0, stretch="no")
my_tree.column("name", anchor="w", minwidth=25,  width=120)
my_tree.column("ip", anchor="w", minwidth=25,  width=120)
my_tree.column("username", anchor="w", minwidth=25,  width=120 )

my_tree.heading("#0", text="", anchor="w")
my_tree.heading("name", text="Name", anchor="w")
my_tree.heading("ip", text="IP", anchor="w")
my_tree.heading("username", text="Username", anchor="w")

for d in search_db():
        my_tree.insert(parent="", index="end", iid=d[3], text="", values=(d[0], d[1], d[2] ))


my_tree.grid()


#buttons



push_btn = tk.Button(tab2, text="Push").grid()
del_btn = tk.Button(tab2, text="Delete").grid()














root.mainloop()