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
        text = QLineEdit()
        mode_form.addRow("Mode Name:", text)
        text.returnPressed.connect(lambda: print_msg())
        # print(content)
        self.layout.addLayout(mode_form)

        def print_msg():
            value = text.text()
            open(f"txt_files/{value}.txt", "a")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())