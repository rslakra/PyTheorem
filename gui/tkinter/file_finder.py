#
# Author: Rohtash Lakra
#
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext


def find_files():
    search_term = entry_search.get()
    start_directory = filedialog.askdirectory()  # User selects starting directory

    if not start_directory or not search_term:
        return

    results_text.delete(1.0, tk.END)  # Clear previous results

    for root, _, files in os.walk(start_directory):
        for file in files:
            if search_term.lower() in file.lower():
                full_path = os.path.join(root, file)
                results_text.insert(tk.END, f"{full_path}\n")


# Create the main window
root = tk.Tk()
root.title("Python File Finder")

# Search input
label_search = tk.Label(root, text="Search for:")
label_search.pack(pady=5)
entry_search = tk.Entry(root, width=50)
entry_search.pack(pady=5)

# Search button
button_find = tk.Button(root, text="Find Files", command=find_files)
button_find.pack(pady=10)

# Results display
results_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
results_text.pack(pady=10)

# Run the application
root.mainloop()
