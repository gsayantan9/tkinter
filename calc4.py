import tkinter as tk
from tkinter import ttk,StringVar

class Calculator:
    def __init__(self,root):
        self.input1 = StringVar()
        self.result = StringVar()

        root.title("Calculator")
        root.geometry("480x360")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        input_value = ttk.Entry(mainframe, width=50,textvariable=self.input1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        input_value.focus()
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=0, row=3, sticky=tk.W)
        ttk.Button(mainframe, text="Clear", command=self.clear).grid(column=0, row=4, sticky=tk.W)
        ttk.Label(mainframe, textvariable=self.result).grid(column=0, row=5, sticky=(tk.W, tk.E))
        root.bind("<Return>", self.result)

    def calculate(self):
        try:
            self.result.set(str(eval(self.input1.get())))
        except ValueError:
            pass

    def clear(self):
        self.input1.set("")
        self.result.set("")

def main():
    gui = tk.Tk()
    app = Calculator(gui)
    gui.mainloop()
if __name__=="__main__":
    main()