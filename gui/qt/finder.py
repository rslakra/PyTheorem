# #
# # Author: Rohtash Lakra
# #
# import os
# import sys
#
# from PyQt6.QtCore import QDir, Qt
# from PyQt6.QtGui import QFileSystemModel, QPixmap
# from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QSplitter,
#                              QColumnView, QLabel, QTextEdit, QPushButton, QLineEdit)
#
#
# class FileExplorer(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Python Finder")
#         self.setGeometry(100, 100, 800, 600)
#
#         main_layout = QVBoxLayout()
#         splitter = QSplitter(self)
#         main_layout.addWidget(splitter)
#
#         # File system model
#         self.model = QFileSystemModel()
#         self.model.setRootPath(QDir.homePath())
#
#         # Column View
#         self.column_view = QColumnView(self)
#         self.column_view.setModel(self.model)
#         self.column_view.setRootIndex(self.model.index(QDir.homePath()))
#         self.column_view.clicked.connect(self.update_preview)
#         splitter.addWidget(self.column_view)
#
#         # Preview Pane
#         self.preview_pane = QWidget(self)
#         preview_layout = QVBoxLayout()
#         self.preview_label = QLabel("Select a file to preview", self)
#         self.preview_text = QTextEdit(self)
#         self.preview_text.setReadOnly(True)
#         preview_layout.addWidget(self.preview_label)
#         preview_layout.addWidget(self.preview_text)
#         self.preview_pane.setLayout(preview_layout)
#         splitter.addWidget(self.preview_pane)
#
#         self.setLayout(main_layout)
#
#     def update_preview(self, index):
#         file_path = self.model.filePath(index)
#         if self.model.isDir(index):
#             self.preview_label.setText(f"Folder: {os.path.basename(file_path)}")
#             self.preview_text.clear()
#         else:
#             self.preview_label.setText(f"File: {os.path.basename(file_path)}")
#             try:
#                 # Attempt to open and read as text
#                 with open(file_path, 'r', encoding='utf-8') as f:
#                     content = f.read()
#                     self.preview_text.setText(content)
#             except Exception:
#                 # If not text, try to open as image
#                 pixmap = QPixmap(file_path)
#                 if not pixmap.isNull():
#                     self.preview_label.setPixmap(pixmap.scaled(self.preview_label.size(),
#                                                                Qt.AspectRatioMode.KeepAspectRatio,
#                                                                Qt.TransformationMode.SmoothTransformation))
#                     self.preview_text.clear()
#                 else:
#                     self.preview_label.setText("No preview available")
#                     self.preview_text.clear()
#
#
# # Main application
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     explorer = FileExplorer()
#     explorer.show()
#     sys.exit(app.exec())
