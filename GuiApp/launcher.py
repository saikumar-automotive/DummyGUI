import tkinter as tk
from tkinter import ttk
from UserMethods.UserLogin import login
from UserMethods.UserSignUp import signup
from UserMethods.GuestUser import guest_login
from GuiApp.main_gui import main_app

def launch():
    root = tk.Tk()
    root.title("Welcome")
    root.geometry("300x200")
    ttk.Label(root, text="Please choose an option:", font=("Arial", 12)).pack(pady=10)

    def do_signin():
        if login():
            root.destroy()
            main_app(guest_mode=False)

    def do_signup():
        if signup():
            # after signup, send them to sign‐in 
            do_signin()

    def do_guest():
        if guest_login():
            root.destroy()
            main_app(guest_mode=True)

    ttk.Button(root, text="Sign In",    command=do_signin).pack(fill='x', padx=50, pady=5)
    ttk.Button(root, text="Sign Up",    command=do_signup).pack(fill='x', padx=50, pady=5)
    ttk.Button(root, text="Guest Login",command=do_guest).pack(fill='x', padx=50, pady=5)

    root.mainloop()

if __name__ == "__main__":
    launch()
