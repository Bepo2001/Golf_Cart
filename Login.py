import tkinter as tk

class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry('800x800')

        self.buttonBack = tk.Button(self.window, text='Sign up', command=self.go_signup)

        self.buttonBack.pack()
        self.window.mainloop()

    def go_signup(self):
        self.window.destroy()
        import Signup
        Signup.Signup()
