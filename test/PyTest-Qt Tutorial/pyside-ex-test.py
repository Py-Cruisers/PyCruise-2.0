# Test pyside-ex-findfiles.py's basic functionality

def test_basic_search(qtbot, tmpdir):
    '''
    test to ensure basic find files functionality is working.
    '''
    tmpdir.join('video1.avi').ensure()
    tmpdir.join('video1.srt').ensure()

    tmpdir.join('video2.avi').ensure()
    tmpdir.join('video2.srt').ensure()

    window = Window()
    window.show()
    qtbot.addWidget(window)

    window.fileComboBox.clear()
    qtbot.keyClicks(window.fileComboBox, '*.avi')

    window.directoryComboBox.clear()
    qtbot.keyClicks(window.directoryComboBox, str(tmpdir))

    qtbot.mouseClick(window.findButton, QtCore.Qt.LeftButton)

    assert window.filesTable.rowCount() == 2
    assert window.filesTable.item(0, 0).text() == 'video1.avi'
    assert window.filesTable.item(1, 0).text() == 'video2.avi'


def test_hello(qtbot):
    widget = HelloWidget()
    qtbot.addWidget(widget)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.button_greet, QtCore.Qt.LeftButton)

    assert widget.greet_label.text() == "Hello!"