import tkinter as tk

def main():
    root = tk.Tk()
    root.title("BuzzPlay")
    root.iconbitmap(r"assets/images/buzzplay_icon.ico")  #probleem solved using r

    root.geometry("800x600")
    root.mainloop()
    
if __name__=="__main__":
    main()