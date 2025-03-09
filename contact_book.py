import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

def setup_database():
    with sqlite3.connect("contacts_data.db") as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            phone TEXT UNIQUE NOT NULL,
                            email TEXT,
                            address TEXT)''')
        db.commit()

def add_new_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    phone = simpledialog.askstring("Add Contact", "Enter Phone:")
    email = simpledialog.askstring("Add Contact", "Enter Email (Optional):")
    address = simpledialog.askstring("Add Contact", "Enter Address (Optional):")

    if not name or not phone:
        messagebox.showwarning("Warning", "Name and Phone Number are required!")
        return

    try:
        with sqlite3.connect("contacts_data.db") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                           (name, phone, email, address))
            db.commit()
        messagebox.showinfo("Success", "Contact Added Successfully!")
        display_contacts()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Phone number already exists!")

def display_contacts():
    contact_listbox.delete(0, tk.END)
    with sqlite3.connect("contacts_data.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, name, phone FROM contacts ORDER BY name")
        for row in cursor.fetchall():
            contact_listbox.insert(tk.END, f"{row[0]} - {row[1]} 📞 {row[2]}")

def search_contact():
    search_term = simpledialog.askstring("Search Contact", "Enter Name or Phone:")
    if search_term:
        contact_listbox.delete(0, tk.END)
        with sqlite3.connect("contacts_data.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                           (f"%{search_term}%", f"%{search_term}%"))
            results = cursor.fetchall()

        if results:
            for contact in results:
                contact_listbox.insert(tk.END, f"{contact[0]} - {contact[1]} 📞 {contact[2]}")
        else:
            messagebox.showinfo("No Results", "No matching contact found!")

def modify_contact():
    selected_item = contact_listbox.curselection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a contact to update!")
        return

    contact_id = contact_listbox.get(selected_item[0]).split(" - ")[0]
    new_phone = simpledialog.askstring("Update Contact", "Enter new phone number:")
    if new_phone:
        with sqlite3.connect("contacts_data.db") as db:
            cursor = db.cursor()
            cursor.execute("UPDATE contacts SET phone = ? WHERE id = ?", (new_phone, contact_id))
            db.commit()
        messagebox.showinfo("Success", "Contact Updated Successfully!")
        display_contacts()

def remove_contact():
    selected_item = contact_listbox.curselection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a contact to delete!")
        return

    contact_id = contact_listbox.get(selected_item[0]).split(" - ")[0]
    with sqlite3.connect("contacts_data.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        db.commit()
    messagebox.showinfo("Success", "Contact Removed Successfully!")
    display_contacts()

def switch_theme():
    global is_dark
    if is_dark:
        root.config(bg="white")
        contact_listbox.config(bg="white", fg="black")
        theme_button.config(text="🌙 Dark Mode")
    else:
        root.config(bg="black")
        contact_listbox.config(bg="gray20", fg="white")
        theme_button.config(text="☀️ Light Mode")
    is_dark = not is_dark

root = tk.Tk()
root.title("📇 Contact Manager")
root.geometry("420x460")

is_dark = False

theme_button = tk.Button(root, text="🌙 Dark Mode", command=switch_theme)
theme_button.pack()

contact_listbox = tk.Listbox(root, width=50)
contact_listbox.pack(pady=10)

tk.Button(root, text="➕ Add Contact", command=add_new_contact).pack()
tk.Button(root, text="📜 View Contacts", command=display_contacts).pack()
tk.Button(root, text="🔍 Search Contact", command=search_contact).pack()
tk.Button(root, text="✏️ Update Contact", command=modify_contact).pack()
tk.Button(root, text="❌ Delete Contact", command=remove_contact).pack()

setup_database()
display_contacts()

root.mainloop()
