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


label = QtWidgets.QLabel('MY_LABEL', getMayaWindow())
label.show()