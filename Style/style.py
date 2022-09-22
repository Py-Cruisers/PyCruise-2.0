import sys
import os
import webbrowser

from PyQt6.QtCore import Qt
import fnmatch
from pathlib import Path
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion, QPalette, QColor
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
    QLabel,
    QMainWindow,
    QStackedLayout
)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QStackedLayout()

        layout.addWidget(Color('#191D32'))
        layout.addWidget(Color('#453A49'))
        layout.addWidget(Color('#6D3B47'))
        layout.addWidget(Color('#BA2C73'))
        
        layout.setCurrentIndex(3)
        
        

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()