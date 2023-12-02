import tkinter as tk
from tkinter import messagebox
import csv  # For CSV backup (you may need to install the 'csv' module)
import sqlite3
import Login
#pop up
class AdminWindow:
    def __init__(self, main):
        self.main = main
        self.main.title("Admin Panel")

        self.frame = tk.Frame(self.main, padx=10, pady=10)
        self.frame.grid(row=0, column=0, sticky="nsew")
        # Labels
        tk.Label(self.frame, text="Golf Cart Plate Number:").grid(row=0, column=0, sticky="e")
        tk.Label(self.frame, text="College:").grid(row=1, column=0, sticky="e")

        self.plate_number_entry = tk.Entry(self.frame)
        self.selected_college = tk.StringVar()
        colleges = ["College of Computer and Information Sciences", "College of Science", "College of Engineering",
                    "College of Business Administration"]
        self.college_menu = tk.OptionMenu(self.frame, self.selected_college, *colleges)

        # Grid layout for entry widgets
        self.plate_number_entry.grid(row=0, column=1, padx=5, pady=5)
        self.college_menu.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.frame, text="Create", command=self.create_record).grid(row=2, column=0, columnspan=2, pady=7)
        tk.Button(self.frame, text="Logout", command=self.logout).grid(row=3, column=0, columnspan=2, pady=7)
        tk.Button(self.frame, text="Backup", command=self.backup).grid(row=4, column=0, columnspan=2, pady=7)

        # Column and Row Weights to allow resizing
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)

    def create_record(self):
        # Dummy: Send information to the central database (replace with actual database interaction)     (((DONE)))

        conn = sqlite3.connect("GolfDataBase.db")
        try:
            insertion = "INSERT INTO CartData (PlateNumber, College) VALUES (?, ?)"
            insertionValues = (self.plate_number_entry.get(), self.selected_college.get())
            conn.execute(insertion, insertionValues)
            conn.commit()
            messagebox.showinfo("Created", "Cart has been added successfully.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Plate Number Already Exists!!")
        conn.close()

    def logout(self):
        self.frame.destroy()
        Login.LoginWindow(self.main)

    def backup(self):
        data_to_backup = [["Plate Number", "College"],
                          [self.plate_number_entry.get(), self.selected_college.get()]]

        with open('backup.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data_to_backup)

        messagebox.showinfo("Backup", "Backup successful. Data saved to 'backup.csv'.")
