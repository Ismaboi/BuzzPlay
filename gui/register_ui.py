import tkinter as tk
from tkinter import ttk, messagebox
from backend.database import register_user

class RegisterUI(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        container = ttk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(container, text="Register", font=("Arial", 20)).pack(pady=20)

        self.username_entry = ttk.Entry(container, width=30)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "Username")

        self.password_entry = ttk.Entry(container, width=30, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Password")

        ttk.Button(container, text="Register", command=self.register).pack(pady=10)
        ttk.Button(container, text="Back to Login", command=controller.go_to_login).pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if register_user(username, password):
            messagebox.showinfo("Success", "Registration successful!")
            self.controller.go_to_login()
        else:
            messagebox.showerror("Error", "Username already exists")
