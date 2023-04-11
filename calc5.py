import tkinter as tk
from tkinter import ttk,StringVar

class Calculator:
    def __init__(self,root):
        self.input1 = StringVar()
        self.result = StringVar()

        root.title("Calculator")
        root.geometry("480x360")
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        button_frame = ttk.Frame(root)
        button_frame.grid(column=0, row=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ttk.Entry(mainframe, width=50,textvariable=self.input1).grid(column=0,row=0,sticky=tk.W)
        ttk.Button(mainframe, text="C", command=self.clear).grid(column=1, row=0, sticky=tk.W)
        ttk.Button(button_frame, text="1",command=lambda:self.display(1)).grid(column=0, row=1, sticky=tk.W)
        ttk.Button(button_frame, text="2",command=lambda:self.display(2)).grid(column=1, row=1)
        ttk.Button(button_frame, text="3",command=lambda:self.display(3)).grid(column=2, row=1)
        ttk.Button(button_frame, text="/",command=lambda:self.display("/")).grid(column=3, row=1)
        ttk.Button(button_frame, text="4",command=lambda:self.display(4)).grid(column=0, row=2, sticky=tk.W)
        ttk.Button(button_frame, text="5",command=lambda:self.display(5)).grid(column=1, row=2)
        ttk.Button(button_frame, text="6",command=lambda:self.display(6)).grid(column=2, row=2)
        ttk.Button(button_frame, text="-",command=lambda:self.display("-")).grid(column=3, row=2)
        ttk.Button(button_frame, text="7",command=lambda:self.display(7)).grid(column=0, row=3, sticky=tk.W)
        ttk.Button(button_frame, text="8",command=lambda:self.display(8)).grid(column=1, row=3)
        ttk.Button(button_frame, text="9",command=lambda:self.display(9)).grid(column=2, row=3)
        ttk.Button(button_frame, text="+",command=lambda:self.display("+")).grid(column=3, row=3)
        ttk.Button(button_frame, text=".",command=lambda:self.display(".")).grid(column=0, row=4, sticky=tk.W)
        ttk.Button(button_frame, text="0",command=lambda:self.display(0)).grid(column=1, row=4)
        ttk.Button(button_frame, text="*",command=lambda:self.display("*")).grid(column=3,row=4)
        ttk.Button(button_frame, text="=",command=self.calculate).grid(column=2, row=4)  ## calculation will be done after this button is pressed
        root.bind("<Return>", self.result)

    def display(self,value):
        previous_value = self.input1.get()
        new_value = previous_value + str(value)
        self.input1.set(str(new_value))

    def calculate(self):
        try:
            self.input1.set(str(eval(self.input1.get())))
        except ValueError:
            pass

    def clear(self):
        self.input1.set("")

def main():
    gui = tk.Tk()
    app = Calculator(gui)
    gui.mainloop()
if __name__=="__main__":
    main()