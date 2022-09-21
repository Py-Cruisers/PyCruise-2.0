import sys
import os
import webbrowser

from PyQt6.QtCore import Qt
import fnmatch
from pathlib import Path
import platform

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

        self.layout = QVBoxLayout()

        button = QPushButton("Create new Mode")
        button.clicked.connect(self.add_mode)
        self.layout.addWidget(button)
        
        self.tabs = QTabWidget()
        self.add_tabs()

        self.layout.addStretch()
        self.setLayout(self.layout)

    # TO DO: Create 'enter' button for creating mode
    # TO DO: When new mode created, prompt should disappear
    def add_mode(self):
        mode_form = QFormLayout()
        text = QLineEdit()
        mode_form.addRow("Mode Name:", text)
        text.returnPressed.connect(lambda: create_mode())
        self.layout.addLayout(mode_form)

        def create_mode():
            value = text.text()
            open(f"txt_files/{value}.txt", "a")
            self.tabs.addTab(self.mode_tab(), f"{value}")

    def add_tabs(self):
        DIR = 'txt_files/'
        file_list = fnmatch.filter(os.listdir(DIR), '*txt')

        # TO DO: edit strip txt to just '.txt' and not all t's and x's
        for i in range(len(file_list)):
            text = str(Path(file_list[i]))
            mode_text = text.rstrip(".txt")

            self.tabs.addTab(self.mode_tab(), f"{mode_text}")
        self.layout.addWidget(self.tabs)

    # TO DO: 'show' functionality
    def mode_tab(self):
        modeTab = QWidget()
        layout = QVBoxLayout()
        app_form = QFormLayout()
        text = QLineEdit()

        # TO DO: condition to only display with edit(); edit button go here instead of add_app 
        app_form.addRow("Add App:", text)
        layout.addLayout(app_form)
        text.returnPressed.connect(lambda: self.add_app(text))
        
        launch_button = QPushButton("Launch")
        layout.addWidget(launch_button)
        launch_button.clicked.connect(self.launch_mode)

        modeTab.setLayout(layout)
        return modeTab

    # TO DO: condition
    def add_app(self, text):
        value = text.text()
        index = self.tabs.currentIndex()
        current_collection = self.tabs.tabText(index)
        with open(f"txt_files/{current_collection}.txt", "a") as f:
            f.write(f"{value}\n")
    
    # TO DO: 'delete' functionality
    def launch_mode(self):
        index = self.tabs.currentIndex()
        current_collection = self.tabs.tabText(index)
        with open(f"txt_files/{current_collection}.txt", "r") as f:
            text_from_file = f.readlines()
            for app in text_from_file:
                if "http" in app or "www" in app:
                    webbrowser.open(app.strip())
                else:
                    app_to_use = app.strip('\n').lower()

                    if platform.system() == 'Linux':
                        os.system(f"/snap/bin/{app_to_use}")

                    if platform.system() == 'Darwin':
                        os.system(f"""osascript -e 'tell application "{app_to_use}" to activate'""")

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
