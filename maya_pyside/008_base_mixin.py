from PySide2 import QtWidgets
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

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
        
def getControl(name, type=QtWidgets.QWidget):
    """Get a control
    
    Arguments:
        name {string} -- the name of the control to find
    
    Keyword Arguments:
        type {class} -- the class type to wrap the instance (default: {QtWidgets.QWidget})
    
    Returns:
        instance -- instance of the wrapped class
    """
    ptr = apiUI.MQtUtil.findControl(name)
    if ptr is not None:
        return shiboken2.wrapInstance(long(ptr), type)


class MyWindow(MayaQWidgetBaseMixin, QtWidgets.QPushButton):
    
    singleton_name = ""

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setText('MyAction')
        

mainPane = getControl("MainPane")
if mainPane != None:
    
    btn = MyWindow(mainPane)
    btn.move(300, 40)
    btn.show()
    MyWindow.singleton_name = btn.objectName()
    
    #find back the controller by it's name now
    foundBtn = getControl(MyWindow.singleton_name, QtWidgets.QPushButton)
    foundBtn.setText('ChangeActionName')


