import tkinter as tk
from tkinter import messagebox
from backend.database import get_user

class LoginUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f0f0")
        self.controller = controller

        # Centering Frame
        center_frame = tk.Frame(self, bg="#f0f0f0")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centers UI

        # Title
        tk.Label(center_frame, text="BuzzPlay Login", font=("Arial", 24, "bold"), bg="#f0f0f0").pack(pady=20)

        # Username Entry
        tk.Label(center_frame, text="Username:", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w", padx=10)
        self.username_entry = tk.Entry(center_frame, font=("Arial", 14), width=25)
        self.username_entry.pack(pady=5, padx=10)

        # Password Entry
        tk.Label(center_frame, text="Password:", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w", padx=10)
        self.password_entry = tk.Entry(center_frame, font=("Arial", 14), width=25, show="*")
        self.password_entry.pack(pady=5, padx=10)

        # Login Button
        tk.Button(center_frame, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white",
                  command=self.login, width=20).pack(pady=10)

        # Register Button
        tk.Button(center_frame, text="Register", font=("Arial", 14), bg="#2196F3", fg="white",
                  command=self.show_register, width=20).pack(pady=5)

    def login(self):
        """Handle user login."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        user = get_user(username)

        if user and user[2] == password:  # user[2] is the password from the DB
            self.controller.show_frame("HomeUI")  # Navigate to Home
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def show_register(self):
        """Navigate to the Register screen."""
        self.controller.show_frame("RegisterUI")
