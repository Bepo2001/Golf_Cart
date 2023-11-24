import tkinter
from tkinter import ttk

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


     def change_page(self, page_name):
         self.current_page.frame.destroy()
         self.current_page = page_name(self)