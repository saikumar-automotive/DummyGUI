import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

def login():
    """
    Show login window, verify against User Database,
    return True if successful, False otherwise.
    """
    print("Entered Login Section")
    success = []

    def authenticate():
        print("entered authenticate function")
        user = entry_user.get().strip()
        pw   = entry_pw.get().strip()
        base = Path(__file__).resolve().parents[1]
        db   = base / "User Database" / user / "User_Credentials.txt"
        
  
        print(f"Checking credentials for user: {user}")
        print(f"Password entered: {pw}")
        print(f"Database path: {db}")

        if db.exists():
            print(f"Database file exists: {db}")
            print(f"Database file content: {db.read_text().strip()}")
        else:
            print(f"Database file does not exist: {db}")
        
        if not user or not pw:
            print("Username or password is empty")
            messagebox.showwarning("Missing Data", "Enter both username and password")
            return

        if not db.exists():
            messagebox.showerror("No Such User", f"User '{user}' not found.")
            return

        if db.exists() and not db.is_file():
            messagebox.showerror("Invalid Database", "User credentials file is not valid.")
            return
        
        stored_pw = db.read_text().strip()
        print(f"Stored password for user '{user}': {stored_pw}")
        if pw == stored_pw:
            print("Password matches stored password")
            success.append(True)
            messagebox.showinfo("Login Successful", "Welcome back!")
            
        else:
            messagebox.showerror("Login Failed", "Incorrect password")

        win.destroy()

    win = tk.Tk()
    win.title("Sign In")
    win.geometry("300x180")

    ttk.Label(win, text="Username:").pack(pady=5)
    entry_user = ttk.Entry(win); entry_user.pack()

    ttk.Label(win, text="Password:").pack(pady=5)
    entry_pw = ttk.Entry(win, show="*"); entry_pw.pack()

    ttk.Button(win, text="Login", command=authenticate).pack(pady=10)
    win.mainloop()
    print("I am at the end of the login function")
    # Return True if login was successful, False otherwisewise
    return bool(success)


