import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"
        Image {
            sourceSize.width: 344
            sourceSize.height: 344
            source: "/Users/brentice/Desktop/app/pyqt/rocket-1.png"
            fillMode: Image.PreserveAspectCrop
        }
    Text {
        anchors.centerIn: parent
        text: "PyJet"
        font.pixelSize: 24
    }
}