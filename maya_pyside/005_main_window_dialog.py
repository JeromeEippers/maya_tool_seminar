from PySide2 import QtWidgets

import shiboken2
import maya.OpenMayaUI as apiUI

def getMayaWindow():
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """
    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)
        


class MyWindow(QtWidgets.QDialog):


    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        lay = QtWidgets.QVBoxLayout(self)
        
        
        label = QtWidgets.QLabel('label1')
        lay.addWidget(label)
        
        label = QtWidgets.QLabel('label2')
        lay.addWidget(label)

        

win = MyWindow( getMayaWindow() )
win.show()