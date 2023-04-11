import tkinter as tk
from tkinter import ttk,StringVar

class App:
    def __init__(self,root) -> None:
        self.root = root
        self.name_input = StringVar()
        self.email_input = StringVar()
        self.submit_result = StringVar()
        root.title("Register & Login")
        root.geometry("480x360")
    ## one is register window
class register(App):
    def __init__(self, root) -> None:
        super().__init__(root)
        mainframe = ttk.Frame(self.root)
        mainframe.grid(column=0, row=0,sticky=tk.E)
        ttk.Label(mainframe,text="Register Yourself here!").grid(column=1,row=0)
        ttk.Entry(mainframe, textvariable=self.name_input).grid(column=1,row=1,sticky=(tk.E,tk.W))
        ttk.Entry(mainframe, width=50,textvariable=self.email_input).grid(column=1,row=3,sticky=(tk.E,tk.W))
        ttk.Label(mainframe,text="Username").grid(column=0,row=1,sticky=tk.E)
        ttk.Label(mainframe,text="Email").grid(column=0,row=3,sticky=tk.E)
        ttk.Label(mainframe,text="Submitted!").grid(sticky=tk.E)
        ttk.Button(mainframe,text="Submit",command=self.submit).grid(column=1,row=4)
    ## after successful register you need to login
    def submit(self):
        value = "Your Name has been registered!"
        self.submit_result.set(str(value))
        print(self.submit_result.set(str(value)))
# class login(App):
#     def __init__(self, root) -> None:
#         super().__init__(root)
#         mainframe1 = ttk.Frame(self.root)
#         mainframe1.grid(column=0, row=1,sticky=tk.E)
#         ttk.Label(mainframe1,text="Login here!").grid(column=1,row=0)
#         ttk.Entry(mainframe1, width=50).grid(column=1,row=1,sticky=(tk.E,tk.W))
#         ttk.Entry(mainframe1, width=50).grid(column=1,row=3,sticky=(tk.E,tk.W))
#         ttk.Label(mainframe1,text="Username").grid(column=0,row=1,sticky=tk.E)
#         ttk.Label(mainframe1,text="Email").grid(column=0,row=3,sticky=tk.E)
#         ttk.Button(mainframe1,text="Submit").grid(column=1,row=4)

def main():
    gui = tk.Tk()
    app = App(gui)
    reg = register(gui)
    reg.submit()
    # log = login(gui)
    gui.mainloop()
if __name__=="__main__":
    main()