import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import csv
import Login


class UserWindow:
    def __init__(self, main, data):
        self.main = main
        self.data = data # self.data.get("user_id")
        self.main.title("User Panel")
        self.frame = tk.Frame(self.main)
        self.frame.grid()
        # Create tabs
        self.tabControl = ttk.Notebook(self.frame)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="Reserve a Cart")
        self.tabControl.add(self.tab2, text="View My Reservations")
        self.tabControl.pack(expand=1, fill="both")

        # Variables for reservation details
        self.selected_college = tk.StringVar()
        self.start_time_var = tk.StringVar()
        self.end_time_var = tk.StringVar()

        # Tab 1: Reserve a Cart
        self.create_reserve_tab()

        # Tab 2: View My Reservations
        self.create_view_reservations_tab()

    def create_reserve_tab(self):
        # Labels and entry widgets
        tk.Label(self.tab1, text="Select College:").grid(row=0, column=0, sticky="e")
        colleges = ["College of Computer and Information Sciences", "College of Science", "College of Engineering", "College of Business Administration"]
        college_menu = tk.OptionMenu(self.tab1, self.selected_college, *colleges)
        college_menu.grid(row=0, column=1)

        tk.Label(self.tab1, text="Start Time & Date:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.tab1, textvariable=self.start_time_var).grid(row=1, column=1)

        tk.Label(self.tab1, text="End Time & Date:").grid(row=2, column=0, sticky="e")
        tk.Entry(self.tab1, textvariable=self.end_time_var).grid(row=2, column=1)

        # Reserve button
        tk.Button(self.tab1, text="Reserve", command=self.reserve_cart).grid(row=3, column=0, columnspan=2)

        # Logout button
        tk.Button(self.tab1, text="Logout", command=self.logout).grid(row=4, column=0, columnspan=2)

    def create_view_reservations_tab(self):
        # Placeholder for the View My Reservations tab
        # You can add the necessary UI elements and logic based on your requirements
        tk.Label(self.tab2, text="View My Reservations Tab").pack()

        # Show button
        tk.Button(self.tab2, text="Show", command=self.show_reservations).pack()

        # Logout button
        tk.Button(self.tab2, text="Logout", command=self.logout).pack()

    def reserve_cart(self):
        # Dummy: Implement reservation logic based on the provided rules
        # Replace the following code with your actual reservation logic

        # Check reservation period validity
        if not self.validate_reservation_period():
            return

        # Dummy: Check availability in the central database (replace with actual database check)
        if self.check_availability():
            # Dummy: Reserve the cart and log the transaction
            self.log_transaction("success")
            messagebox.showinfo("Success", "Cart reserved successfully!")
        else:
            # Dummy: Log the transaction for a failed reservation
            self.log_transaction("failure")
            messagebox.showerror("Error", "Cart not available for the given time & date.")

    def validate_reservation_period(self):
        # Dummy: Validate reservation period based on user class
        # Replace this with your actual validation logic

        # For now, assume the validation is successful
        return True


    def check_availability(self):
        # Dummy: Check availability in the central database
        # Replace this with your actual database check
        # For now, assume the cart is available
        return True

    def show_reservations(self):
        # Dummy: Show reservations for the user
        # Replace this with your actual logic to retrieve and display reservations
        messagebox.showinfo("Reservations", "No reservations to display.")

    def log_transaction(self, status):
        # Dummy: Log transaction to a CSV file (replace with actual logging mechanism)
        transaction_data = [
            [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             "User ID Placeholder",  # Replace with the actual user ID
             "Golf Cart Plate Placeholder",  # Replace with the actual plate number
             self.selected_college.get(),
             self.start_time_var.get(),
             self.end_time_var.get(),
             status]
        ]

        with open('transaction_log.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(transaction_data)

    def logout(self):
        # Add logic to go back to the sign-up window or login window
        self.frame.destroy()
        Login.LoginWindow(self.main)
