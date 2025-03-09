import json
import tkinter as tk
from tkinter import messagebox

TASKS_FILE = "tasks_data.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            task_data = json.load(file)
            return [{"task": t.get("task", ""), "done": t.get("done", False)} for t in task_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task_content = task_entry.get().strip()
    if task_content:
        tasks.append({"task": task_content, "done": False})
        save_tasks()
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a valid task!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for index, item in enumerate(tasks, start=1):
        status_icon = "✔" if item["done"] else "✖"
        task_listbox.insert(tk.END, f"{index}. {status_icon} {item['task']}")

def mark_completed():
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected]["done"] = True
        save_tasks()
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed.")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        del tasks[selected]
        save_tasks()
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def exit_app():
    root.quit()

tasks = load_tasks()

root = tk.Tk()
root.title("Task Manager")
root.geometry("450x500")
root.configure(bg="#121212")

title_label = tk.Label(root, text="Task Manager", font=("Helvetica", 18, "bold"), bg="#121212", fg="#ffffff")
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=45, font=("Helvetica", 12), bg="#333333", fg="#ffffff", insertbackground="#ffffff")
task_entry.pack(pady=10)

task_listbox = tk.Listbox(root, width=55, height=12, font=("Helvetica", 12), bg="#2e2e2e", fg="#ffffff", selectbackground="#00adb5")
task_listbox.pack(pady=10)
update_task_list()

button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", command=add_task, width=18, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Mark as Complete", command=mark_completed, width=18, bg="#2196F3", fg="#ffffff", font=("Helvetica", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Delete Task", command=delete_task, width=18, bg="#f44336", fg="#ffffff", font=("Helvetica", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Exit", command=exit_app, width=18, bg="#555555", fg="#ffffff", font=("Helvetica", 10, "bold")).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
