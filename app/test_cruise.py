import pytest
# import PyQt6
import main
from pytestqt import qtbot 
from PyQt6 import QtCore
from PyQt6.QtCore import Qt


def test_123():
    assert "testing testing 123"

# @pytest.mark.skip
def test_window_title(qtbot):
    window = main.Window()
    qtbot.mouseClick(window.create_new_mode_button, QtCore.Qt.LeftButton)

    assert window.layout == "PyCruise"


@pytest.mark.skip
def test_hello(qtbot):

    window = main.Window()
    window.show()
    qtbot.addWidget(window)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.button_greet, QtCore.Qt.LeftButton)

    assert widget.greet_label.text() == "Hello!"