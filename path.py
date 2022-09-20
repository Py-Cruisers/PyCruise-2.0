import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui

class Window(widgets.QWidget):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("App")

    form_layout = widgets.QFormLayout()
    self.setLayout(form_layout)

    #add stuff
    label_1 = widgets.QLabel("APP Name")
    label_1.setFont(gui.QFont("Helvetica", 24))
    f_name = widgets.QLineEdit(self)
    l_name = widgets.QLineEdit(self)

    #add rows to app
    form_layout.addRow(label_1)
    form_layout.addRow("App Name", f_name)
    form_layout.addRow("Description", l_name)
    form_layout.addRow(widgets.QPushButton("Create New Mode",
        clicked = lambda: create_it()
    ))
    form_layout.addRow(widgets.QPushButton("Select",
        clicked = lambda: select_it()
    ))
    form_layout.addRow(widgets.QPushButton("View Mode",
        clicked = lambda: view_it()
    ))
    
    
    #show app
    self.show()
    def create_it():
        label_1.setText(f'You clicked button, {f_name.text()}!')
    
    def select_it():
        label_1.setText("selectNode")

        for i in reversed(range(layout.count())): 
          layout.itemAt(i).widget().setParent(None

    def view_it():
        label_1.setText(f'You clicked button, {f_name.text()}!')
    
app = widgets.QApplication([])
mw = Window()
app.exec()
     