from tkinter import *

class Contact:
    def __init__(self, first_name, family_name, street, postcode, city, phone_number, email_address, row_number):
        self.first_name = first_name.capitalize()
        self.family_name = family_name.upper()
        self.street = street
        self.postcode = postcode
        self.city = city.capitalize()
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = f"{self.street}, {self.postcode} {self.city}"
        self.row_number = row_number

    def pack_in_tk_frame(self, master_frame, row_number):
        background = "#8866AA" if self.row_number % 2 == 0 else "#AA88CC"
        row_frame = Frame(master_frame, bg=background)
        row_frame.grid(row=self.row_number, column=0, columnspan=5)
        first_name = Label(row_frame, text=self.first_name, bg=background, width=15, anchor="w")
        first_name.grid(row=self.row_number, column=0)
        family_name = Label(row_frame, text=self.family_name, bg=background, width=15, anchor="w")
        family_name.grid(row=self.row_number, column=1)
        address = Label(row_frame, text=self.address, bg=background, width=45, anchor="w")
        address.grid(row=row_number, column=2)
        phone_number = Label(row_frame, text=self.phone_number, bg=background, width=15, anchor="w")
        phone_number.grid(row=self.row_number, column=3)
        email_address = Label(row_frame, text=self.email_address, bg=background, width=45, anchor="w")
        email_address.grid(row=self.row_number, column=4)
        
        modification_icone = PhotoImage(file="modification.png")
        modification_button = Button(master_frame, image=modification_icone, bg="#EEEEEE", width=30, command=self.contact_modification)
        modification_button.grid(row=self.row_number, column=5, padx=5)

        delete_icone = PhotoImage(file="trash.png")
        delete_button = Button(master_frame, image=delete_icone, bg="#EEEEEE", width=30, command=self.delete_contact)
        delete_button.grid(row=self.row_number, column=6, padx=5)

    def contact_modification(self):
        pass

    def delete_contact(self):
        pass
