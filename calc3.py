import tkinter as tk
from tkinter import ttk,StringVar

class Calculator:
    def __init__(self,root):
        self.input1 = StringVar()
        self.input2 = StringVar()
        self.input3 = StringVar()
        self.result = StringVar()

        root.title("Calculator")
        root.geometry("480x360")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        input1_entry = ttk.Entry(mainframe,width=50,textvariable=self.input1)
        input2_entry = ttk.Entry(mainframe,width=50,textvariable=self.input2)
        input3_entry = ttk.Entry(mainframe,width=50,textvariable=self.input3)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        input1_entry.focus()
        input2_entry.focus()
        input3_entry.focus()
        ttk.Label(mainframe, text="input1").grid(column=3, row=0, sticky=tk.W)
        ttk.Label(mainframe, text="input2").grid(column=3, row=1, sticky=tk.W)
        ttk.Label(mainframe, text="sign").grid(column=3, row=2, sticky=tk.W)
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=0, row=3, sticky=tk.W)
        ttk.Label(mainframe, textvariable=self.result).grid(column=0, row=4, sticky=(tk.W, tk.E))
        root.bind("<Return>", self.result)

    def calculate(self):
        if self.input3.get() == "+":
            value1 = float(self.input1.get())
            value2 = float(self.input2.get())
            self.result.set(str(value1+value2))
        elif self.input3.get() == "-":
            value1 = float(self.input1.get())
            value2 = float(self.input2.get())
            self.result.set(str(value1-value2))
        elif self.input3.get() == "*":
            value1 = float(self.input1.get())
            value2 = float(self.input2.get())
            self.result.set(str(value1*value2))
        elif self.input3.get() == "/":
            try:
                value1 = float(self.input1.get())
                value2 = float(self.input2.get())
                assert value2!=0
                self.result.set(str(value1/value2))
            except AssertionError:
                pass
def main():
    gui = tk.Tk()
    app = Calculator(gui)
    gui.mainloop()
if __name__=="__main__":
    main()