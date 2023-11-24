import hashlib
import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        # Labels
        tk.Label(master, text="ID:").grid(row=0, column=0, sticky="e")
        tk.Label(master, text="Password:").grid(row=1, column=0, sticky="e")

        # Entry widgets
        self.id_entry = tk.Entry(master)
        self.password_entry = tk.Entry(master, show="*")  # Hide password

        # Grid layout for entry widgets
        self.id_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        # Login button
        tk.Button(master, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)

    def login(self):
        # Validate input
        if not self.validate_input():
            return

        # Hash the entered password
        entered_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

        # Dummy: Check credentials against the central database (replace with actual database check)
        if self.check_credentials(entered_password):
            messagebox.showinfo("Success", "Login successful!")
            # Add logic to open the appropriate window based on user class (normal user or admin)
        else:
            messagebox.showerror("Error", "Invalid credentials.")

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

    def check_credentials(self, entered_password):
        # Dummy: Check against the central database (replace with actual database check)
        # For now, assume credentials are valid
        return True

# Create the main application window
root = tk.Tk()
app = LoginWindow(root)

# Run the application
root.mainloop()
