import tkinter as tk
from tkinter import filedialog, messagebox

import importlib.util
import os


def main_app(guest_mode=False):
    def browse_file1():
        display_text = "Select File to be processed"
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            file1_var.set(file_path)

    def browse_file2():
        display_text = "Select Default File"
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            file2_var.set(file_path)

    def submit():
        file1 = file1_var.get()
        file2 = file2_var.get()
        if not file1 or not file2:
            messagebox.showwarning("Missing File", "Please select both Excel files.")
        else:
            print(f"File 1: {file1}")
            print(f"File 2: {file2}")
            messagebox.showinfo("Files Selected", f"File 1:\n{file1}\n\nFile 2:\n{file2}")
        try:
            module_path = os.path.join(os.path.dirname(__file__), "..", "MainFunction", "Start_File_Compare.py")
            spec = importlib.util.spec_from_file_location("Start_File_Compare", module_path)
            compare_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(compare_module)
               #Call the main function from Start_File_Compare
            if hasattr(compare_module, "run_comparison"):
                compare_module.run_comparison(file1, file2)
            else:
                messagebox.showerror("Function Missing", "The function 'run_comparison' was not found in Start_File_Compare.py.")
        except Exception as e:
            messagebox.showerror("Execution Error", f"An error occurred:\n{e}")


    root = tk.Tk()
    root.title("Excel File Selector")

    file1_var = tk.StringVar()
    file2_var = tk.StringVar()

    tk.Label(root, text="Select File to be processed").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(root, textvariable=file1_var, width=50).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=browse_file1).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="Select Default File").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(root, textvariable=file2_var, width=50).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=browse_file2).grid(row=1, column=2, padx=10, pady=10)

    tk.Button(root, text="Submit", command=submit).grid(row=2, column=1, pady=20)

    root.mainloop()
