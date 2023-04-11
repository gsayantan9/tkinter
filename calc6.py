import tkinter as tk
from tkinter import ttk,StringVar

class App:
    def __init__(self,root) -> None:
        root.title("Just An APP")
        root.geometry("500x500")
def main():
    gui = tk.Tk()
    App(gui)
    gui.mainloop()
if __name__=="__main__":
    main()
    if 1 != 2:
        print("hello")