from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class About(QWidget):
    def __init__(self, github_url="https://github.com/ShakedShabtay/ice-cream-profits.git"):
        super().__init__()
        self.github_url = github_url
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("About")
        self.resize(360, 420)


        self.image_label = QLabel()
        self.image_label.setFixedSize(140, 140)
        pixmap = QPixmap("my_photo.JPG")
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
        else:
            self.image_label.setText("Profile Photo")
            self.image_label.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel("Name: Shaked Shabtay")
        self.email_label = QLabel("Email: Shaked789@gmail.com")

        self.linkedin_label = QLabel(
            '<a href="https://www.linkedin.com/in/shaked-shabtay">My LinkedIn Profile</a>'
        )
        self.linkedin_label.setOpenExternalLinks(True)


        self.github_label = QLabel(
            f'<a href="{self.github_url}">GitHub Repository</a>'
        )
        self.github_label.setOpenExternalLinks(True)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.name_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.linkedin_label)
        layout.addWidget(self.github_label)
        layout.addStretch()

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication()
    window = About()
    window.show()
    app.exec()