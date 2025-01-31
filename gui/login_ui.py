import tkinter as tk
from tkinter import messagebox
from backend.database import get_user

class LoginUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="BuzzPlay Login", font=("Arial", 24), bg="#f0f0f0").pack(pady=30)

        tk.Label(self, text="Username:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        self.password_entry = tk.Entry(self, font=("Arial", 14), show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", font=("Arial", 14), bg="#4caf50", fg="white", command=self.login).pack(pady=10)
        tk.Button(self, text="Register", font=("Arial", 14), bg="#2196f3", fg="white", command=self.show_register).pack(pady=10)  # NEW BUTTON

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = get_user(username)
        
        if user and user[2] == password:  # user[2] is the password column in the database
            self.controller.show_frame("HomeUI")  # Navigate to home screen
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def show_register(self):
        self.controller.show_frame("RegisterUI")  # Navigate to registration screen
