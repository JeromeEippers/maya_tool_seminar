"""
Exercice
Use the widget hierarchy example to figure out how to find the main pane
"""


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
        
        
def findWidget(name, widget):
    if widget.objectName() == name:
        return widget
    for child in widget.children():
        found = findWidget(name, child)
        if found != None:
            return found
            

mainPane = findWidget( "MainPane", getMayaWindow() )
if mainPane != None:
    btn = QtWidgets.QPushButton('MyAction', mainPane)
    btn.move(5, 40)
    btn.show()