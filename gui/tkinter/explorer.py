#
# Author: Rohtash Lakra
#
import os
import tkinter as tk
from tkinter import ttk


class FinderLikeExplorer:

    def __init__(self, master):
        self.master = master
        master.title("Python File Explorer")
        master.geometry("800x600")
        self.home_dir = "~/Downloads"
        self.current_path = os.path.expanduser(self.home_dir)

        # Create main frames
        self.sidebar_frame = tk.Frame(master, width=200, bg="lightgray", relief="raised")
        self.sidebar_frame.pack(side="left", fill="y")

        self.main_content_frame = tk.Frame(master, bg="white")
        self.main_content_frame.pack(side="right", fill="both", expand=True)

        # Sidebar content (simplified)
        self.home_button = tk.Button(self.sidebar_frame, text="Home",
                                     command=lambda: self.display_directory(self.current_path))
        self.home_button.pack(pady=5, padx=10, anchor="w")

        # Main content area (using Treeview for list-like display)
        self.tree = ttk.Treeview(self.main_content_frame, columns=("Type", "Size"), show="headings")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Size", text="Size")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", self.on_item_double_click)

        # self.current_path = os.path.expanduser(self.home_dir)
        self.display_directory(self.current_path)

    def display_directory(self, path):
        self.current_path = path
        self.tree.delete(*self.tree.get_children())  # Clear existing items
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    self.tree.insert("", "end", text=item, values=("Folder", ""))
                else:
                    size = os.path.getsize(full_path)
                    self.tree.insert("", "end", text=item, values=("File", f"{size} bytes"))
        except PermissionError:
            print(f"Permission denied to access: {path}")

    def on_item_double_click(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            item_text = self.tree.item(selected_item, "text")
            full_path = os.path.join(self.current_path, item_text)
            if os.path.isdir(full_path):
                self.display_directory(full_path)
            else:
                # Open file (platform-dependent)
                try:
                    os.startfile(full_path)  # For Windows
                except AttributeError:
                    import subprocess
                    subprocess.call(['open', full_path])  # For macOS/Linux


if __name__ == "__main__":
    root = tk.Tk()
    app = FinderLikeExplorer(root)
    root.mainloop()
