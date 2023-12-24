import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Task list
        self.tasks = []

        # GUI components
        self.task_entry = tk.Entry(root, width=30)
        self.priority_entry = tk.Entry(root, width=10)
        self.due_date_entry = tk.Entry(root, width=15)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)
        self.task_listbox.bind('<Double-Button-1>', self.show_task_details)

        # Labels
        tk.Label(root, text="Task:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        tk.Label(root, text="Priority:").grid(row=0, column=1, padx=5, pady=5, sticky='e')
        tk.Label(root, text="Due Date:").grid(row=0, column=2, padx=5, pady=5, sticky='e')

        # Entries
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        self.priority_entry.grid(row=0, column=1, padx=5, pady=5)
        self.due_date_entry.grid(row=0, column=2, padx=5, pady=5)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task).grid(row=1, column=0, columnspan=3, pady=10)
        tk.Button(root, text="Delete Task", command=self.delete_task).grid(row=2, column=0, columnspan=3, pady=5)
        tk.Button(root, text="Exit", command=root.destroy).grid(row=3, column=0, columnspan=3, pady=10)

        # Listbox
        self.task_listbox.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

    def add_task(self):
        task_text = self.task_entry.get()
        priority_text = self.priority_entry.get()
        due_date_text = self.due_date_entry.get()

        if task_text:
            task_details = f"Priority: {priority_text}, Due Date: {due_date_text}"
            self.tasks.append((task_text, task_details))
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task, details in self.tasks:
            self.task_listbox.insert(tk.END, f"{task} - {details}")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_list()

    def show_task_details(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task, details = self.tasks[selected_index[0]]
            messagebox.showinfo("Task Details", f"Task: {task}\nDetails: {details}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
