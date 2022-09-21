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
        
        self.tabs = QTabWidget()
        self.add_tabs()

        self.layout.addStretch()
        # Set the layout on the application's window
        self.setLayout(self.layout)
        # self.setCentralWidget(QWidget)

    def add_mode(self):
        mode_form = QFormLayout()
        text = QLineEdit()
        mode_form.addRow("Mode Name:", text)
        text.returnPressed.connect(lambda: create_mode())
        # print(content)
        self.layout.addLayout(mode_form)

        def create_mode():
            value = text.text()
            open(f"txt_files/{value}.txt", "a")
            self.tabs.addTab(self.mode_tab(), f"{value}")

    def add_tabs(self):
        DIR = 'txt_files/'
        current_collection = None
        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        file_len = (len(fnmatch.filter(os.listdir(DIR), '*txt')))
        for i in range(len(file_list)):
            text = str(Path(file_list[i]))
            mode_text = text.rstrip(".txt")
            self.tabs.addTab(self.mode_tab(), f"{mode_text}")
        self.layout.addWidget(self.tabs)
    
    def mode_tab(self):
        modeTab = QWidget()
        layout = QVBoxLayout()
        app_form = QFormLayout()
        text = QLineEdit()
        app_form.addRow("Add App:", text)
        layout.addLayout(app_form)
        text.returnPressed.connect(lambda: self.add_app(text))
        
        
        layout.addWidget(QPushButton("Launch"))
        modeTab.setLayout(layout)
        return modeTab

    def add_app(self, text):
        value = text.text()
        index = self.tabs.currentIndex()
        current_collection = self.tabs.tabText(index)
        with open(f"txt_files/{current_collection}.txt", "a") as f:
            f.write(f"{value}\n")

        
          
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())