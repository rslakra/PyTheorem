#
# Author: Rohtash Lakra
#
import os
import tkinter as tk
from tkinter import ttk


class FileExplorer:
    def __init__(self, master):
        self.master = master
        master.title("Python File Explorer")
        master.geometry("600x400")

        self.current_path = tk.StringVar()
        self.current_path.set(os.getcwd())  # Set initial path to current working directory

        self.path_label = tk.Label(master, textvariable=self.current_path, anchor="w")
        self.path_label.pack(fill=tk.X, padx=10, pady=5)

        self.tree = ttk.Treeview(master)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree.heading("#0", text="Name", anchor="w")
        self.tree.bind("<Double-1>", self.on_double_click)

        self.populate_tree(self.current_path.get())

    def populate_tree(self, path):
        self.tree.delete(*self.tree.get_children())
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    self.tree.insert("", "end", text=item, values=("Directory",), tags=("folder",))
                else:
                    self.tree.insert("", "end", text=item, values=("File",), tags=("file",))
        except Exception as e:
            print(f"Error listing directory: {e}")

    def on_double_click(self, event):
        item_id = self.tree.selection()[0]
        item_text = self.tree.item(item_id, "text")
        item_type = self.tree.item(item_id, "values")[0]

        if item_type == "Directory":
            new_path = os.path.join(self.current_path.get(), item_text)
            self.current_path.set(new_path)
            self.populate_tree(new_path)
        elif item_type == "File":
            # Example: Open the file with default application
            try:
                os.startfile(os.path.join(self.current_path.get(), item_text))
            except Exception as e:
                print(f"Error opening file: {e}")


root = tk.Tk()
app = FileExplorer(root)
root.mainloop()
