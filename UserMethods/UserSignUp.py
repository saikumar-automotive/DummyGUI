import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

def signup():
    """
    Show sign-up window, create a folder under 'User Database'
    and write credentials. Returns True on success.
    """
    created = []

    def register():
        user = entry_user.get().strip()
        pw   = entry_pw.get().strip()
        base = Path(__file__).resolve().parents[1]
        user_dir = base / "User Database" / user

        if not user or not pw:
            messagebox.showwarning("Missing Data", "All fields are required")
            return

        if user_dir.exists():
            messagebox.showerror("Taken", f"Username '{user}' already exists")
            return

        user_dir.mkdir(parents=True, exist_ok=False)
        (user_dir / "User_Credentials.txt").write_text(pw)
        messagebox.showinfo("Success", f"User '{user}' created!")
        created.append(True)
        win.destroy()

    win = tk.Tk()
    win.title("Sign Up")
    win.geometry("300x200")

    ttk.Label(win, text="New Username:").pack(pady=5)
    entry_user = ttk.Entry(win); entry_user.pack()

    ttk.Label(win, text="New Password:").pack(pady=5)
    entry_pw = ttk.Entry(win, show="*"); entry_pw.pack()

    ttk.Button(win, text="Register", command=register).pack(pady=10)
    win.mainloop()

    return bool(created)
