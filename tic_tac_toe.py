import tkinter as tk
import numpy as np
from tkinter import ttk,StringVar
"""if a player starts from any corner the player can win in 3 ways
    if a player starts from any other position than the corner then he can win in two ways"""

class TicTacTo:
    def __init__(self,root):
        super().__init__()
        self.root = root
        self.mainframe = ttk.Frame(root)
        self.input1 = StringVar()
        self.result = StringVar()
        root.title("Tic Tac To")
        root.geometry("480x360")
        self.mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.e11 = ttk.Entry(self.mainframe,width=12)
        self.e11.grid(column=0, row=1, sticky=tk.W)
        self.e12 = ttk.Entry(self.mainframe,width=12)
        self.e12.grid(column=1, row=1)
        self.e13 = ttk.Entry(self.mainframe,width=12)
        self.e13.grid(column=2, row=1)
        self.e21 = ttk.Entry(self.mainframe,width=12)
        self.e21.grid(column=0, row=2)
        self.e22 = ttk.Entry(self.mainframe,width=12)
        self.e22.grid(column=1, row=2, sticky=tk.W)
        self.e23 = ttk.Entry(self.mainframe,width=12)
        self.e23.grid(column=2, row=2)
        self.e31 = ttk.Entry(self.mainframe,width=12)
        self.e31.grid(column=0, row=3)
        self.e32 = ttk.Entry(self.mainframe,width=12)
        self.e32.grid(column=1, row=3)
        self.e33 = ttk.Entry(self.mainframe,width=12)
        self.e33.grid(column=2, row=3)
        ttk.Button(self.mainframe,width=10,command=self.clear_all,text="Clear").grid(column=0,row=4,sticky=tk.W)
        ttk.Button(self.mainframe,width=10,text="Submit",command=self.submit_game).grid(column=2,row=4,sticky=tk.E)
        ttk.Label(self.mainframe,textvariable=self.result).grid(column=0, row=5, sticky=(tk.W, tk.E))

    # def display(self):
    #     """display all the widgets and define all the colors and etc in the main window"""
    #     self.root.title("Tic Tac To")
    #     self.root.geometry("480x360")
    #     self.mainframe.grid(column=0, row=0)
    #     self.root.columnconfigure(0, weight=1)
    #     self.root.rowconfigure(0, weight=1)
    #     e11 = ttk.Entry(self.mainframe,width=12)
    #     e11.grid(column=0, row=1, sticky=tk.W)
    #     e12 = ttk.Entry(self.mainframe,width=12)
    #     e12.grid(column=1, row=1)
    #     e13 = ttk.Entry(self.mainframe,width=12)
    #     e13.grid(column=2, row=1)
    #     e21 = ttk.Entry(self.mainframe,width=12)
    #     e21.grid(column=0, row=2)
    #     e22 = ttk.Entry(self.mainframe,width=12)
    #     e22.grid(column=1, row=2, sticky=tk.W)
    #     e23 = ttk.Entry(self.mainframe,width=12)
    #     e23.grid(column=2, row=2)
    #     e31 = ttk.Entry(self.mainframe,width=12)
    #     e31.grid(column=0, row=3)
    #     e32 = ttk.Entry(self.mainframe,width=12)
    #     e32.grid(column=1, row=3)
    #     e33 = ttk.Entry(self.mainframe,width=12)
    #     e33.grid(column=2, row=3)
    #     clear_button = ttk.Button(self.mainframe,width=10,command=self.clear_all,text="Clear")
    #     clear_button.grid(column=0,row=4,sticky=tk.W)
    #     submit_button = ttk.Button(self.mainframe,width=10,text="Submit",command=e11.get())
    #     submit_button.grid(column=2,row=4,sticky=tk.E)
    #     ttk.Label(self.mainframe,textvariable=self.result,width=10).grid(column=1, row=5, sticky=(tk.W, tk.E))
        

    def clear_all(self):
        """Clear all the selection in the tic tac to boxes and also clear the result"""
        for i in self.mainframe.winfo_children():
            if isinstance(i,ttk.Entry):
                i.delete(0,tk.END)
        self.result.set("")
        

    def submit_game(self):
        """evaluate which player has won, either cross or circle either one of them can win
        the game can also be finished at a draw if neither of them can complete the requirement"""
        # self.result.set(f"{self.e11.get()}")
        input_value_matrix = np.array([i.get() for i in self.mainframe.winfo_children() if isinstance(i,ttk.Entry)])
        input_value_matrix = np.reshape(input_value_matrix,newshape=(3,3))
        # """the diagonal and anti-diagonal cases"""
        if len(set(input_value_matrix.diagonal()))==1:
            if set(input_value_matrix.diagonal())=={'+'}:
                self.result.set("Cross wins the game!")
            elif set(input_value_matrix.diagonal())=={'o'}:
                self.result.set("Circle wins the game!")
        elif len(set(np.fliplr(input_value_matrix).diagonal()))==1:
            if set(np.fliplr(input_value_matrix).diagonal())=={'+'}:
                self.result.set("Cross wins the game!")
            elif set(np.fliplr(input_value_matrix).diagonal())=={'o'}:
                self.result.set("Circle wins the game!")
        # the horizontal row cases
        elif len(set(input_value_matrix[0,:]))==1 or len(set(input_value_matrix[1,:]))==1 or \
            len(set(input_value_matrix[2,:]))==1:
            if set(input_value_matrix[0,:]) == {'+'} or set(input_value_matrix[1,:]) == {'+'} or \
                set(input_value_matrix[2,:]) == {'+'}:
                self.result.set("Cross wins the game!")
            else:
                self.result.set("Circle wins the game!")
        # the vertical column cases
        elif len(set(input_value_matrix[:,0]))==1 or len(set(input_value_matrix[:,1]))==1 or \
            len(set(input_value_matrix[:,2]))==1:
            if set(input_value_matrix[:,0]) == {'+'} or set(input_value_matrix[:,1]) == {'+'} or \
                 set(input_value_matrix[:,2]) == {'+'}:
                self.result.set("Cross wins the game!")
            else:
                self.result.set("Circle wins the game!")

def main():
    gui = tk.Tk()
    app = TicTacTo(gui)
    # app.display()
    gui.mainloop()
if __name__=="__main__":
    main()


