import tkinter as tk
from tkinter import messagebox
from gui.login_ui import LoginUI
from gui.register_ui import RegisterUI
from gui.home_ui import HomeUI
from backend.database import initialize_database


class BuzzPlayApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BuzzPlay")
        self.geometry("1920x1080")
        self.frames = {}  # Dictionary to store frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.iconbitmap("assets/images/buzzplay_icon.ico")

        # Initialize Database
        initialize_database()

        # 🟢 Configure grid to allow resizing and stretching of frames
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add all frames to the container and set to expand
        for F in (LoginUI, RegisterUI, HomeUI):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginUI")  # Start with Login Page

    def show_frame(self, page_name):
        """Show a frame by name."""
        frame = self.frames.get(page_name)
        if frame:
            frame.tkraise()
        else:
            print(f"Error: Frame '{page_name}' not found!")

    def get_frame(self, page_name):
        """Retrieve a frame by name."""
        return self.frames.get(page_name)


if __name__ == "__main__":
    app = BuzzPlayApp()
    app.mainloop()
