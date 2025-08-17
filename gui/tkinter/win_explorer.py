#
# Author: Rohtash Lakra
#
import os
import tkinter as tk
from tkinter import ttk


class Finder:

    def __init__(self, master):
        self.master = master
        master.title("Python Explorer")
        master.geometry("640x480")
        self.root_dir = os.getcwd()
        print("Root directory: " + self.root_dir)
        # Load folder and file icons
        # Replace 'folder_icon.png' and 'file_icon.png' with your actual icon file paths
        self.folder_icon = tk.PhotoImage(file=os.path.join(self.root_dir, "gui/icons/folder.png"))
        self.file_icon = tk.PhotoImage(file=os.path.join(self.root_dir, "gui/icons/file.png"))

        self.current_path = os.path.expanduser("~/Documents")  # Starting directory

        # Styling
        style = ttk.Style()
        # style.theme_use('vista')  # A Windows-like theme for ttk
        style.configure("Treeview", rowheight=25, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("TButton", font=("Segoe UI", 9))

        # --- Top Bar (Path and Navigation) ---
        self.top_bar_frame = tk.Frame(master, bd=1, relief="raised", bg="#f0f0f0")
        self.top_bar_frame.pack(side="top", fill="x")

        self.back_button = ttk.Button(self.top_bar_frame, text="←", command=self.go_back)
        self.back_button.pack(side="left", padx=5, pady=5)

        self.forward_button = ttk.Button(self.top_bar_frame, text="→", command=self.go_forward)
        self.forward_button.pack(side="left", padx=5, pady=5)

        self.path_entry = ttk.Entry(self.top_bar_frame, font=("Segoe UI", 10))
        self.path_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        self.path_entry.bind("<Return>", self.navigate_to_path)  # Navigate on Enter key
        self.path_entry.insert(0, self.current_path)

        # --- Main Content Area (Sidebar and File List) ---
        self.main_content_pane = ttk.PanedWindow(master, orient="horizontal")
        self.main_content_pane.pack(side="right", fill="both", expand=True)

        # Sidebar (Treeview for directory structure)
        self.sidebar_frame = tk.Frame(self.main_content_pane, width=250, bg="white", bd=1, relief="raised")
        self.main_content_pane.add(self.sidebar_frame)

        self.tree_scroll_y = ttk.Scrollbar(self.sidebar_frame, orient="vertical")
        self.tree_scroll_y.pack(side="right", fill="y")
        self.tree_scroll_x = ttk.Scrollbar(self.sidebar_frame, orient="horizontal")
        self.tree_scroll_x.pack(side="bottom", fill="x")

        self.treeview = ttk.Treeview(self.sidebar_frame, yscrollcommand=self.tree_scroll_y.set,
                                     xscrollcommand=self.tree_scroll_x.set, selectmode="browse")
        self.treeview.pack(fill="both", expand=True)
        self.treeview.heading("#0", text="Folders", anchor="w")
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)
        self.tree_scroll_y.config(command=self.treeview.yview)
        self.tree_scroll_x.config(command=self.treeview.xview)

        # File list area
        self.file_list_frame = tk.Frame(self.main_content_pane, bg="white")
        self.main_content_pane.add(self.file_list_frame)

        self.file_scroll_y = ttk.Scrollbar(self.file_list_frame, orient="vertical")
        self.file_scroll_y.pack(side="right", fill="y")

        self.file_list_view = ttk.Treeview(self.file_list_frame, columns=("Type", "Size", "Date Modified"),
                                           yscrollcommand=self.file_scroll_y.set, selectmode="browse")
        self.file_list_view.pack(fill="both", expand=True)

        self.file_list_view.heading("#0", text="Name", anchor="w")
        self.file_list_view.heading("Type", text="Type", anchor="w")
        self.file_list_view.heading("Size", text="Size", anchor="w")
        self.file_list_view.heading("Date Modified", text="Date Modified", anchor="w")

        self.file_list_view.column("#0", width=300, minwidth=150)
        self.file_list_view.column("Type", width=50, minwidth=50)
        self.file_list_view.column("Size", width=100, minwidth=100)
        self.file_list_view.column("Date Modified", width=125, minwidth=125)

        self.file_list_view.bind("<Double-1>", self.on_file_list_double_click)

        self.file_scroll_y.config(command=self.file_list_view.yview)

        self.history = []
        self.history_index = -1

        self.populate_treeview()
        self.display_directory(self.current_path)
        # self.select_and_expand_treeview_path(self.current_path)

    def populate_treeview(self, parent_id="", path=""):
        if not path:
            path = os.path.expanduser("~")  # Start from home directory
        if not parent_id:
            parent_id = self.treeview.insert("", "end", text=os.path.basename(path) or path, open=True, iid=path)

        for item in sorted(os.listdir(path), key=lambda s: s.lower()):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                self.treeview.insert(parent_id, "end", text=item, iid=full_path, open=False)

            # if os.path.isdir(full_path):
            #     self.treeview.insert(parent_id, "end", text=item, iid=full_path, open=False, image=self.folder_icon)
            # else:
            #     self.treeview.insert(parent_id, "end", text=item, iid=full_path, open=False, image=self.file_icon)

    def display_directory(self, path):
        if not os.path.isdir(path):
            print(f"Error: {path} is not a valid directory.")
            return

        self.current_path = path
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)

        self.file_list_view.delete(*self.file_list_view.get_children())  # Clear file list

        try:
            for item in sorted(os.listdir(path), key=lambda s: s.lower()):
                full_path = os.path.join(path, item)
                item_type = ""
                item_size = ""
                item_date_modified = ""

                if os.path.isdir(full_path):
                    item_type = "Folder"
                    # self.file_list_view.insert("", "end", text=item, values=(item_type, item_size, item_date_modified),
                    #                            image=self.folder_icon)
                else:
                    item_type = "File"
                    item_size = self.format_size(os.path.getsize(full_path))
                    item_date_modified = self.format_date(os.path.getmtime(full_path))
                    # self.file_list_view.insert("", "end", text=item, values=(item_type, item_size, item_date_modified),
                    #                            image=self.file_icon)

                self.file_list_view.insert("", "end", text=item, values=(item_type, item_size, item_date_modified))

                # Update sidebar selection and expansion
                # First, ensure the path exists in the treeview
                # self.select_and_expand_treeview_path(path)

        except PermissionError:
            print(f"Permission denied to access: {path}")

        # Update history
        if not self.history or self.history[-1] != path:
            self.history = self.history[:self.history_index + 1]
            self.history.append(path)
            self.history_index = len(self.history) - 1

    def select_and_expand_treeview_path(self, target_path):
        """Selects and expands the given path in the sidebar Treeview."""
        # Collapse all items first for a cleaner visual, then expand only the target path
        for item in self.treeview.get_children():
            self.treeview.item(item, open=False)

        # Iterate through path components to expand the tree
        current_node = ""
        path_parts = target_path.split(os.sep)
        # Find the root node (e.g., C:\ or home directory)
        # This needs to be more robust for different operating systems and root paths
        # For simplicity, we'll assume the top-level items in treeview are root-like
        # You'll need to adapt this logic for handling different roots like C:\ or /
        if path_parts:
            # Try to find the top-level parent in the treeview
            top_level_items = self.treeview.get_children()
            for item_id in top_level_items:
                item_path = self.treeview.item(item_id, "iid")
                # Check if the current path starts with this top-level item's path
                if target_path.startswith(item_path):
                    current_node = item_id
                    break

        # If a matching top-level node is found, proceed
        if current_node:
            accumulated_path = self.treeview.item(current_node, "iid")
            self.treeview.item(current_node, open=True)  # Open the top-level node

            for part in path_parts[len(accumulated_path.split(os.sep)):]:  # Start from the next part
                found = False
                for child_id in self.treeview.get_children(current_node):
                    child_path = self.treeview.item(child_id, "iid")
                    if os.path.basename(child_path) == part:
                        current_node = child_id
                        self.treeview.item(current_node, open=True)
                        # Populate children if they haven't been loaded yet
                        if not self.treeview.get_children(current_node):
                            self.populate_treeview(parent_id=current_node, path=child_path)
                        found = True
                        break
                if not found:  # If a part is not found, break and possibly report an error
                    break
        else:
            print(f"Could not find {target_path} in the treeview hierarchy.")

        # Select the final node
        self.treeview.selection_set(current_node)
        self.treeview.see(current_node)  # Scroll to the selected item if not visible

    def on_treeview_select(self, event):
        selected_item = self.treeview.focus()
        if selected_item:
            path = self.treeview.item(selected_item, "iid")
            self.display_directory(path)

            # Expand the selected node if it's a directory
            if os.path.isdir(path) and not self.treeview.item(selected_item, "open"):
                self.treeview.item(selected_item, open=True)
                # Populate its children if not already populated
                if not self.treeview.get_children(selected_item):
                    self.populate_treeview(parent_id=selected_item, path=path)

    def on_file_list_double_click(self, event):
        selected_item = self.file_list_view.focus()
        if selected_item:
            item_name = self.file_list_view.item(selected_item, "text")
            full_path = os.path.join(self.current_path, item_name)
            if os.path.isdir(full_path):
                self.display_directory(full_path)
            else:
                self.open_file(full_path)

    def open_file(self, full_path):
        try:
            os.startfile(full_path)  # For Windows
        except AttributeError:
            import subprocess
            subprocess.call(['open', full_path])  # For macOS/Linux

    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.display_directory(self.history[self.history_index])

    def go_forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.display_directory(self.history[self.history_index])

    def navigate_to_path(self, event=None):
        path = self.path_entry.get()
        if os.path.isdir(path):
            self.display_directory(path)
        else:
            print(f"Invalid path: {path}")

    def format_size(self, size_in_bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_in_bytes < 1024.0:
                return f"{size_in_bytes:.1f} {unit}"
            size_in_bytes /= 1024.0
        return f"{size_in_bytes:.1f} TB"

    def format_date(self, timestamp):
        from datetime import datetime
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    root = tk.Tk()
    app = Finder(root)
    root.mainloop()
