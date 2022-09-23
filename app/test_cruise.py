from termios import TAB3
import pytest
# import PyQt6
import main
from pytestqt import qtbot 
from PyQt6 import QtCore
from PyQt6.QtCore import Qt

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


def test_123():
    assert "testing testing 123"

# def test_window_title(qtbot):
#     window = main.Window()
#     assert window.windowTitle == "PyCruise"

# @pytest.mark.skip
def test_create_new_mode_button(qtbot):
    window = main.Window()
    qtbot.mouseClick(window.create_new_mode_button, QtCore.Qt.MouseButton.LeftButton)

    assert window.mode_form.rowCount() == 1

# @pytest.mark.skip
def test_edit_button(qtbot):
    window = main.Window()
    tab = main.Tab()
    qtbot.mouseClick(tab.edit_button, QtCore.Qt.MouseButton.LeftButton)

    assert window.mode_form.rowCount() == 2




