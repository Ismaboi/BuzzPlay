import tkinter as tk
from tkinter import messagebox
import os

# File to store user data
USER_DATA_FILE = "users.txt"

# Helper function to load user data
def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r") as file:
        lines = file.readlines()
        return {line.split(",")[0]: line.split(",")[1].strip() for line in lines}

# Helper function to save user data
def save_user(username, password):
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username},{password}\n")

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

# Login functionality
def login():
    username = username_entry.get()
    password = password_entry.get()
    users = load_users()
    if username in users and users[username] == password:
        show_frame(home_frame)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Registration functionality
def register():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    confirm_password = reg_confirm_password_entry.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    if password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match!")
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Registration Error", "Username already exists!")
        return

    save_user(username, password)
    messagebox.showinfo("Success", "Registration successful!")
    show_frame(login_frame)

# Root window setup
root = tk.Tk()
root.title("BuzzPlay")
root.geometry("800x600")
root.resizable(False, False)

# Set the app icon
root.iconbitmap(r"assets/images/buzzplay_icon.ico")  # Path to your icon file

# Set up the container for all frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Configure rows and columns to stack frames
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Initialize frames
login_frame = tk.Frame(container, bg="#f0f0f0")
register_frame = tk.Frame(container, bg="#e8f5e9")
home_frame = tk.Frame(container, bg="#ffffff")

# Add frames to the container
for frame in (login_frame, register_frame, home_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# --- Login Screen ---
tk.Label(login_frame, text="BuzzPlay Login", font=("Arial", 24), bg="#f0f0f0").pack(pady=30)
tk.Label(login_frame, text="Username:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
username_entry = tk.Entry(login_frame, font=("Arial", 14))
username_entry.pack(pady=5)
tk.Label(login_frame, text="Password:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
password_entry = tk.Entry(login_frame, font=("Arial", 14), show="*")
password_entry.pack(pady=5)
tk.Button(login_frame, text="Login", font=("Arial", 14), bg="#4caf50", fg="white", command=login).pack(pady=10)
tk.Button(login_frame, text="Register", font=("Arial", 14), bg="#2196f3", fg="white", command=lambda: show_frame(register_frame)).pack(pady=10)

# --- Registration Screen ---
tk.Label(register_frame, text="BuzzPlay Registration", font=("Arial", 24), bg="#e8f5e9").pack(pady=30)
tk.Label(register_frame, text="Username:", font=("Arial", 14), bg="#e8f5e9").pack(pady=5)
reg_username_entry = tk.Entry(register_frame, font=("Arial", 14))
reg_username_entry.pack(pady=5)
tk.Label(register_frame, text="Password:", font=("Arial", 14), bg="#e8f5e9").pack(pady=5)
reg_password_entry = tk.Entry(register_frame, font=("Arial", 14), show="*")
reg_password_entry.pack(pady=5)
tk.Label(register_frame, text="Confirm Password:", font=("Arial", 14), bg="#e8f5e9").pack(pady=5)
reg_confirm_password_entry = tk.Entry(register_frame, font=("Arial", 14), show="*")
reg_confirm_password_entry.pack(pady=5)
tk.Button(register_frame, text="Register", font=("Arial", 14), bg="#4caf50", fg="white", command=register).pack(pady=10)
tk.Button(register_frame, text="Back to Login", font=("Arial", 14), bg="#f44336", fg="white", command=lambda: show_frame(login_frame)).pack(pady=10)

# --- Home Screen ---
tk.Label(home_frame, text="Welcome to BuzzPlay!", font=("Arial", 24), bg="#ffffff").pack(pady=30)
tk.Button(home_frame, text="Logout", font=("Arial", 14), bg="#f44336", fg="white", command=lambda: show_frame(login_frame)).pack(pady=10)

# Show the login screen by default
show_frame(login_frame)

# Start the main loop
root.mainloop()
