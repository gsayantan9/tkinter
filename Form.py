# we will build a name and email submit form
import tkinter as tk
from tkinter import ttk,StringVar

class App:
    def __init__(self,root,name,email,full_details):
        self.root = root
        self.name = name
        self.email = email
        self.full_details = full_details

    def create_mainframe(self):
        self.root.geometry("480x360")
        self.root.title("Email Form")
        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        name_entry = ttk.Entry(mainframe,width=50,textvariable=self.name)
        email_entry = ttk.Entry(mainframe,width=50,textvariable=self.email)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        name_entry.focus()
        email_entry.focus()
        ttk.Label(mainframe, text="name").grid(column=3, row=0, sticky=tk.W)
        ttk.Label(mainframe, text="email").grid(column=3, row=1, sticky=tk.W)
        ttk.Button(mainframe, text="submit", command=self.show_details).grid(column=0, row=3, sticky=tk.W)
        # ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
        ttk.Label(mainframe, textvariable=self.full_details).grid(column=0, row=4, sticky=(tk.W, tk.E))
        # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W)
        self.root.bind("<Return>", self.show_details)

    def show_details(self,*args):
        try:
            # self.name.set(str(self.name))
            # email_value = self.email.get()
            # self.email.set(str(email_value))
            self.full_details.set(f"your name is {self.name.get()} and your email is {self.email.get()} is registered!")
            # self.full_details.set(self.name.get())
        except ValueError:
            pass

def main():
    gui = tk.Tk()
    app = App(gui,StringVar(),StringVar(),StringVar())
    app.create_mainframe()
    gui.mainloop()
if __name__=="__main__":
    main()