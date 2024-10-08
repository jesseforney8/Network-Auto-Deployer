import tkinter as tk
from tkinter import ttk
import sqlite3
from db_startup import try_create_db


root = tk.Tk()
root.title("Network-Auto-Deployer (NAD)")
root.geometry("800x500")

#Creates db if first boot

try_create_db()

#functions

def search_db():
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    devices = c.execute("SELECT *, oid FROM devices")
    return devices


#Submit form

frame1 = tk.Frame(root, padx=20)

add_new_device_label = tk.Label(frame1, text="Add New Device")
add_new_device_label.grid(row=0, column=0)

name_label = tk.Label(frame1, text="Device Name")
name_label.grid(row=1, column=0)
name_input = tk.Entry(frame1, width=20)
name_input.grid(row=2, column=0)

ip_label = tk.Label(frame1, text="IP Adress")
ip_label.grid(row=3, column=0)
ip_input = tk.Entry(frame1, width=20)
ip_input.grid(row=4, column=0)

username_label = tk.Label(frame1, text="username")
username_label.grid(row=5, column=0)
username_input = tk.Entry(frame1, width=20)
username_input.grid(row=6, column=0)

password_label = tk.Label(frame1, text="password")
password_label.grid(row=7, column=0)
password_input = tk.Entry(frame1, width=20)
password_input.grid(row=8, column=0)

secret_label = tk.Label(frame1, text="secret")
secret_label.grid(row=9, column=0)
secret_input = tk.Entry(frame1, width=20)
secret_input.grid(row=10, column=0)

input_btn = tk.Button(frame1, text="Submit")
input_btn.grid(row=15, column=0)

frame1.grid(row=0, column=0)

#Treeview for devices

frame2 = tk.Frame(root, padx=100)

my_tree = ttk.Treeview(frame2)

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

frame2.grid(row=0, column=1)

#buttons

frame3 = tk.Frame(root)

push_btn = tk.Button(frame3, text="Push").grid()
del_btn = tk.Button(frame3, text="Delete").grid()







frame3.grid(row=1, column=1)











root.mainloop()