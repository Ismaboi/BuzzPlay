import customtkinter

class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BuzzPlay")
        self.geometry("800x600")  # You can change this to fit your needs
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Title Label
        self.title_label = customtkinter.CTkLabel(self, text="BuzzPlay", font=("Arial", 30, "bold"))
        self.title_label.grid(row=0, column=0, pady=20, sticky="n")

        # Login Button
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.open_login, width=200, height=50)
        self.login_button.grid(row=1, column=0, pady=10, padx=20)

        # Register Button
        self.register_button = customtkinter.CTkButton(self, text="Register", command=self.open_register, width=200, height=50)
        self.register_button.grid(row=2, column=0, pady=10, padx=20)

    def open_login(self):
        print("Opening Login Page...")
        

    def open_register(self):
        print("Opening Register Page...")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
