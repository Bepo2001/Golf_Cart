import tkinter as tk
from tkinter import messagebox
import csv  # For CSV backup (you may need to install the 'csv' module)
import sqlite3

class AdminWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Panel")

        # Labels
        tk.Label(master, text="Golf Cart Plate Number:").grid(row=0, column=0, sticky="e")
        tk.Label(master, text="College:").grid(row=1, column=0, sticky="e")

        self.plate_number_entry = tk.Entry(master)
        self.selected_college = tk.StringVar()
        colleges = ["College of Computer and Information Sciences", "College of Science", "College of Engineering",
                    "College of Business Administration"]
        self.college_menu = tk.OptionMenu(self.master, self.selected_college, *colleges)

        # Grid layout for entry widgets
        self.plate_number_entry.grid(row=0, column=1)
        self.college_menu.grid(row=1, column=1)

        # Buttons
        tk.Button(master, text="Create", command=self.create_record).grid(row=2, column=0, columnspan=2)
        tk.Button(master, text="Logout", command=self.logout).grid(row=3, column=0, columnspan=2)
        tk.Button(master, text="Backup", command=self.backup).grid(row=4, column=0, columnspan=2)

    def create_record(self):
        # Dummy: Send information to the central database (replace with actual database interaction)     (((DONE)))

        conn = sqlite3.connect("GolfDataBase.db")
        try:
            insertion = "INSERT INTO CartData (PlateNumber, College) VALUES (?, ?)"
            insertionValues = (self.plate_number_entry.get(), self.selected_college.get())
            conn.execute(insertion, insertionValues)
            conn.commit()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Plate Number Already Exists!!")
        conn.close()

    def logout(self):
        self.master.destroy()
        import Login
        Login.LoginWindow(self.master)

    def backup(self):
        data_to_backup = [["Plate Number", "College"],
                          [self.plate_number_entry.get(), self.selected_college.get()]]

        with open('backup.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data_to_backup)

        messagebox.showinfo("Backup", "Backup successful. Data saved to 'backup.csv'.")

# Create the main application window
root = tk.Tk()
app = AdminWindow(root)

# Run the application
root.mainloop()
