import tkinter as tk
from tkinter import ttk

class HomeUI(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        container = ttk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        self.username_label = ttk.Label(container, text="Welcome, ", font=("Arial", 20))
        self.username_label.pack(pady=20)
        
        ttk.Button(container, text="Games", command=self.show_games).pack(pady=5)
        ttk.Button(container, text="Chat", command=self.show_chat).pack(pady=5)
        ttk.Button(container, text="Friends", command=self.show_friends).pack(pady=5)
        ttk.Button(container, text="Logout", command=self.controller.go_to_login).pack(pady=10)
        
    def set_user(self, username):
        self.username_label.config(text=f"Welcome, {username}")
    
    def show_games(self):
        print("Games section")
    
    def show_chat(self):
        print("Chat section")
    
    def show_friends(self):
        print("Friends section")
