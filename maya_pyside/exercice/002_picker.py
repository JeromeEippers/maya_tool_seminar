from PySide2 import QtWidgets
import maya.cmds as cmds

class MyWindow(QtWidgets.QDialog):


    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        lay = QtWidgets.QHBoxLayout(self)
        
        self._line = QtWidgets.QLineEdit('', self)
        self._line.setPlaceholderText('Enter Object Name')
        lay.addWidget(self._line,100)
        
        btn = QtWidgets.QPushButton('<')
        btn.clicked.connect( self.onClicked )
        lay.addWidget(btn,1)
        
    def onClicked(self):
        selection = cmds.ls(sl=True)
        if selection:
            self._line.setText(selection[0])
        

win = MyWindow()
win.show()
