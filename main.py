import tkinter as tk
from tkinter import ttk,StringVar
from tkinter.scrolledtext import ScrolledText
import pandas as pd
from db2 import Database
"""create the table within our database"""
db = Database()

class Employee:
    def __init__(self,root:tk.Tk) -> None:
        super().__init__()
        self.root = root
        # we cannot just take any text input from any box we have to specify it
        self.name = StringVar()
        self.age = StringVar()
        self.doj = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.result = StringVar()

        self.entries_frame = tk.Frame(self.root, bg="#535c68")
        self.button_frame = tk.Frame(self.root, bg="#535c68")
        self.address_entry = tk.Text(self.entries_frame, wrap=tk.WORD,height=10,width=100)

    def display(self):
        """modify the display of the GUI"""
        self.root.title("Employee management Portal")
        self.root.geometry("850x720")
        self.root.configure(background="#2c3e50")

        # Entries Frame
        self.entries_frame.pack(side=tk.TOP, fill=tk.X)
        title = tk.Label(self.entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
        title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        name_label = ttk.Label(self.entries_frame,font=('Calibri',14),text="Name",background="#535c68",foreground="white")
        name_label.grid(column=0,row=1,padx=10,pady=10)
        name_entry = ttk.Entry(self.entries_frame,width=50,background="white",textvariable=self.name)
        name_entry.grid(column=1,row=1,padx=10,pady=10)

        age_label = ttk.Label(self.entries_frame,text="Age",font=('Calibri',14),background="#535c68",foreground="white")
        age_label.grid(column=2,row=1,padx=20,pady=10)
        age_entry = ttk.Entry(self.entries_frame,width=50,background="white",textvariable=self.age)
        age_entry.grid(row=1,column=3,padx=10,pady=10)

        doj_label = ttk.Label(self.entries_frame,font=('Calibri',14),background="#535c68",foreground="white",text="D.O.J")
        doj_label.grid(column=0,row=2,padx=10,pady=10)
        doj_entry = ttk.Entry(self.entries_frame,background="white",width=50,textvariable=self.doj)
        doj_entry.grid(column=1,row=2,padx=10,pady=10)

        email_label = ttk.Label(self.entries_frame,text="Email",background="#535c68",foreground="white",font=('Calibri',14))
        email_label.grid(column=2,row=2,padx=10,pady=10)
        email_entry = ttk.Entry(self.entries_frame,width=50,background="white",textvariable=self.email)
        email_entry.grid(column=3,row=2,padx=10,pady=10)

        gender_label = ttk.Label(self.entries_frame,text="Gender",background="#535c68",foreground="white",font=('Calibri',14))
        gender_label.grid(column=0,row=3,padx=10,pady=10)
        gender_entry = ttk.Entry(self.entries_frame,width=50,background="white",textvariable=self.gender)
        gender_entry.grid(column=1,row=3,padx=10,pady=10)

        contact_label = ttk.Label(self.entries_frame,text="Contact",background="#535c68",foreground="white",font=('Calibri',14))
        contact_label.grid(column=2,row=3,padx=10,pady=10)
        contact_entry = ttk.Entry(self.entries_frame,width=50,background="white",textvariable=self.contact)
        contact_entry.grid(column=3,row=3,padx=10,pady=10)

        address_label = ttk.Label(self.entries_frame,text="Address",background="#535c68",foreground="white",font=('Calibri',14))
        address_label.grid(column=0,row=4,sticky=tk.W,padx=10)

        self.address_entry.grid(row=5,columnspan=4,padx=10,pady=10)

        self.button_frame.pack(fill=tk.X)

        clear_button = ttk.Button(self.button_frame,command=self.clear_details,text="Clear Details")
        clear_button.grid(row=6,column=0,padx=10)

        add_button = ttk.Button(self.button_frame,command=self.add_details,text="Add Details")
        add_button.grid(row=6,column=1,padx=10)

        update_button = ttk.Button(self.button_frame,command=self.clear_details,text="Update Details")
        update_button.grid(column=2,row=6,padx=10)
        
        delete_button = ttk.Button(self.button_frame,command=self.clear_details,text="Delete Details")
        delete_button.grid(column=3,row=6,padx=10)

        view_button = ttk.Button(self.button_frame,command=self.view_details,text="View Details")
        view_button.grid(column=4,row=6,padx=10)

        # result_text = ttk.Label(self.root,textvariable=self.result,
        #                         background="#2c3e50",foreground="white",
        #                         font=('Calibri',14))
        # result_text.pack_configure(padx=10,pady=10,side="bottom")

        global messagebox
        messagebox = tk.Text(self.root, height=50, width=200)
        messagebox.pack_configure(padx=10, pady=10, side="bottom")

    def add_details(self):
        if self.name.get() == "" or self.age.get() == "" or self.doj.get() == "" or self.email.get() == "" \
                or self.contact.get() == "" or self.gender.get() == "" or \
                self.address_entry.get(index1="1.0",index2=tk.END) == "":
            self.result.set("Please enter all the information!")
            messagebox.insert(index="1.0", chars=self.result.get())
        else:
            db.insert(name=self.name.get(),age=float(self.age.get()),gender=self.gender.get(),
                      doj=self.doj.get(),email=self.email.get(),contact=self.contact.get(),
                      address=self.address_entry.get(index1="1.0",index2=tk.END))
            self.result.set(
                pd.read_sql("""SELECT * FROM employees""",con=db.conn).to_string()
            )
            messagebox.insert(index="1.0", chars=self.result.get())

    def clear_details(self):
        """Clear all the selection in all the query boxes"""
        self.name.set("")
        self.age.set("")
        self.doj.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.result.set("")
        for i in self.entries_frame.winfo_children():
            if isinstance(i,tk.Text):
                i.delete(index1="1.0",index2=tk.END)
        for i in self.root.winfo_children():
            if isinstance(i,tk.Text):
                i.delete(index1="1.0",index2=tk.END)

    def view_details(self):
        # """view the query result"""
        # df = pd.read_csv(r"C:\Users\GSAYANTA\Downloads\titanic_dataset.csv")
        # df_text = tk.Text(height=50,width=200)
        # df_text.insert(tk.END,str(df.iloc[:]))
        # df_text.pack(padx=10,pady=10)
        pass
def main():
    gui = tk.Tk()
    app = Employee(gui)
    app.display()
    gui.mainloop()
if __name__=="__main__":
    main()

