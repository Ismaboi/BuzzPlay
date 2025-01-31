import tkinter as tk
from tkinter import messagebox
from backend.database import save_user

class RegisterUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#e8f5e9")

        tk.Label(self, text="BuzzPlay Registration", font=("Arial", 24), bg="#e8f5e9").pack(pady=30)

        tk.Label(self, text="Username:", font=("Arial", 14), bg="#e8f5e9").pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=("Arial", 14), bg="#e8f5e9").pack(pady=5)
        self.password_entry = tk.Entry(self, font=("Arial", 14), show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Register", font=("Arial", 14), bg="#4caf50", fg="white", command=self.register).pack(pady=10)
        tk.Button(self, text="Back to Login", font=("Arial", 14), bg="#f44336", fg="white", command=self.show_login).pack(pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            save_user(username, password)
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login()  # Go back to login screen
        except ValueError:
            messagebox.showerror("Registration Error", "Username already exists!")

    def show_login(self):
        self.controller.show_frame("LoginUI")  # Go back to login screen
