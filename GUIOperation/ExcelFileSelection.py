
import tkinter as tk
from tkinter import filedialog

def select_file1():
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
if file_path:
file1_var.set(file_path)

def select_file2():
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
if file_path:
ile2_var.set(file_path)

# Create the main window
root = tk.Tk()
root.title("Select Two Excel Files")
root.geometry("500x200")

# Variables to store file paths
file1_var = tk.StringVar()
file2_var = tk.StringVar()

# File 1 selection
tk.Label(root, text="Select Excel File 1:").pack(pady=5)
tk.Entry(root, textvariable=file1_var, width=60).pack()
tk.Button(root, text="Browse", command=select_file1).pack(pady=5)

# File 2 selection
tk.Label(root, text="Select Excel File 2:").pack(pady=5)
tk.Entry(root, textvariable=file2_var, width=60).pack()
tk.Button(root, text="Browse", command=select_file2).pack(pady=5)

# Run the GUI loop
root.mainloop()
