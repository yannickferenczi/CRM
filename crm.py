from tkinter import *
import sqlite3

from contact import Contact

class CRM:
    def __init__(self) -> None:
        self.search = "all"
        self.root = Tk()
        self.root.title("CRM")
        self.root.geometry("1250x600")
        self.root.configure(bg="#88CCFF")
        
        self.settings_frame = LabelFrame(self.root, text="Options")
        self.settings_frame.pack()
        self.research_label = Label(self.settings_frame, text="Search : ")
        self.research_label.grid(row=0, column=0)

        self.contact_frame = LabelFrame(self.root, text=self.search, bg="#FF88FF")
        self.contact_frame.pack()

        self.display_contact()


        self.root.mainloop()
    
    def display_contact(self):
        # Create the header of the display
        first_name_header = Label(self.contact_frame, text="First name", bg="#FF88FF", width=15)
        first_name_header.grid(row=0, column=0)
        family_name_header = Label(self.contact_frame, text="Family name", bg="#FF88FF", width=15)
        family_name_header.grid(row=0, column=1)
        address_header = Label(self.contact_frame, text="Address", bg="#FF88FF", width=45)
        address_header.grid(row=0, column=2)
        phone_number_header = Label(self.contact_frame, text="Phone number", bg="#FF88FF", width=15)
        phone_number_header.grid(row=0, column=3)
        email_address_header = Label(self.contact_frame, text="Email", bg="#FF88FF", width=45)
        email_address_header.grid(row=0, column=4)
        space_for_icones = Label(self.contact_frame, bg="#FF88FF", width=5)
        space_for_icones.grid(row=0, column=5, columnspan=2)

        # For each contact in DB, create an instance of Contact and store it in a dictionnary
        dict_of_contacts = {}

        self.sql_conn = sqlite3.connect("contact_data.db")
        self.curs = self.sql_conn.cursor()

        row_number = 1
        for row in self.curs.execute("SELECT * FROM contacts"):
            dict_of_contacts[str(row_number)] = Contact(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row_number)
            row_number += 1
        self.sql_conn.close()

        # Display the Contact instances 
        for personne in dict_of_contacts.values():
            personne.pack_in_tk_frame(self.contact_frame, row_number)


if __name__ == "__main__":
    mainwindow = CRM()