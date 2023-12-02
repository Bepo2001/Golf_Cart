import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import Login
from tkcalendar import DateEntry, Calendar
import logging

# start_time = datetime(2023, 11, 30, 22, 0)
# end_time = datetime(2023, 11,30,23, 0)
# query = "INSERT INTO Resv VALUES (?,?,?,?)"
# values = ("plate_number", "id", start_time, end_time)
#
# conn.execute(query, values)
#
# (datetime.strptime(date, "%Y-%m-%d %H:%M:%S") > start_date > datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) and (datetime.strptime(date, "%Y-%m-%d %H:%M:%S") > start_date > datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) and (datetime.strptime(date, "%Y-%m-%d %H:%M:%S") > start_date > datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))

class UserWindow:
    def __init__(self, main, user_id,user_class):
        self.main = main
        self.user_id = user_id
        self.user_class=user_class
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

        self.start_date = DateEntry(self.tab1)
        self.start_date.grid(pady=20)

        self.end_date = DateEntry(self.tab1)
        self.end_date.grid(pady=20)

        self.start_hour = tk.StringVar()
        tk.Entry(self.tab1, textvariable=self.start_hour, width=3).grid()

        self.start_min = tk.StringVar()
        tk.Entry(self.tab1, textvariable=self.start_min, width=3).grid()

        self.end_hour = tk.StringVar()
        tk.Entry(self.tab1, textvariable=self.end_hour, width=3).grid()

        self.end_min = tk.StringVar()
        tk.Entry(self.tab1, textvariable=self.end_min, width=3).grid()

        # Reserve button
        tk.Button(self.tab1, text="Reserve", command=self.reserve_cart).grid(row=3, column=0, columnspan=2)

        # Logout button
        tk.Button(self.tab1, text="Logout", command=self.logout).grid(row=4, column=0, columnspan=2)

    def create_view_reservations_tab(self):
        tk.Label(self.tab2, text="View My Reservations Tab").pack()

        # Show button
        tk.Button(self.tab2, text="Show", command=self.show_reservations).pack()

        # Logout button
        tk.Button(self.tab2, text="Logout", command=self.logout).pack()

    def reserve_cart(self):
        start_datetime = datetime(int(self.start_date.get().split("/")[2]) + 2000, int(self.start_date.get().split("/")[0]), int(self.start_date.get().split("/")[1]), int(self.start_hour.get()), int(self.start_min.get()))
        end_datetime = datetime(int(self.end_date.get().split("/")[2]) + 2000, int(self.end_date.get().split("/")[0]), int(self.end_date.get().split("/")[1]), int(self.end_hour.get()), int(self.end_min.get()))
        maxFaculty = datetime(1, 1, 1, 1, 30) - datetime(1, 1, 1, 0, 0)
        maxEmployees = datetime(1, 1, 1, 1, 0) - datetime(1, 1, 1, 0, 0)
        maxStudents = datetime(1, 1, 1, 0, 30) - datetime(1, 1, 1, 0, 0)
        reserveTime = end_datetime - start_datetime
        if reserveTime > maxFaculty :
            print()
        elif self.user_class=="Employees" and reserveTime > maxEmployees:
            print()
        elif self.user_class=="St;udent" and reserveTime > maxStudents:
            print()
        else:
            conn = sqlite3.connect("GolfDataBase.db")
            sql="SELECT PlateNumber FROM CartData WHERE College = ?"
            sol=(self.selected_college.get(),)
            sil=list(conn.execute(sql,sol))
            for x in sil:
                print(x)
                spl = "SELECT StartDate,EndDate FROM Reservations WHERE PlateNumber = ?"
                sll = x
                skl = list(conn.execute(spl, sll))
                flag=True
                for y in skl:
                    y=list(y)
                    start=datetime.strptime(y[0],'%Y-%m-%d %H:%M:%S')
                    end=datetime.strptime(y[1],'%Y-%m-%d %H:%M:%S')


    def show_reservations(self):
        conn = sqlite3.Connection("GolfDataBase.db")
        farr = conn.execute(
            "SELECT Reservations.PlateNumber,College,StartDate,EndDate FROM Reservations LEFT JOIN CartData ON Reservations.PlateNumber=CartData.PlateNumber WHERE ID = " + self.user_id)
        farr = list(farr)
        self.window = tk.Tk()
        self.select_reserve = ttk.Treeview(self.window, height=7, columns=(1, 2, 3, 4), show="headings")
        self.select_reserve.heading(1, text="Plate Number")
        self.select_reserve.column(1, minwidth=0, width=100, anchor=tk.CENTER)
        self.select_reserve.heading(2, text="Location")
        self.select_reserve.column(2, minwidth=0, width=110, anchor=tk.CENTER)
        self.select_reserve.heading(3, text="Start Time")
        self.select_reserve.column(3, minwidth=0, width=120, anchor=tk.CENTER)
        self.select_reserve.heading(4, text="End Time")
        self.select_reserve.column(4, minwidth=0, width=120, anchor=tk.CENTER)
        self.select_reserve.pack()
        for x in farr:
            self.select_reserve.insert(parent="", index=0, values=(x[0], x[1], x[2], x[3]))

    def logout(self):
        self.frame.destroy()
        Login.LoginWindow(self.main)
