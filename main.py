import tkinter as tk
from gui.login_ui import LoginUI
from gui.home_ui import HomeUI
from backend.database import initialize_database

# Initialize the database
initialize_database()

# Root window setup
root = tk.Tk()
root.title("BuzzPlay")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap(r"assets/images/buzzplay_icon.ico")  # App icon

# Set up the container for all frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Configure rows and columns to stack frames
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Initialize frames
login_frame = LoginUI(container, root)  # Login screen
home_frame = HomeUI(container, root)    # Home screen

# Add frames to the container
login_frame.grid(row=0, column=0, sticky="nsew")
home_frame.grid(row=0, column=0, sticky="nsew")

# Show the login screen by default
login_frame.tkraise()

# Start the main loop
root.mainloop()
