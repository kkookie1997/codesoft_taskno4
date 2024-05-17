import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []

        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 10))

        # Labels and Entry Fields
        labels = ["Name:", "Phone:", "Email:", "Address:"]
        self.entry_vars = []
        for i, label_text in enumerate(labels):
            label = ttk.Label(master, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry_var = tk.StringVar()
            entry = ttk.Entry(master, textvariable=entry_var, width=30)
            entry.grid(row=i, column=1, columnspan=3, padx=5, pady=5, sticky="we")
            self.entry_vars.append(entry_var)

        # Buttons
        button_texts = ["Add Contact", "View Contacts", "Search Contact", "Update Contact", "Delete Contact"]
        button_commands = [self.add_contact, self.view_contacts, self.search_contact, self.update_contact, self.delete_contact]
        for i, (button_text, command) in enumerate(zip(button_texts, button_commands)):
            button = ttk.Button(master, text=button_text, command=command)
            button.grid(row=len(labels) + i, column=0, columnspan=4, padx=5, pady=5, sticky="we")

    def add_contact(self):
        name = self.entry_vars[0].get()
        phone = self.entry_vars[1].get()
        email = self.entry_vars[2].get()
        address = self.entry_vars[3].get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join(f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts)
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def search_contact(self):
        name = self.entry_vars[0].get()
        phone = self.entry_vars[1].get()

        if not name and not phone:
            messagebox.showerror("Error", "Please enter name or phone number to search.")
            return

        found_contacts = []
        for contact in self.contacts:
            if name and contact["Name"].lower() == name.lower():
                found_contacts.append(contact)
            elif phone and contact["Phone"] == phone:
                found_contacts.append(contact)

        if found_contacts:
            contact_list = "\n".join(f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts)
            messagebox.showinfo("Search Result", contact_list)
        else:
            messagebox.showinfo("Search Result", "No matching contacts found.")

    def update_contact(self):
        name = self.entry_vars[0].get()
        phone = self.entry_vars[1].get()

        if not name or not phone:
            messagebox.showerror("Error", "Please enter name and phone number to update.")
            return

        for contact in self.contacts:
            if contact["Name"].lower() == name.lower() and contact["Phone"] == phone:
                contact["Email"] = self.entry_vars[2].get()
                contact["Address"] = self.entry_vars[3].get()
                messagebox.showinfo("Success", "Contact updated successfully.")
                return

        messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.entry_vars[0].get()
        phone = self.entry_vars[1].get()

        if not name or not phone:
            messagebox.showerror("Error", "Please enter name and phone number to delete.")
            return

        for contact in self.contacts:
            if contact["Name"].lower() == name.lower() and contact["Phone"] == phone:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully.")
                return

        messagebox.showerror("Error", "Contact not found.")

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
