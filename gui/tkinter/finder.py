#
# Author: Rohtash Lakra
#
import os
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk  # For handling images


class FileExplorer:

    def __init__(self, master):
        self.master = master
        master.title("Python Finder")  # Renamed for clarity
        master.geometry("1000x700")  # Larger window size

        self.downloads_path = os.path.expanduser("~/Downloads")  # Start in downloads

        # Styling for ttk widgets to mimic macOS
        style = ttk.Style()
        style.theme_use('clam')  # A cleaner theme for ttk
        style.configure("Treeview", rowheight=25, font=("Helvetica", 10))
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("ColumnButton.TButton", background="lightgray", font=("Helvetica", 10))

        # --- Frames ---
        # Top bar for path and navigation
        self.top_bar_frame = tk.Frame(master, bd=1, relief="raised", bg="lightgray")
        self.top_bar_frame.pack(side="top", fill="x")

        # Sidebar frame
        self.sidebar_frame = tk.Frame(master, width=200, bg="#f0f0f0", relief="raised", bd=1)
        self.sidebar_frame.pack(side="left", fill="y")

        # Main content area - Using PanedWindow for adjustable columns
        self.main_content_pane = ttk.PanedWindow(master, orient="horizontal")
        self.main_content_pane.pack(side="right", fill="both", expand=True)

        # Preview pane frame
        self.preview_frame = tk.Frame(self.main_content_pane, width=250, bg="#e0e0e0")
        self.main_content_pane.add(self.preview_frame)

        # --- Top Bar ---
        self.back_button = ttk.Button(self.top_bar_frame, text="<", command=self.go_back)
        self.back_button.pack(side="left", padx=5, pady=5)

        self.path_label = tk.Label(self.top_bar_frame, text=self.downloads_path, bg="lightgray",
                                   font=("Helvetica", 10))
        self.path_label.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        # --- Sidebar ---
        self.sidebar_label = tk.Label(self.sidebar_frame, text="Favorites", bg="#f0f0f0",
                                      font=("Helvetica", 12, "bold"))
        self.sidebar_label.pack(pady=10, padx=10, anchor="w")

        self.home_button = ttk.Button(self.sidebar_frame, text="Home",
                                      command=lambda: self.display_directory(os.path.expanduser("~")),
                                      style="ColumnButton.TButton")
        self.home_button.pack(pady=5, padx=10, anchor="w")

        self.downloads_button = ttk.Button(self.sidebar_frame, text="Downloads",
                                           command=lambda: self.display_directory(self.downloads_path),
                                           style="ColumnButton.TButton")
        self.downloads_button.pack(pady=5, padx=10, anchor="w")

        # --- Column View (Listboxes as columns) ---
        self.column_frames = []
        self.column_lists = []
        self.column_widths = 200  # Adjust width as needed

        for i in range(3):  # Start with 3 columns
            frame = tk.Frame(self.main_content_pane, bg="white", bd=1, relief="raised")
            self.main_content_pane.add(frame)
            self.column_frames.append(frame)

            listbox = tk.Listbox(frame, selectmode="single", font=("Helvetica", 10),
                                 borderwidth=0, highlightthickness=0)
            listbox.pack(fill="both", expand=True, padx=2, pady=2)
            listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
            listbox.bind("<Double-1>", self.on_listbox_double_click)  # Bind double-click for navigation
            self.column_lists.append(listbox)

        # --- Preview Pane ---
        self.preview_title = tk.Label(self.preview_frame, text="File Information",
                                      bg="#e0e0e0", font=("Helvetica", 12, "bold"))
        self.preview_title.pack(pady=10)

        self.preview_image_label = tk.Label(self.preview_frame, bg="#e0e0e0")
        self.preview_image_label.pack(pady=10)

        self.preview_text = tk.Text(self.preview_frame, wrap="word", height=10, width=30,
                                    font=("Helvetica", 10), relief="flat")
        self.preview_text.pack(pady=10, padx=10, fill="both", expand=True)

        self.display_directory(self.downloads_path)

    def display_directory(self, path, column_index=0):
        self.current_path = path
        self.path_label.config(text=self.current_path)

        for i in range(column_index, len(self.column_lists)):
            self.column_lists[i].delete(0, tk.END)  # Clear columns from current onwards

        try:
            items = sorted(os.listdir(path), key=lambda s: s.lower())  # Sort items alphabetically
            for item in items:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    self.column_lists[column_index].insert(tk.END, item + "/")  # Indicate folders with /
                else:
                    self.column_lists[column_index].insert(tk.END, item)
        except PermissionError:
            print(f"Permission denied to access: {path}")

    def on_listbox_select(self, event):
        selected_listbox = event.widget
        column_index = self.column_lists.index(selected_listbox)
        selected_index = selected_listbox.curselection()

        if selected_index:
            item_name = selected_listbox.get(selected_index[0]).rstrip('/')
            selected_path = os.path.join(self.get_current_path_for_column(column_index), item_name)

            if os.path.isdir(selected_path):
                self.display_directory(selected_path, column_index + 1)
            else:
                self.show_file_preview(selected_path)

            self.clear_columns_after(column_index + 1)  # Clear columns to the right

    def on_listbox_double_click(self, event):
        selected_listbox = event.widget
        column_index = self.column_lists.index(selected_listbox)
        selected_index = selected_listbox.curselection()

        if selected_index:
            item_name = selected_listbox.get(selected_index[0]).rstrip('/')
            full_path = os.path.join(self.get_current_path_for_column(column_index), item_name)

            if os.path.isdir(full_path):
                self.display_directory(full_path, column_index + 1)
            else:
                try:
                    os.startfile(full_path)  # For Windows
                except AttributeError:
                    import subprocess
                    subprocess.call(['open', full_path])  # For macOS/Linux

    def go_back(self):
        parent_path = os.path.dirname(self.current_path)
        if parent_path != self.current_path:  # Prevent going above root
            self.display_directory(parent_path, 0)  # Redisplay from the first column

    def get_current_path_for_column(self, column_index):
        path_components = []
        for i in range(column_index):
            selected_indices = self.column_lists[i].curselection()
            if selected_indices:
                item_name = self.column_lists[i].get(selected_indices[0]).rstrip('/')
                path_components.append(item_name)
        return os.path.join(self.current_path.split(os.sep)[0] + os.sep, *path_components)  # Reconstruct path

    def clear_columns_after(self, start_index):
        for i in range(start_index, len(self.column_lists)):
            self.column_lists[i].delete(0, tk.END)

    def show_file_preview(self, file_path):
        self.preview_image_label.config(image=None)  # Clear previous image
        self.preview_text.delete("1.0", tk.END)

        try:
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_path)[1].lower()

                if file_extension in [".jpg", ".jpeg", ".png", ".gif"]:
                    image = Image.open(file_path)
                    image.thumbnail((200, 200))  # Resize for preview
                    photo = ImageTk.PhotoImage(image)
                    self.preview_image_label.config(image=photo)
                    self.preview_image_label.image = photo  # Keep a reference
                elif file_extension in [".txt", ".md", ".py", ".html"]:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(1000)  # Read first 1000 characters
                        self.preview_text.insert(tk.END, content)
                else:
                    self.preview_text.insert(tk.END, "No preview available for this file type.")
            else:
                self.preview_text.insert(tk.END, "No file selected or not a valid file.")
        except Exception as e:
            self.preview_text.insert(tk.END, f"Error previewing file: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()
