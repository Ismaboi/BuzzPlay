import sys
import tkinter as tk
from tkinter import ttk
from gui.login_ui import LoginUI
from gui.register_ui import RegisterUI
from gui.home_ui import HomeUI

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("BuzzPlay")
        self.state("zoomed")  # Make the window fullscreen
        
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.frames = {}
        for F in (LoginUI, RegisterUI, HomeUI):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("LoginUI")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def go_to_register(self):
        self.show_frame("RegisterUI")
    
    def go_to_login(self):
        self.show_frame("LoginUI")
    
    def go_to_home(self, username):
        self.frames["HomeUI"].set_user(username)
        self.show_frame("HomeUI")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
