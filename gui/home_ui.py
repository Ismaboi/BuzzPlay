import tkinter as tk

class HomeUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller

        # Prevent shrinking
        self.pack_propagate(False)

        # Welcome text
        tk.Label(self, text="Welcome to BuzzPlay!", font=("Arial", 24), bg="#ffffff").pack(pady=20)

        # ✅ Frame to hold buttons
        button_frame = tk.Frame(self, bg="#ffffff")
        button_frame.pack(pady=20, fill="both", expand=True)

        # ✅ Games Button
        tk.Button(button_frame, text="Games", font=("Arial", 14), bg="#4CAF50", fg="white",
                  command=self.open_games, width=20).pack(pady=5, fill="x")

        # ✅ Chat Button
        tk.Button(button_frame, text="Chat", font=("Arial", 14), bg="#2196F3", fg="white",
                  command=self.open_chat, width=20).pack(pady=5, fill="x")

        # ✅ Friends Button
        tk.Button(button_frame, text="Friends", font=("Arial", 14), bg="#FF9800", fg="white",
                  command=self.open_friends, width=20).pack(pady=5, fill="x")

        # ✅ Logout Button
        tk.Button(button_frame, text="Logout", font=("Arial", 14), bg="#f44336", fg="white",
                  command=lambda: controller.show_frame("LoginUI"), width=20).pack(pady=5, fill="x")

    def open_games(self):
        print("Games button clicked!")  # Replace with actual navigation when ready

    def open_chat(self):
        print("Chat button clicked!")  # Replace with actual navigation when ready

    def open_friends(self):
        print("Friends button clicked!")  # Replace with actual navigation when ready
