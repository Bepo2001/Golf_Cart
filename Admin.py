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

        self.frame = tk.Frame(self.main, bg="#add8e6")
        self.frame.grid()

        font = ("Helvetica", 14)
        welcome_font = ("Helvetica", 20, "bold")
        light_blue = "#add8e6"
        # Labels
        tk.Label(self.frame, text="   Cart Creation", font=welcome_font, bg=light_blue).grid(row=0, column=0, columnspan=3, pady=30, sticky="n")
        tk.Label(self.frame, text="Golf Cart Plate Number:", font=font, bg=light_blue).grid(row=2, column=0, sticky="e")
        tk.Label(self.frame, text="College:", font=font, bg=light_blue).grid(row=3, column=0, sticky="e")

        self.plate_number_entry = tk.Entry(self.frame, font=font)
        self.selected_college = tk.StringVar()
        colleges = ["College of Computer and Information Sciences", "College of Science", "College of Engineering",
                    "College of Business Administration"]
        self.college_menu = tk.OptionMenu(self.frame, self.selected_college, *colleges)

        # Grid layout for entry widgets
        self.plate_number_entry.grid(row=2, column=1, padx=5, pady=5)
        self.college_menu.grid(row=3, column=1, padx=5, pady=30, ipadx=50)

        # Buttons
        tk.Button(self.frame, text="Create", command=self.create_record, font=font).grid(row=4, column=1, sticky="w", pady=15)
        tk.Button(self.frame, text="Backup", command=self.backup, font=font).grid(row=5, column=1, sticky="w", pady=10)
        tk.Button(self.frame, text="Logout", command=self.logout, font=font).grid(row=6, column=1, sticky="w", pady=10)

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
        conn = sqlite3.connect("GolfDataBase.db")
        P = "SELECT PlateNumber FROM CartData"
        C = "SELECT College FROM CartData"

        Plates = conn.execute(P).fetchall()
        College = conn.execute(C).fetchall()
        pairedData = zip(Plates, College)
        data_to_backup = [["Plate Number", "College"]]

        with open('backup.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data_to_backup)

            csvwriter.writerows(pairedData)

        messagebox.showinfo("Backup", "Backup successful. Data saved to 'backup.csv'.")
