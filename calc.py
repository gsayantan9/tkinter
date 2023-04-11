# from sqlite3 import Row
import tkinter as tk
from tkinter import ttk
from tkinter import *
# from typing import List
# # import numpy as np
# # import pandas as pd
#
# # def show_buttons(root):
# #     sign_list = """+,-,*,/,clear,%,.,=""".split(sep=',')
# #     num_and_sign_list = np.arange(0,10).astype(str).tolist() + sign_list
# #     entry = tk.Entry(root)
# #     entry.grid(row=0,columnspan=10)
#     # tk.Label(root,text='first').grid(row=0)
#     # tk.Label(root,text='second').grid(row=1)
#     # e1 = tk.Entry(root)
#     # e2 = tk.Entry(root)
#     # e1.grid(row=0,column=1)
#     # e2.grid(row=1,column=1)
#     # num_and_sign_list = np.array(num_and_sign_list).reshape(6,3).squeeze()
#     # for i in range(6):
#     #     for j in range(3):
#     #         btn = tk.Button(root,text=num_and_sign_list[i][j],bd='5')
#     #         btn.place()
#     #         if j == 2:
#     #             print('',end='\n')
#     # j = 0
#     # i = 1
#     # for x in num_and_sign_list:
#     #         btn = tk.Button(root,text=x,bd='5')
#     #         btn.grid(row=i,column=j)
#     #         j = j+1
#     #         if j == 3:
#     #             i = i+1
#     #             btn.grid(row=i,column=j)
#     # btn1 = tk.Button(root,text='0',bd='5')
#     # btn1.grid(row=1,column=0)
#     # btn2 = tk.Button(root,text='1',bd='5')
#     # btn2.grid(row=2,column=0)
#     # tk.Checkbutton()
#     # btn3 = tk.Button(root,text='2',bd='5')
#     # btn3.place(x=40,y=0)
#     # btn4 = tk.Button(root,text='3',bd='5')
#     # btn4.place(x=0,y=30)
#
# def show_text_input(root):
#     canvas1 = tk.Canvas(root, width=400, height=300)
#     canvas1.pack()
#     entry1 = tk.Entry(root)
#     canvas1.create_window(200, 140, window=entry1)
#
# def do_calculations():
#     text = tk.Text()
#     text.insert(tk.INSERT,"Hello World!")
#     # text.pack()
#
# def show_button(root,value):
#     # btn1 = tk.Button(root,text='Press Button',command=do_calculations)
#     # btn1.pack()
#     btn = tk.Button(root,text=str(value))
#     btn.pack()
#
# def main():
#     gui = tk.Tk()  ## initializing the gui window
#     gui.title('This is a calculator,Welcome!')
#     gui.geometry('480x360')
#     show_text_input(gui)  ## show text input
#     show_button(gui,1)  ## show button function
#     show_button(gui,2)
#     # show_button_1(gui) ## show number buttons
#     gui.mainloop()  ## the windows stays forever open
# if __name__=='__main__':
#     main()

# We'll create a simple GUI tool to convert a distance in feet to the equivalent distance in meters.
# If we were to sketch this out, it might look something like this:
# The layout of our user interface, which follows a 3 x 3 grid.




def main():
    gui = tk.Tk()
    gui.geometry("480x360")
    gui.title("Feet to Meters")
    mainframe = ttk.Frame(gui, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N,tk.W, tk.E, tk.S))
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1)
    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
    meters = StringVar()
    def calculate(*args):
        try:
            value = float(feet.get())
            meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass
    ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(tk.W, tk.E))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=tk.W)

    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W)
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    feet_entry.focus()
    gui.bind("<Return>", calculate)
    gui.mainloop()

if __name__=="__main__":
    main()


