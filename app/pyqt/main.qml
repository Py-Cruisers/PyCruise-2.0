import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"
    Text {
        anchors.centerIn: parent
        text: "PyJet"
        font.pixelSize: 24
    }

    Button{
        y:70
        text : "Add Mode"
        onClicked: {
            print("Hello")
        }
    }
}