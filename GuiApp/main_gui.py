import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class DateSelectorApp:
    def __init__(self, root, guest_mode=False):
        self.guest_mode = guest_mode
        self.root = root
        self.root.title("Server Tool")
        self.root.geometry("400x330")
        self.build_ui()

    def build_ui(self):
        pad = dict(pady=5)
        ttk.Label(self.root, text="Category A:").pack(**pad)
        self.dropdown_a = ttk.Combobox(
            self.root,
            values=["A1", "A2", "A3"],
            state="readonly"
        )
        self.dropdown_a.pack(**pad)

        if not self.guest_mode:
            ttk.Label(self.root, text="Category B:").pack(**pad)
            self.dropdown_b = ttk.Combobox(
                self.root,
                values=["B1", "B2", "B3"],
                state="readonly"
            )
            self.dropdown_b.pack(**pad)

        ttk.Label(self.root, text="Start Date:").pack(**pad)
        self.start = DateEntry(self.root); self.start.pack(**pad)

        ttk.Label(self.root, text="End Date:").pack(**pad)
        self.end = DateEntry(self.root); self.end.pack(**pad)

        ttk.Button(self.root, text="Submit", command=self.submit).pack(pady=15)

    def submit(self):
        print("Guest Mode:", self.guest_mode)
        print("Category A:", self.dropdown_a.get())
        if not self.guest_mode:
            print("Category B:", self.dropdown_b.get())
        print("Date Range:", self.start.get_date(), "→", self.end.get_date())
        # here you’d hook into your server‐call logic

def main_app(guest_mode=False):
    root = tk.Tk()
    DateSelectorApp(root, guest_mode)
    root.mainloop()
