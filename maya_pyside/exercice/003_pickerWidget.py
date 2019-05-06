from PySide2 import QtWidgets
import maya.cmds as cmds

class Picker(QtWidgets.QWidget):

    def __init__(self, label, parent=None):
        super(Picker, self).__init__(parent)
        
        layV = QtWidgets.QVBoxLayout(self)
        layH = QtWidgets.QHBoxLayout(self)
        
        label = QtWidgets.QLabel(label + " :", self)
        layV.addWidget(label)
        layV.addLayout(layH)
        layV.addStretch()
        
        self._line = QtWidgets.QLineEdit('', self)
        self._line.setPlaceholderText('Enter Object Name')
        layH.addWidget(self._line,100)
        
        btn = QtWidgets.QPushButton('<')
        btn.clicked.connect( self.onClicked )
        layH.addWidget(btn,1)
        
    def onClicked(self):
        selection = cmds.ls(sl=True)
        if selection:
            self._line.setText(selection[0])
            
    def selection(self):
        return str( self._line.text() )
        


class MyWindow(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        lay = QtWidgets.QVBoxLayout(self)
        
        picker = Picker("root", self)
        lay.addWidget(picker)
        
        picker = Picker("sub object", self)
        lay.addWidget(picker)
        

win = MyWindow()
win.show()
