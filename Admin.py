import tkinter as tk
from tkinter import messagebox
import csv  # For CSV backup (you may need to install the 'csv' module)

class AdminWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Panel")

        # Labels
        tk.Label(master, text="Golf Cart Plate Number:").grid(row=0, column=0, sticky="e")
        tk.Label(master, text="College:").grid(row=1, column=0, sticky="e")

        # Entry widgets
        self.plate_number_entry = tk.Entry(master)
        self.college_entry = tk.Entry(master)

        # Grid layout for entry widgets
        self.plate_number_entry.grid(row=0, column=1)
        self.college_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(master, text="Create", command=self.create_record).grid(row=2, column=0, columnspan=2)
        tk.Button(master, text="Logout", command=self.logout).grid(row=3, column=0, columnspan=2)
        tk.Button(master, text="Backup", command=self.backup).grid(row=4, column=0, columnspan=2)

    def create_record(self):
        # Dummy: Send information to the central database (replace with actual database interaction)
        plate_number = self.plate_number_entry.get()
        college = self.college_entry.get()

        # Dummy: Print information (replace with actual database insertion)
        print(f"Record Created:\nPlate Number: {plate_number}\nCollege: {college}")

    def logout(self):
        # Add logic to go back to the sign-up window or login window
        pass

    def backup(self):
        # Dummy: Backup information to a CSV file (replace with actual database backup)
        data_to_backup = [["Plate Number", "College"],
                          [self.plate_number_entry.get(), self.college_entry.get()]]

        with open('backup.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data_to_backup)

        messagebox.showinfo("Backup", "Backup successful. Data saved to 'backup.csv'.")

# Create the main application window
root = tk.Tk()
app = AdminWindow(root)

# Run the application
root.mainloop()
