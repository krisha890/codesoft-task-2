import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("Contact Management System")

contacts = {}

def add_contact():
    name = simpledialog.askstring("Input", "Enter the contact name:")
    if name:
        phone = simpledialog.askstring("Input", "Enter the phone number:")
        email = simpledialog.askstring("Input", "Enter the email:")
        address = simpledialog.askstring("Input", "Enter the address:")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        update_contact_list()

def update_contact_list():
    listbox.delete(0, tk.END)
    for name, info in contacts.items():
        listbox.insert(tk.END, f"{name}: {info['phone']}")

def view_contact():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0]
        contact = contacts.get(name)
        if contact:
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")

def update_contact():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0]
        if name in contacts:
            phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contacts[name]["phone"])
            email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contacts[name]["email"])
            address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contacts[name]["address"])
            contacts[name] = {"phone": phone, "email": email, "address": address}
            update_contact_list()

def delete_contact():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0]
        if name in contacts:
            del contacts[name]
            update_contact_list()

def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number:")
    if search_term:
        found = False
        for name, info in contacts.items():
            if search_term.lower() in name.lower() or search_term in info['phone']:
                messagebox.showinfo("Search Result", f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
                found = True
                break
        if not found:
            messagebox.showinfo("Search Result", "No contact found")

frame = tk.Frame(root)
frame.pack(pady=10)

add_button = tk.Button(frame, text="Add the Contact", command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)

view_button = tk.Button(frame, text="View the Contact", command=view_contact)
view_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(frame, text="Update the Contact", command=update_contact)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Delete the Contact", command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(frame, text="Search the Contact", command=search_contact)
search_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

update_contact_list()

root.mainloop()