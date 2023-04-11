import sqlite3
import pandas as pd
from typing import Optional

class Database:
    def __init__(self) -> None:
        super().__init__()
        self.db = "mytable.db"
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
        """create the table within the init method"""
        self.cur.execute(
            """CREATE TABLE  IF NOT EXISTS employees (
                id Integer Primary Key,
                name String,
                age float,
                doj String,
                email String,
                gender String,
                contact String,
                address String)""")

    def insert(self,name:str,age:float,doj:str,email:str,gender:str,contact:Optional[str],address:Optional[str] = ""):
        self.cur.execute("""INSERT INTO employees VALUES (NULL,?,?,?,?,?,?,?)""",(name, age, doj, email, gender, contact, address))
        self.conn.commit()

    def fetch(self,id:int):
        self.cur.execute(f"SELECT * FROM employees WHERE id={id}")
        self.conn.commit()

    def update(self,id,name:str,age:float,doj:str,email:str,gender:str,contact:Optional[str],address:Optional[str] = ""):
        self.cur.execute("UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",(name, age, doj, email, gender, contact, address, id))
        self.conn.commit()

    def delete(self,id):
        """delete a record in the database"""
        self.cur.execute(f"delete from employees where id={id}")
        self.conn.commit()
