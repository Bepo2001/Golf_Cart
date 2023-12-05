import tkinter as tk
from tkinter import messagebox
import re
import hashlib
import sqlite3
import Login


class SignUpWindow:
    def __init__(self, main):
        self.main = main
        self.main.title("Signup Panel")
        self.main.geometry("500x500")
        self.main.configure(bg="#add8e6")  # Hexadecimal code for light blue
        self.main.columnconfigure(0, weight=1)
        self.main.rowconfigure(0, weight=1)

        welcome_font = ("Helvetica", 20, "bold")
        font = ("Helvetica", 12)
        light_blue = "#add8e6"

        self.frame = tk.Frame(self.main, bg="#add8e6")
        self.frame.grid()

        tk.Label(self.frame, text="        Welcome to KSU Golf", font=welcome_font, bg=light_blue).grid(row=0, column=0, columnspan=2, pady=20)
        tk.Label(self.frame, text="First Name:", font=font, bg=light_blue).grid(row=1, column=0, sticky="e", padx=3, pady=5)
        tk.Label(self.frame, text="Last Name:", font=font, bg=light_blue).grid(row=2, column=0, sticky="e", padx=3, pady=5)
        tk.Label(self.frame, text="User Class:", font=font, bg=light_blue).grid(row=3, column=0, sticky="e", padx=3, pady=5)
        tk.Label(self.frame, text="Student ID:", font=font, bg=light_blue).grid(row=4, column=0, sticky="e", padx=3, pady=5)
        tk.Label(self.frame, text="Password:", font=font, bg=light_blue).grid(row=5, column=0, sticky="e", padx=3, pady=5)
        tk.Label(self.frame, text="Email:", font=font, bg=light_blue).grid(row=6, column=0, sticky="e", padx=3, pady=5)
        tk.Label(self.frame, text="Phone Number:", font=font, bg=light_blue).grid(row=7, column=0, sticky="e", padx=3, pady=5)

        self.first_name_entry = tk.Entry(self.frame, font=font)
        self.last_name_entry = tk.Entry(self.frame, font=font)
        #self.user_class_entry = tk.Entry(self.frame, font=font)
        self.selected_class = tk.StringVar()
        Classes = ["Student", "Employee", "Faculty", "Admin"]
        self.college_menu = tk.OptionMenu(self.frame, self.selected_class, *Classes)
        self.id_entry = tk.Entry(self.frame, font=font)
        self.password_entry = tk.Entry(self.frame, show="*", font=font)  # Hide password
        self.email_entry = tk.Entry(self.frame, font=font)
        self.phone_entry = tk.Entry(self.frame, font=font)

        self.first_name_entry.grid(row=1, column=1, pady=5)
        self.last_name_entry.grid(row=2, column=1, pady=5)
        self.college_menu.grid(row=3, column=1, pady=5, ipadx=25)
        self.id_entry.grid(row=4, column=1, pady=3)
        self.password_entry.grid(row=5, column=1, pady=5)
        self.email_entry.grid(row=6, column=1, pady=5)
        self.phone_entry.grid(row=7, column=1, pady=5)

        tk.Button(self.frame, text="Submit", command=self.submit, font=font).grid(row=8, column=0, columnspan=2, pady=15)
        tk.Label(self.frame, text="Already Have An Account?", font=font, bg=light_blue).grid(row=9, column=1, sticky="w", padx=1)
        tk.Button(self.frame, text="Login", command=self.login, font=font).grid(row=9, column=2, sticky="e", columnspan=1, pady=1)

    def submit(self):
        if not self.validate_input():
            return

        hashed_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()
        conn = sqlite3.connect("GolfDataBase.db")
        try:
            insertion = "INSERT INTO UserData (ID, FName, LName, UserClass, Password, Email, PhoneNumber) VALUES (?,?,?,?,?,?,?)"

            insertionValues = (self.id_entry.get(), self.first_name_entry.get(), self.last_name_entry.get(), self.selected_class.get(), hashed_password, self.email_entry.get(), self.phone_entry.get())
            conn.execute(insertion, insertionValues)
            conn.commit()
            messagebox.showinfo("Success", "Your Account Has Been Created Successfully!.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Account Already Exists!")
        conn.close()

    def login(self):
        self.frame.destroy()
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

        # Check for valid user classes
        user_class = self.selected_class.get().lower()
        valid_user_classes = ["student", "faculty", "employee"]
        if user_class not in valid_user_classes:
            messagebox.showerror("Error", "Invalid user class. Please choose Student, Faculty, Employee, or Admin.")
            return False

        # ID validation based on user class
        if user_class == "student" and not (self.id_entry.get().isdigit() and len(self.id_entry.get()) == 10):
            messagebox.showerror("Error", "For students, ID must be 10 digits.")
            return False
        elif user_class in ["faculty", "employee"] and not (
                self.id_entry.get().isdigit() and len(self.id_entry.get()) == 6):
            messagebox.showerror("Error", "For Faculty and Employees, ID must be 6 digits.")
            return False

        return True