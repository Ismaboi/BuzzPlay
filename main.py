import tkinter as tk
from gui.login_ui import LoginUI
from gui.home_ui import HomeUI
from gui.register_ui import RegisterUI  # Import Register UI
from backend.database import initialize_database

# Initialize the database
initialize_database()

# Root window setup
class BuzzPlayApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("BuzzPlay")
        self.geometry("800x600")
        self.resizable(False, False)
        self.iconbitmap(r"assets/images/buzzplay_icon.ico")  # App icon

        # Set up container for frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Store frames

        for F in (LoginUI, RegisterUI, HomeUI):
            page_name = F.__name__.replace("UI", "").lower()
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = BuzzPlayApp()
    app.mainloop()
