import tkinter
import sqlite3
from tkinter import ttk




conn = sqlite3.connect("GolfDataBase.db")
conn.execute('''CREATE TABLE IF NOT EXISTS UserData
         (ID INT PRIMARY KEY NOT NULL,
         FName TEXT NOT NULL,
         LName TEXT NOT NULL,
         UserClass TEXT NOT NULL,
         Password TEXT NOT NULL,
         Email TEXT NOT NULL,
         PhoneNumber INT(10) NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS CartData
         (PlateNumber INT PRIMARY KEY NOT NULL,
         College TEXT NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS Reservations
         (PlateNumber INT NOT NULL,
         ID INT NOT NULL,
         StartDate TIMESTAMP NOT NULL,
         EndDate TIMESTAMP NOT NULL,
         FOREIGN KEY(PlateNumber) REFERENCES CareData(PlateNumber),
         FOREIGN KEY(ID) REFERENCES UserData(ID));''')

class app:
    def init(self):
        self.main = tkinter.Tk()
        self.main.title("Golf carts App")
        self.employment_form = tkinter.LabelFrame(self.main, text="KSU Golf Carts",padx=120)

        self.iframe = tkinter.Frame(self.employment_form,height=500,width=600)
        self.employment_form.grid()
        self.iframe.grid()
        tkinter.Label(self.iframe, text="Welcome to the app!").grid(row=0, column=0, pady=5)
        tkinter.Button(self.iframe, text="Sign up", width=10).grid(row=1, column=0, pady=10)
        tkinter.Button(self.iframe, text="Login", width=10).grid(row=1, column=1, pady=10)

        self.main.mainloop()


     # def change_page(self, page_name):
     #     self.current_page.frame.destroy()
     #     self.current_page = page_name(self)