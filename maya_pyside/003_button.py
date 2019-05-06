from PySide2 import QtWidgets
import maya.cmds as cmds

class MyWindow(QtWidgets.QDialog):


    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        layV = QtWidgets.QVBoxLayout(self)
        
        label = QtWidgets.QLabel('This is rad')
        layV.addWidget(label)
        
        btn = QtWidgets.QPushButton('PRESS ME')
        btn.clicked.connect( self.onClicked )
        layV.addWidget(btn)
        
    def onClicked(self):
        cmds.polyCube()
        

win = MyWindow()
win.show()
