import hashlib
import sqlite3
import tkinter as tk
from tkinter import messagebox
import Signup
import User
import Admin

class LoginWindow:
    def __init__(self, main):
        self.main = main
        self.main.title("Login Panel")
        # self.main.columnconfigure(0, weight=1)
        # self.main.rowconfigure(0, weight=1)
        self.frame = tk.Frame(self.main, bg="#add8e6")
        self.frame.grid(sticky="ns")


        welcome_font = ("Helvetica", 20, "bold")
        font = ("Helvetica", 14)
        button_font = ("Helvetica", 13)
        light_blue = "#add8e6"

        # Labels
        tk.Label(self.frame, text="Welcome Back", font=welcome_font, bg=light_blue).grid(row=0, column=0, columnspan=3, pady=70, sticky="n")
        tk.Label(self.frame, text="ID:", font=font, bg=light_blue).grid(row=1, column=0, sticky="e", pady=5, padx=3)
        tk.Label(self.frame, text="Password:", font=font, bg=light_blue).grid(row=2, column=0, sticky="e", pady=5, padx=3)
        tk.Label(self.frame, text="Don't have an account ?", font=font, bg=light_blue).grid(row=7, column=1, sticky="w", pady=5)

        # Entry widgets
        self.id_entry = tk.Entry(self.frame, font=font)
        self.password_entry = tk.Entry(self.frame, show="*", font=font)  # Hide password

        # Grid layout for entry widgets
        self.id_entry.grid(row=1, column=1, sticky="e", pady=5, padx=3)
        self.password_entry.grid(row=2, column=1, sticky="e", pady=5, padx=3)

        # Login button
        tk.Button(self.frame, text="Login", command=self.login, font=button_font).grid(row=5, column=1, pady=15)
        tk.Button(self.frame, text="Sign Up", command=self.Sign_Up, font=button_font).grid(row=7, column=2, columnspan=1, sticky="w", pady=20)


    def login(self):
        # Validate input
        if not self.validate_input():
            return

        # Hash the entered password
        entered_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

        conn = sqlite3.Connection("GolfDataBase.db")
        farr = conn.execute("SELECT Password, UserClass FROM UserData WHERE ID = "+ self.id_entry.get())
        farr = list(farr)
        if farr[0][0] == entered_password:
            user_id = self.id_entry.get()
            if farr[0][1] == "Admin":
                self.frame.destroy()
                Admin.AdminWindow(self.main)
            else:
                self.frame.destroy()
                User.UserWindow(self.main, user_id=user_id,user_class=farr[0][1])
        else:
            messagebox.showerror("error","ID or Password is incorrect")

    def Sign_Up(self):
        self.frame.destroy()
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


#
# # Create the main application window
# root = tk.Tk()
# app = LoginWindow(root)
#
# # Run the application
# root.mainloop()
