import sys

from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QPushButton,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCruise")
        self.resize(300, 300)
        # Create a QVBoxLayout instance
        self.layout = QVBoxLayout()
        # Add widgets to the layout
        button = QPushButton("Create new Mode")
        button.clicked.connect(self.add_mode)
        self.layout.addWidget(button)
        

        self.layout.addStretch()
        # Set the layout on the application's window
        self.setLayout(self.layout)
        # self.setCentralWidget(QWidget)

    def add_mode(self):
        mode_form = QFormLayout()
        mode_form.addRow("Mode Name:", QLineEdit())
        self.layout.addLayout(mode_form)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())