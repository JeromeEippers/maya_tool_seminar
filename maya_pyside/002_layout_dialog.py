from PySide2 import QtWidgets

class MyWindow(QtWidgets.QDialog):


    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        lay = QtWidgets.QVBoxLayout(self)
        
        
        label = QtWidgets.QLabel('label1')
        lay.addWidget(label)
        
        label = QtWidgets.QLabel('label2')
        lay.addWidget(label)

        

win = MyWindow()
win.show()