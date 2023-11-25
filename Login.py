import hashlib
import sqlite3
import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, main):
        self.main = main
        self.frame = tk.Frame(self.main)
        self.frame.grid()

        # Labels
        tk.Label(self.frame, text="ID:").grid(row=0, column=0, sticky="e")
        tk.Label(self.frame, text="Password:").grid(row=1, column=0, sticky="e")

        # Entry widgets
        self.id_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame, show="*")  # Hide password

        # Grid layout for entry widgets
        self.id_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        # Login button
        tk.Button(self.frame, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)
        tk.Button(self.frame, text="Sign Up", command=self.Sign_Up).grid(row=3, column=0, columnspan=2)

    def login(self):
        # Validate input
        if not self.validate_input():
            return



        # Hash the entered password
        entered_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

        # Dummy: Check credentials against the central database (replace with actual database check)
        conn=sqlite3.Connection("GolfDataBase.db")
        farr=conn.execute("SELECT Password FROM UserData WHERE ID = "+ self.id_entry.get)
        farr=list(farr)
        if farr[0][0]==entered_password:
             GO TO ADMIN
        else:
            messagebox.showerror("error","ID or Password is incorrect")

    def Sign_Up(self):
        self.main.destroy()
        import Signup
        Signup.SignUpWindow(self.main)
    def validate_input(self):
        # ID validation
        if not self.id_entry.get().isdigit() or \
                (len(self.id_entry.get()) not in [6, 10]):
            messagebox.showerror("Error", "Invalid ID. Please enter digits, and ensure it's 6 or 10 digits.")
            return False

        # Password validation (add more as needed)
        if len(self.password_entry.get()) < 6:
            messagebox.showerror("Error", "Password should be at least 6 characters.")
            return False

        return True



# Create the main application window
root = tk.Tk()
app = LoginWindow(root)

# Run the application
root.mainloop()
