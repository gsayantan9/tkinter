import sqlite3
from typing import Optional
"""create a database system for the employee where the columns are id,name,age,doj,email ,gender,contact,address"""
"""We will create every methods and other stuffs related to database of our system"""
"""https://www.tutorjoes.in/tkinter_python_tutorial_tamil/"""


class Database:
    def __init__(self,db) -> None:
        self.db = db
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text)"""
        self.cur.execute(sql)
        self.conn.commit()

    def Insert(self,name,age,doj,email,gender,contact,address:Optional[str]=" "):
        """insert info into database"""
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",(name, age, doj, email, gender, contact, address))
        self.conn.commit()

    def Fetch(self,id):
        """Fetch the info from the database"""
        self.cur.execute(f"select * from employees where id={id}")
        self.conn.commit()

    def Update(self,id,name,age,email,gender,contact,address,doj):
        """update info in the database"""
        self.cur.execute("update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
            (name, age, doj, email, gender, contact, address, id))
        self.conn.commit()

    def Delete(self,id):
        "delete a record in the database"
        self.cur.execute(f"delete from employees where id={id}")
        self.conn.commit()
