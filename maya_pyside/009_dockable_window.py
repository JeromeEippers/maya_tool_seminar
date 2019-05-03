from PySide2 import QtWidgets
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class MyWindow(MayaQWidgetDockableMixin, QtWidgets.QWidget):


    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle('My Dockable Window')
        lay = QtWidgets.QVBoxLayout(self)
        
        
        label = QtWidgets.QLabel('label1')
        lay.addWidget(label)
        
        label = QtWidgets.QLabel('label2')
        lay.addWidget(label)

        

win = MyWindow()
win.show(dockable=True)
