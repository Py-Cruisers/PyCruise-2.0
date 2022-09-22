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

        # Initial application window setup
        self.setWindowTitle("PyCruise")
        self.resize(300, 300)

        # Create a QVBoxLayout instance
        self.layout = QVBoxLayout()

        # 'Create Mode' Button
        button = QPushButton("Create new Mode")
        button.clicked.connect(self.add_mode)
        self.layout.addWidget(button)
        
        # Tabs Initialization
        self.tabs = QTabWidget()
        # Tabs function call to display on window
        self.add_tabs()

        # Makes window styling dynamic
        self.layout.addStretch()

        # Set the layout on the application's window
        self.setLayout(self.layout)
        # self.setCentralWidget(QWidget)

    # Function to create a mode
    # TO DO: Create 'enter' button for creating mode
    # TO DO: When new mode created, prompt should disappear
    def add_mode(self):

        # Widget calls
        mode_form = QFormLayout()
        text = QLineEdit()
        # User prompt
        mode_form.addRow("Mode Name:", text)
        #Click event
        text.returnPressed.connect(lambda: create_mode())
        # Format call to display form on page
        self.layout.addLayout(mode_form)

        # Actual creation of mode
        def create_mode():
            # User input
            value = text.text()
            # Creation of txt file with user input
            open(f"txt_files/{value}.txt", "a")
            # Push new txt file to tabs
            self.tabs.addTab(self.mode_tab(), f"{value}")

    def add_tabs(self):
        DIR = 'txt_files/'
        # current_collection = None # using?

        # filtering through txt files to display them
        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        
        # file_len = (len(fnmatch.filter(os.listdir(DIR), '*txt'))) # checking if txt files existed; need here?

        # Strip .txt 
        # TO DO: edit strip txt to just '.txt' and not all t's and x's
        for i in range(len(file_list)):
            text = str(Path(file_list[i]))
            mode_text = text.rstrip(".txt")
            # push new txt file stripped names to tabs
            self.tabs.addTab(self.mode_tab(), f"{mode_text}")
        self.layout.addWidget(self.tabs)
    
    # Tabs for each mode
    # TO DO: 'show' functionality
    def mode_tab(self):
        # Class initials
        modeTab = QWidget()
        layout = QVBoxLayout()
        app_form = QFormLayout()
        text = QLineEdit()

        # TO DO: condition to only display with edit(); edit button go here instead of add_app 
        app_form.addRow("Add App:", text)
        layout.addLayout(app_form)
        
        text.returnPressed.connect(lambda: self.add_app(text, layout))
        # layout.addWidget(QCheckBox(text.text()))
    
        # index = self.tabs.currentIndex()
        # current_collection = self.tabs.tabText(index)
        # print(current_collection)

        # launch button initial
        launch_button = QPushButton("Launch")
        layout.addWidget(launch_button)
        # launch_button.clicked.connect(self.launch_mode)

        open_button = QPushButton("open")
        layout.addWidget(open_button)
        # open_button.clicked.connect(self.show_app(self.layout))

        modeTab.setLayout(layout)
            
        return modeTab

        

    

    # wrap add_app and delete_app in def edit() so when they click edit, those two functions pop up
    # TO DO: condition
    # function for adding application to txt files
    def add_app(self, text, layout):
        value = text.text()
        index = self.tabs.currentIndex()
        layout.addWidget(QCheckBox(value))
        current_collection = self.tabs.tabText(index)
        with open(f"txt_files/{current_collection}.txt", "a") as f:
            f.write(f"{value}\n")
            # current_widget.layout.addWidget(QCheckBox(value))
    
    # TO DO: 'delete' functionality

    # launching functionality
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