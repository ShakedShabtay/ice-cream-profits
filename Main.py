import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QVBoxLayout, QHBoxLayout
)
from About import About

class IceCreamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.temperatures = []
        self.profits = []
        self.about_window = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Ice Cream Profits Analysis")
        self.resize(750, 580)

        self.title_label = QLabel("Ice Cream Profits vs. Temperature")
        self.title_label.setObjectName("title")

        # שורה עליונה: כפתור בחירת קובץ
        self.load_btn = QPushButton("Load Ice Cream CSV")
        self.load_btn.clicked.connect(self.load_file)

        self.file_label = QLabel("No file selected")

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.load_btn)
        top_layout.addWidget(self.file_label)
        top_layout.addStretch()
        
















if __name__ == "__main__":
    app = QApplication()

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = IceCreamWindow()
    window.show()
    app.exec()