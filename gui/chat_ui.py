import tkinter as tk
from tkinter import scrolledtext
from backend.database import send_message, get_messages

class ChatUI(tk.Frame):
    def __init__(self, parent, root, sender, receiver):
        super().__init__(parent)
        self.root = root
        self.sender = sender
        self.receiver = receiver

        self.configure(bg="white")

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
        self.chat_display.pack(pady=10)

        # Input field
        self.message_entry = tk.Entry(self, font=("Arial", 12), width=40)
        self.message_entry.pack(side=tk.LEFT, padx=5, pady=10)

        # Send button
        self.send_button = tk.Button(self, text="Send", font=("Arial", 12), bg="#4CAF50", fg="white",
                                     command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=5, pady=10)

        # Load previous messages
        self.load_messages()

    def load_messages(self):
        """Load previous messages between sender and receiver."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete("1.0", tk.END)

        messages = get_messages(self.sender, self.receiver)
        for sender, message, timestamp in messages:
            self.chat_display.insert(tk.END, f"{sender}: {message} ({timestamp})\n")

        self.chat_display.config(state=tk.DISABLED)

    def send_message(self):
        """Send a message and update the chat window."""
        message = self.message_entry.get()
        if message:
            send_message(self.sender, self.receiver, message)
            self.message_entry.delete(0, tk.END)
            self.load_messages()  # Refresh chat
