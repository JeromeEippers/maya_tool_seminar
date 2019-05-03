from PySide2 import QtWidgets

class MyWindow(QtWidgets.QDialog):


    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        label = QtWidgets.QLabel('label1', self)
        label.move(10,10)
        label = QtWidgets.QLabel('label2', self)
        label.move(20,30)

        

win = MyWindow()
win.show()
