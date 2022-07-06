from tkinter import *
import sqlite3
from turtle import bgcolor


class CRM:
    def __init__(self) -> None:
        self.search = "all"
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.configure(bg="#88CCFF")
        
        self.contact_frame = LabelFrame(self.root, text=self.search)
        self.contact_frame.pack()

        self.display_contact()


        self.root.mainloop()
    
    def display_contact(self):
        self.sql_conn = sqlite3.connect("contact_data.db")
        self.curs = self.sql_conn.cursor()
        first_name_header = Label(self.contact_frame, text="First name")
        first_name_header.grid(row=0, column=0)
        family_name_header = Label(self.contact_frame, text="Family name")
        family_name_header.grid(row=0, column=1)
        address_header = Label(self.contact_frame, text="Address")
        address_header.grid(row=0, column=2)
        phone_number_header = Label(self.contact_frame, text="Phone number")
        phone_number_header.grid(row=0, column=3)
        email_address_header = Label(self.contact_frame, text="Email")
        email_address_header.grid(row=0, column=4)

        row_number = 1
        background = "#8866AA" if row_number % 2 == 0 else "#AA88CC"
        for row in self.curs.execute("SELECT * FROM contacts"):
            row_frame = Frame(self.contact_frame, bg=background)
            row_frame.grid(row=row_number, column=0, columnspan=5)
            first_name = Label(self.contact_frame, text=row[0], bg=background)
            first_name.grid(row=row_number, column=0)
            family_name = Label(self.contact_frame, text=row[1], bg=background)
            family_name.grid(row=row_number, column=1)
            address = Label(self.contact_frame, text=f"{row[2]}, {row[3]} {row[4]}", bg=background)
            address.grid(row=row_number, column=2)
            phone_number = Label(self.contact_frame, text=row[5], bg=background)
            phone_number.grid(row=row_number, column=3)
            email_address = Label(self.contact_frame, text=row[6], bg=background)
            email_address.grid(row=row_number, column=4)

            row_number += 1
        self.sql_conn.close()



if __name__ == "__main__":
    mainwindow = CRM()