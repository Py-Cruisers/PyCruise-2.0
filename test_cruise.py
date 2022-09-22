import pytest
# import PyQt6
import app.main
from pytestqt import qtbot
def test_123():
    assert "testing testing 123"

# @pytest.mark.skip
def test_window_title(qtbot):
    window = app.main.Window()
    window.show()
    
    assert window.windowTitle == "PyCruise"


@pytest.mark.skip
def test_hello(qtbot):

    window = main.Window()
    window.show()
    qtbot.addWidget(window)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.button_greet, QtCore.Qt.LeftButton)

    assert widget.greet_label.text() == "Hello!"