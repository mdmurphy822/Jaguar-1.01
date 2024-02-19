# BKTGUI2
# Okay so this one got a bit complicated as it turned into a lesson
# on how to create a GUI with Python. This is technically my first
# GUI program, and I have some cool ideas I want to implement with
# the tkinter module. For now, the focus remains on CSV and data
# analysis, since the end goal is managing mindblowingly large datasets.
# https://docs.python.org/3/library/tkinter.html#

import csv
import tkinter as tk
from tkinter import Label, Entry, Button
from tkinter import END

# Function to save input values to a CSV file
def save_to_csv():
    name = name_entry.get()
    bktid = bktid_entry.get()
    bktmass = bktmass_entry.get()
    with open('today.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, bktid, bktmass])
    print("Saved!")
    name_entry.delete(0, END)
    bktid_entry.delete(0, END)
    bktmass_entry.delete(0, END)

# Create the main application window
root = tk.Tk()
root.title("BKTS")

# Create labels and input fields
name_label = Label(root, text="USERID:")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

bktid_label = Label(root, text="BKTID:")
bktid_label.grid(row=1, column=0, padx=10, pady=5)

bktid_entry = Entry(root)
bktid_entry.grid(row=1, column=1, padx=10, pady=5)

bktmass_label = Label(root, text="WEIGHT:")
bktmass_label.grid(row=2, column=0, padx=10, pady=5)

bktmass_entry = Entry(root)  # Fix: Replace Label with Entry
bktmass_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = Button(root, text="Submit", command=save_to_csv)  # Fix: Define the get_input function
submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
