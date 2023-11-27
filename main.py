import tkinter
import sqlite3
from tkinter import ttk
import Signup

# Admin id 4431015210, pass 12301230
# Student ID 1111111111, Pass 12301230


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
         FOREIGN KEY(PlateNumber) REFERENCES CartData(PlateNumber),
         FOREIGN KEY(ID) REFERENCES UserData(ID));''')


class App:
    def __init__(self):
        self.main = tkinter.Tk()

        Signup.SignUpWindow(self.main)

        self.main.mainloop()


if __name__ == "__main__":
    App()