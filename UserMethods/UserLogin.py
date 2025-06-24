import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

def login():
    """
    Show login window, verify against User Database,
    return True if successful, False otherwise.
    """
    success = []

    def authenticate():
        user = entry_user.get().strip()
        pw   = entry_pw.get().strip()
        base = Path(__file__).resolve().parents[1]
        db   = base / "User Database" / user / "User_Credentials.txt"

        if not user or not pw:
            messagebox.showwarning("Missing Data", "Enter both username and password")
            return

        if not db.exists():
            messagebox.showerror("No Such User", f"User '{user}' not found.")
            return

        stored_pw = db.read_text().strip()
        if pw == stored_pw:
            success.append(True)
            win.destroy()
        else:
            messagebox.showerror("Login Failed", "Incorrect password")

    win = tk.Tk()
    win.title("Sign In")
    win.geometry("300x180")

    ttk.Label(win, text="Username:").pack(pady=5)
    entry_user = ttk.Entry(win); entry_user.pack()

    ttk.Label(win, text="Password:").pack(pady=5)
    entry_pw = ttk.Entry(win, show="*"); entry_pw.pack()

    ttk.Button(win, text="Login", command=authenticate).pack(pady=10)
    win.mainloop()

    return bool(success)
