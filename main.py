import tkinter as tk
from gui.login_ui import LoginUI
from gui.register_ui import RegisterUI  # NEW
from gui.home_ui import HomeUI
from backend.database import initialize_database
from gui.chat_ui import ChatUI

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

# Dictionary to store frames
frames = {}

for F in (LoginUI, RegisterUI, HomeUI):  # ADD RegisterUI
    frame = F(container, root)
    frames[F.__name__] = frame
    frame.grid(row=0, column=0, sticky="nsew")

# Function to show frames
def show_frame(name):
    frames[name].tkraise()

root.show_frame = show_frame  # Attach function to root
show_frame("LoginUI")  # Show login screen by default

# Inside HomeUI or another suitable location:
chat_button = tk.Button(home_frame, text="Chat", font=("Arial", 14), bg="#2196F3", fg="white",
                        command=lambda: show_frame(chat_frame))
chat_button.pack(pady=10)

chat_frame = ChatUI(container, root, current_user, "friend_username")  # Replace with actual values
chat_frame.grid(row=0, column=0, sticky="nsew")

# Start the main loop
root.mainloop()
