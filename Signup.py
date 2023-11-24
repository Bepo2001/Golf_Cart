import tkinter as tk

class Signup:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sign up")
        self.window.geometry('800x800')
        self.window.geometry("+600+200") # to position the window in the center
        self.buttonBack = tk.Button(self.window, text='Login', command=self.go_Login)

        self.buttonBack.pack()
        self.window.mainloop()

    def go_Login(self):
        self.window.destroy()
        import Login
        Login.Login()

Signup()