import tkinter as tk
from tkinter import messagebox
from backend.database import get_user

class LoginUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f0f0")
        self.controller = controller

        # 🟢 Configure the grid of the parent container to stretch
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 🟢 Main Frame (Perfectly Centered)
        self.center_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="solid", padx=20, pady=20)
        self.center_frame.grid(row=0, column=0, sticky="nsew")  # Make it stretch in both directions

        # 🟢 Title
        tk.Label(self.center_frame, text="BuzzPlay Login", font=("Arial", 20, "bold"), bg="#ffffff").pack(pady=10)

        # 🟢 Username
        tk.Label(self.center_frame, text="Username:", font=("Arial", 14), bg="#ffffff").pack(anchor="w")
        self.username_entry = tk.Entry(self.center_frame, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=5)

        # 🟢 Password
        tk.Label(self.center_frame, text="Password:", font=("Arial", 14), bg="#ffffff").pack(anchor="w")
        self.password_entry = tk.Entry(self.center_frame, font=("Arial", 14), width=30, show="*")
        self.password_entry.pack(pady=5)

        # 🟢 Login Button
        tk.Button(self.center_frame, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white",
                  command=self.login, width=25).pack(pady=10)

        # 🟢 Register Button
        tk.Button(self.center_frame, text="Register", font=("Arial", 14), bg="#2196F3", fg="white",
                  command=self.show_register, width=25).pack(pady=5)

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
