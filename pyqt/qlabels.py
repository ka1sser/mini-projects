# Topic: PyQt5 | QLabel

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Garamond", 30))
        label.setGeometry(0, 0, 500, 100)

        label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-weight: bold;"
            "font-style: italic;"
        )

        # label.setAlignment(Qt.AlignTop) # Vertically Top
        # label.setAlignment(Qt.AlignBottom) # Vertically Top
        # label.setAlignment(Qt.AlignVCenter) # Vertically Top

        # label.setAlignment(Qt.AlignRight)  # Horizontally Right
        # label.setAlignment(Qt.AlignHCenter)  # Horizontally Center
        # label.setAlignment(Qt.AlignLeft)  # Horizontally Left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & Center
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # HCenter & Vertically Top
        label.setAlignment(Qt.AlignCenter)  # Center


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
