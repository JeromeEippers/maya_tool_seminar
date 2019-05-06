from PySide2 import QtWidgets

class MyWindow (QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        lay = QtWidgets.QVBoxLayout(self)
        layH = QtWidgets.QHBoxLayout(self)
        lay.addLayout(layH)
        
        label = QtWidgets.QLabel('hello', self)
        layH.addWidget(label)
        
        label = QtWidgets.QLabel('world', self)
        layH.addWidget(label)
        
        label = QtWidgets.QLabel('this is rad', self)
        lay.addWidget(label)
        
        
    
win = MyWindow()
win.show()
