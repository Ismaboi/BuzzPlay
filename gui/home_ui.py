import tkinter as tk


class HomeUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")

        # Home Screen Layout
        tk.Label(self, text="Welcome to BuzzPlay!", font=("Arial", 24), bg="#ffffff").pack(pady=30)
        tk.Button(self, text="Logout", font=("Arial", 14), bg="#f44336", fg="white",
                  command=lambda: controller.children['!loginui'].tkraise()).pack(pady=10)
