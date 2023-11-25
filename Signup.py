import tkinter as tk
from tkinter import messagebox
import re
import hashlib
import sqlite3

class SignUpWindow:
    def __init__(self, main):
        self.main = main
        self.frame = tk.Frame(self.main)
        self.frame.grid()


        tk.Label(self.frame, text="First Name:").grid(row=0, column=0, sticky="e")
        tk.Label(self.frame, text="Last Name:").grid(row=1, column=0, sticky="e")
        tk.Label(self.frame, text="User Class:").grid(row=2, column=0, sticky="e")
        tk.Label(self.frame, text="Student ID:").grid(row=3, column=0, sticky="e")
        tk.Label(self.frame, text="Password:").grid(row=5, column=0, sticky="e")
        tk.Label(self.frame, text="Email:").grid(row=6, column=0, sticky="e")
        tk.Label(self.frame, text="Phone Number:").grid(row=7, column=0, sticky="e")


        self.first_name_entry = tk.Entry(self.frame)
        self.last_name_entry = tk.Entry(self.frame)
        self.user_class_entry = tk.Entry(self.frame)
        self.id_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame, show="*")  # Hide password
        self.email_entry = tk.Entry(self.frame)
        self.phone_entry = tk.Entry(self.frame)


        self.first_name_entry.grid(row=0, column=1)
        self.last_name_entry.grid(row=1, column=1)
        self.user_class_entry.grid(row=2, column=1)
        self.id_entry.grid(row=3, column=1)
        self.password_entry.grid(row=5, column=1)
        self.email_entry.grid(row=6, column=1)
        self.phone_entry.grid(row=7, column=1)


        tk.Button(self.frame, text="Submit", command=self.submit).grid(row=8, column=0, columnspan=2)
        tk.Button(self.frame, text="Login", command=self.login).grid(row=9, column=0, columnspan=2)

    def submit(self):
        if not self.validate_input():
            return


        hashed_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()


        if self.check_existing_user():
            messagebox.showerror("Error", "User already registered.")
            return


        print(f"User Information:\n"
              f"First Name: {self.first_name_entry.get()}\n"
              f"Last Name: {self.last_name_entry.get()}\n"
              f"User Class: {self.user_class_entry.get()}\n"
              f"Hashed Password: {hashed_password}\n"
              f"Email: {self.email_entry.get()}\n"
              f"Phone Number: {self.phone_entry.get()}")

        conn = sqlite3.connect("GolfDataBase.db")


        insertion = "INSERT INTO USERDATA (ID, FName, LName, UserClass, Password, Email, PhoneNumber) VALUES (?, ?, ?, ?, ?, ?, ?)"

        insertionValues = (self.id_entry.get(), self.first_name_entry.get(), self.last_name_entry.get(), self.user_class_entry.get(), hashed_password, self.email_entry.get(), self.phone_entry.get())
        conn.execute(insertion, insertionValues)
        conn.commit()
        conn.close()

    def login(self):
        self.main.destroy()
        import Login
        Login.LoginWindow(self.main)

    def validate_input(self):
        # Email validation using regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9]+@ksu\.edu\.sa$')
        if not email_pattern.match(self.email_entry.get()):
            messagebox.showerror("Error", "Invalid email format.")
            return False

        # Phone number validation using regular expression
        phone_pattern = re.compile(r'^05[0-9]{8}$')
        if not phone_pattern.match(self.phone_entry.get()):
            messagebox.showerror("Error", "Invalid phone number format.")
            return False

        # Add more validation as needed

        return True

    def check_existing_user(self):
        # Dummy check for existing user (replace with actual database check)
        # For now, assume user doesn't exist
        return False

# Create the main application window
root = tk.Tk()
app = SignUpWindow(root)

# Run the application
root.mainloop()
