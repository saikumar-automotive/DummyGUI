
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
# This line ensures that the parent directory of the current file is added to the system path
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
       
        print("Launcher window closed, proceeding to sign in...")
        print("Attempting login...")
        root.destroy()
     
        if login():
            #if not root.destroyed():
            #    root.destroy()  # Close the launcher window
            # If login is successful, close the login window and launch the main app
            print("Login successful. Launching main app...")
            main_app(guest_mode=False)

        
        else:
            print("Login failed.")

        


    def do_signup():
        root.destroy()
        
        if signup():
            # after signup, send them to sign‐in 
            print("Sign up successful. Redirecting to sign in...")

        if login():
           
            print("Login successful. Launching main app...")
            main_app(guest_mode=False)

            

    def do_guest():
        if guest_login():
            # Destroy the launcher window before launching the main app in guest mode
            root.destroy()
            main_app(guest_mode=True)

    ttk.Button(root, text="Sign In",    command=do_signin).pack(fill='x', padx=50, pady=5)
    ttk.Button(root, text="Sign Up",    command=do_signup).pack(fill='x', padx=50, pady=5)
    ttk.Button(root, text="Guest Login",command=do_guest).pack(fill='x', padx=50, pady=5)

    root.mainloop()

if __name__ == "__main__":
    launch()
