import tkinter as tk
from tkinter import ttk,StringVar


class App:
    def __init__(self,root,feet,meters):
        self.root = root
        self.feet = feet
        self.meters = meters

    def calculate(self,*args):
        try:
            value = float(self.feet.get())
            self.meters.set(str(int(0.3048 * value * 10000.0 + 0.5)/10000.0))
        except ValueError:
            pass

    def create_mainframe(self):
        """Creating a Content Frame
        Next, we create a frame widget, which will hold the contents of our user interface."""
        self.root.geometry("480x360")
        self.root.title("Feet to Meters")
        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        feet_entry = ttk.Entry(mainframe,width=7,textvariable=self.feet)
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(tk.W, tk.E))

        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=tk.W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        feet_entry.focus()
        self.root.bind("<Return>", self.calculate)

def main():
    gui = tk.Tk()
    app = App(gui,StringVar(),StringVar())
    app.create_mainframe()
    gui.mainloop()

if __name__=="__main__":
    main()