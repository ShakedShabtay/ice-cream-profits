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


        self.load_btn = QPushButton("Load Ice Cream CSV")
        self.load_btn.clicked.connect(self.load_file)

        self.file_label = QLabel("No file selected")

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.load_btn)
        top_layout.addWidget(self.file_label)
        top_layout.addStretch()

        self.fig, self.ax = plt.subplots(1, 1)
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)


        self.about_btn = QPushButton("About")
        self.about_btn.setObjectName("about_btn")
        self.about_btn.clicked.connect(self.open_about)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.about_btn)


        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Ice Cream File", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_path != "":
            self.file_label.setText(os.path.basename(file_path))
            self.temperatures = []
            self.profits = []

            with open(file_path, 'r') as f:
                next(f)  
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) >= 2:
                        temp = float(parts[0])
                        profit = float(parts[1])
                        self.temperatures.append(temp)
                        self.profits.append(profit)

            self.plot_graph()

    def plot_graph(self):
        self.ax.clear()

        self.ax.scatter(self.temperatures, self.profits, s=1, color='blue', label='Daily Sales')

        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)













if __name__ == "__main__":
    app = QApplication()

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = IceCreamWindow()
    window.show()
    app.exec()