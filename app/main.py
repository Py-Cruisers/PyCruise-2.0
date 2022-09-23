import sys
import os
import webbrowser
import shutil
from xml.dom import NOT_FOUND_ERR

from PyQt6 import QtCore
from PyQt6.QtCore import Qt

import fnmatch
from pathlib import Path
import platform

from PyQt6.QtGui import QIcon, QPixmap


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
    QLabel,
)
print("testing testing 123")
class Window(QWidget):

    def __init__(self):
        super().__init__()

        # Initial application window setup
        self.setWindowTitle("PyCruise")
        self.resize(500, 300)

        # Create a QVBoxLayout instance
        self.layout = QVBoxLayout()

        pixmap = QPixmap("pycruise.png")
        self.setGeometry(15, 15, 10, 10)
        self.label = QLabel()
        self.label.setPixmap(pixmap)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.show()

        # 'Create Mode' Button
        self.create_new_mode_button = QPushButton("Create new Mode")
        self.create_new_mode_button.clicked.connect(self.add_mode)
        self.layout.addWidget(self.create_new_mode_button)
        
        button.setStyleSheet(
        "background-color: #dedbd2; "
        "color: #000000;"
        "font-family: sans-serif; "
        "font-size: 15px;")
        

        # Tabs Initialization
        self.tabs = QTabWidget()

        # Tabs function call to display on window
        self.add_tabs()
        
        self.layout.addStretch()

        self.setLayout(self.layout)

    def add_mode(self):
        mode_form = QFormLayout()
        text = QLineEdit()
        mode_form.addRow("Mode Name:", text)
        
        text.returnPressed.connect(lambda: create_mode())
        text.returnPressed.connect(text.clear)
        self.layout.addLayout(mode_form)

        def create_mode():
            value = text.text()
            open(f"txt_files/{value}.txt", "a")
            self.tabs.addTab(Tab(value, self.layout), f"{value}")

    def add_tabs(self):
        DIR = 'app/txt_files/'
        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        
        for i in range(len(file_list)):
            text = str(Path(file_list[i]))
            mode_text = text.rstrip(".txt")
            self.tabs.addTab(Tab(mode_text, self.layout), f"{mode_text}")
        self.layout.addWidget(self.tabs)

class Tab(QTabWidget):
    def __init__(self, mode_text, window_layout):
        super().__init__()
        self.test_tab = QWidget()
        self.layout = QVBoxLayout()
        self.addTab(self.test_tab, "PyCruise")
        # self.add_tabs()
        self.mode_text = mode_text
        self.window_layout = window_layout
        launch_button = QPushButton("Launch")
        launch_button.move(10,10)
        self.layout.addWidget(launch_button)
        
        launch_button.setStyleSheet(
            "background-color: #dedbd2;"
            "color: #000000;"
            "font-family: times; "
            "font-size: 15px;")

        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(lambda: self.add_app(window_layout, self.layout))
        edit_button.clicked.connect(lambda: self.delete_app(window_layout))
        self.layout.addWidget(edit_button)
        
        edit_button.setStyleSheet(
            "background-color: #dedbd2; "
            "color: #000000;"
            "font-family: times; "
            "font-size: 15px;")

        self.show_apps()
        launch_button.clicked.connect(self.launch_mode)
        self.test_tab.setGeometry(50,50,320,200)
    
        self.test_tab.setLayout(self.layout)
    
    def hi(self):
        print("Hi")

    def add_app(self, window_layout, layout):
        mode_form = QFormLayout()
        text = QLineEdit()
        mode_form.addRow("Add Application or Website:", text)
        text.returnPressed.connect(lambda: create_app(layout))
        text.returnPressed.connect(text.clear)
        window_layout.addLayout(mode_form)
        
        def create_app(layout):
    
            layout.addWidget(QCheckBox(text.text()))
            current_collection = self.mode_text
            with open(f"txt_files/{current_collection}.txt", "a") as f:
                f.write(f"{text.text()}\n")

    
    def delete_app(self, window_layout):
        mode_form = QFormLayout()
        text = QLineEdit()
        mode_form.addRow("Delete Application or Website:", text)
        text.returnPressed.connect(lambda: remove_app())
        text.returnPressed.connect(text.clear)
        window_layout.addLayout(mode_form)

        def remove_app():
            value = text.text()
            current_collection = self.mode_text
            print(current_collection, "current collection from delete app")
            with open(f"txt_files/{current_collection}.txt", "r") as fr:
                lines = fr.readlines()
                print(lines, "content for txt file from delete app")
                with open(f"txt_files/{current_collection}.txt", "w") as fw:
                    for line in lines:
                        if line.strip('\n').lower() != f"{value.lower()}":
                            fw.write(line)
        
    def launch_mode(self):
        current_mode = self.mode_text
        with open(f"txt_files/{current_mode}.txt", "r") as f:
            text_from_file = f.readlines()
            for app in text_from_file:
                if "http" in app or "www" in app:
                    webbrowser.open(app.strip())
                else:
                    app_to_use = app.strip('\n').lower()

                    if platform.system() == 'Linux':
                        req_app = shutil.which(f"{app_to_use}")
                        os.system(f"{req_app}")

                    if platform.system() == 'Darwin':
                        os.system(f"""osascript -e 'tell application "{app_to_use}" to activate'""")

    def show_apps(self):
        current_mode = self.mode_text
        with open(f"app/txt_files/{current_mode}.txt", "r") as f:
            text_from_file = f.readlines()
            for app in text_from_file:
                app_to_use = app.strip('\n').lower()
                self.layout.addWidget(QCheckBox(app_to_use))
    
    # FUTURE FEATURE
    # def add_tabs(self):
    #     DIR = 'txt_files/'
    #     file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        
    #     for i in range(len(file_list)):
    #         text = str(Path(file_list[i]))
    #         mode_text = text.rstrip(".txt")
    #         self.addTab(self.test_tab, f"{mode_text}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())