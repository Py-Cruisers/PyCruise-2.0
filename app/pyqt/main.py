import sys
import os

from PyQt6.QtCore import Qt
import fnmatch
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QPushButton,
    QDialogButtonBox,
    QTabWidget,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QCheckBox,
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
        
        tabs = QTabWidget()

        DIR = 'txt_files/'
        current_collection = None
        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        file_len = (len(fnmatch.filter(os.listdir(DIR), '*txt')))
        for i in range(len(file_list)):
            tabs.addTab(self.mode_tab(), f"{Path(file_list[i])}")
        self.layout.addWidget(tabs)

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
    
    def mode_tab(self):
        modeTab = QWidget()
        layout = QVBoxLayout()
        modeTab.setLayout(layout)
        return modeTab
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())