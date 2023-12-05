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
        self.main.configure(bg="#add8e6")
        self.main.title("User Panel")
        self.frame = tk.Frame(self.main, bg="#add8e6")
        self.frame.grid(sticky="nsew")

        self.user_id = user_id
        self.user_class = user_class

        # Create tabs
        self.tabControl = ttk.Notebook(self.frame)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="Reserve a Cart")
        self.tabControl.add(self.tab2, text="View My Reservations")
        self.tabControl.grid(column=1, sticky="nsew")
        self.tabControl.pack(expand=1, fill="both")

        # Configure the style for the Notebook
        style = ttk.Style()
        style.configure('TNotebook', background='#add8e6')
        style.configure('TNotebook.Tab', background='#add8e6', font=('Helvetica', 12))

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

        font = ("Helvetica", 12)
        light_blue = "#add8e6"

        # Create a frame for the content of the tab
        reserve_frame = tk.Frame(self.tab1, bg=light_blue)
        reserve_frame.pack(expand=1, fill="both")

        # Labels and entry widgets
        tk.Label(reserve_frame, text="Select College:", bg=light_blue, font=font).grid(row=0, column=0, sticky="e")
        colleges = ["College of Computer and Information Sciences", "College of Science", "College of Engineering", "College of Business Administration"]
        college_menu = tk.OptionMenu(reserve_frame, self.selected_college, *colleges)
        college_menu.grid(row=0, column=1, ipadx=50, pady=7)

        tk.Label(reserve_frame, text="Choose Start Date:", bg=light_blue, font=font).grid(row=1, column=0, pady=20, sticky="e")
        self.start_date = DateEntry(reserve_frame, font=font, bg=light_blue)
        self.start_date.grid(row=1, column=1, pady=20)

        tk.Label(reserve_frame, text="Choose End Date:", bg=light_blue, font=font).grid(row=2, column=0, pady=20, sticky="e")
        self.end_date = DateEntry(reserve_frame, font=font, bg=light_blue)
        self.end_date.grid(row=2, column=1, pady=20)

        tk.Label(reserve_frame, text="Start Hour:", bg=light_blue, font=font).grid(row=3, column=0, pady=10, sticky="e")
        self.start_hour = tk.StringVar()
        tk.Entry(reserve_frame, textvariable=self.start_hour, font=font).grid(row=3, column=1, pady=10)

        tk.Label(reserve_frame, text="Start Min:", bg=light_blue, font=font).grid(row=4, column=0, pady=10, sticky="e")
        self.start_min = tk.StringVar()
        tk.Entry(reserve_frame, textvariable=self.start_min, font=font).grid(row=4, column=1, pady=10)

        tk.Label(reserve_frame, text="End Hour:", bg=light_blue, font=font).grid(row=5, column=0, pady=10, sticky="e")
        self.end_hour = tk.StringVar()
        tk.Entry(reserve_frame, textvariable=self.end_hour, font=font).grid(row=5, column=1, pady=10)

        tk.Label(reserve_frame, text="End Min:", bg=light_blue, font=font).grid(row=6, column=0, pady=10, sticky="e")
        self.end_min = tk.StringVar()
        tk.Entry(reserve_frame, textvariable=self.end_min, font=font).grid(row=6, column=1, pady=10)

        # Reserve button
        tk.Button(reserve_frame, text="Reserve", command=self.reserve_cart, font=font).grid(row=7, column=0, columnspan=2, pady=10)

        # Logout button
        tk.Button(reserve_frame, text="Logout", command=self.logout, font=font).grid(row=8, column=0, columnspan=2, pady=30)

        # tk.Entry(reserve_frame, bg=light_blue).grid(column=10, sticky="e")
        # tk.Entry(reserve_frame, bg=light_blue).grid(column=11, sticky="e")

    def create_view_reservations_tab(self):

        view_reservations_frame = tk.Frame(self.tab2, bg="#add8e6")
        view_reservations_frame.pack(expand=1, fill="both")

        tk.Label(view_reservations_frame, text="              View My Reservations", font=("Helvetica", 20, "bold"), bg="#add8e6").grid(row=0, column=0, pady=20, sticky="w")

        # Show button
        tk.Button(view_reservations_frame, text="View", command=self.show_reservations, font=("Helvetica", 12)).grid(row=1, column=0, pady=10)

        # Logout button
        tk.Button(view_reservations_frame, text="Logout", command=self.logout, font=("Helvetica", 12)).grid(row=2, column=0, pady=10)

        view_reservations_frame.columnconfigure(0, weight=1)

    def reserve_cart(self):
        logging.basicConfig(filename='cart.log',filemode='a',format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)
        start_datetime = datetime(int(self.start_date.get().split("/")[2]) + 2000, int(self.start_date.get().split("/")[0]), int(self.start_date.get().split("/")[1]), int(self.start_hour.get()), int(self.start_min.get()))
        end_datetime = datetime(int(self.end_date.get().split("/")[2]) + 2000, int(self.end_date.get().split("/")[0]), int(self.end_date.get().split("/")[1]), int(self.end_hour.get()), int(self.end_min.get()))
        maxFaculty = datetime(1, 1, 1, 1, 30) - datetime(1, 1, 1, 0, 0)
        maxEmployees = datetime(1, 1, 1, 1, 0) - datetime(1, 1, 1, 0, 0)
        maxStudents = datetime(1, 1, 1, 0, 30) - datetime(1, 1, 1, 0, 0)
        reserveTime = end_datetime - start_datetime
        if reserveTime > maxFaculty :
            return messagebox.showerror(title="Time exceed",message="you can't reserve a cart for that long time")
        elif self.user_class=="Employees" and reserveTime > maxEmployees:
            return messagebox.showerror(title="Time exceed",message="you can't reserve a cart for that long time")
        elif self.user_class=="Student" and reserveTime > maxStudents:
            return messagebox.showerror(title="Time exceed",message="you can't reserve a cart for that long time")
        else:
            conn = sqlite3.connect("GolfDataBase.db")
            sql="SELECT PlateNumber FROM CartData WHERE College = ?"
            sol=(self.selected_college.get(),)
            sil=list(conn.execute(sql,sol))
            for x in sil:
                spl = "SELECT StartDate,EndDate FROM Reservations WHERE PlateNumber = ?"
                sll = x
                skl = list(conn.execute(spl, sll))
                flag=True
                for y in skl:
                    y=list(y)
                    start=datetime.strptime(y[0],'%Y-%m-%d %H:%M:%S')
                    end=datetime.strptime(y[1],'%Y-%m-%d %H:%M:%S')
                    if start <= start_datetime <= end:
                        flag = False
                    elif start <= end_datetime <= end:
                        flag = False
                    elif start_datetime <= start and end_datetime >= end:
                        flag = False

                if flag == True:
                    sql = "INSERT INTO reservations (PlateNumber, ID, StartDate, EndDate) VALUES (?,?,?,?)"
                    values = (x[0], self.user_id, start_datetime, end_datetime)
                    print(values)
                    conn.execute(sql, values)
                    conn.commit()
                    print(x[0], self.user_id, start_datetime, end_datetime)
                    logging.info("the cart has been reserved")
                    return messagebox.showinfo(title="reserve succeed!",message="your reserve has been reserved")
            logging.info("the cart hasn't been reserved")
            return messagebox.showinfo(title="couldn't reserve", message="sorry no cart from this college available")

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
