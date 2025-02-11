import tkinter as tk
from tkinter import ttk, messagebox
from backend.database import login_user

class LoginUI(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ttk.Label(self, text="Login", font=("Arial", 20)).pack(pady=20)
      
      
        self.username_entry = ttk.Entry(self, width=30)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "Username")
        
        self.password_entry = ttk.Entry(self, width=30, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Password")
        
        ttk.Button(self, text="Login", command=self.login).pack(pady=10)
        ttk.Button(self, text="Register", command=controller.go_to_register).pack()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if login_user(username, password):
            self.controller.go_to_home(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")
