import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 300
    height: 200
    title: "HelloApp"
        Image {
            sourceSize.width: 100
            sourceSize.height: 100
            source: "/Users/brentice/Desktop/app/pyqt/rocket-1.png"
        
        }

    Text {
        text: "PyJet"
        anchors.leftMargin: 12
        text: qsTr("heading text")
        font.pixelSize: 36
        font.bold: true
    }
}