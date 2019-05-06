from PySide2 import QtWidgets, QtGui
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

class AbstractPickerWidget(QtWidgets.QWidget):

    def __init__(self, label, placeHolderText="", btnText="", iconBtn="", parent=None):
        super(AbstractPickerWidget, self).__init__(parent)
        
        layV = QtWidgets.QVBoxLayout(self)
        layH = QtWidgets.QHBoxLayout(self)
        
        label = QtWidgets.QLabel(label + " :", self)
        layV.addWidget(label)
        layV.addLayout(layH)
        layV.addStretch()
        
        self._line = QtWidgets.QLineEdit('', self)
        self._line.setPlaceholderText(placeHolderText)
        layH.addWidget(self._line,100)
        
        if iconBtn:
            icon = QtGui.QIcon(iconBtn)
            btn = QtWidgets.QPushButton(icon, btnText)
        else:
            btn = QtWidgets.QPushButton(btnText)
        btn.clicked.connect( self.onClicked )
        layH.addWidget(btn,1)
        
    def onClicked(self):
        pass
            
          
            
class MayaPickerWidget( AbstractPickerWidget ):
    
    def __init__(self, label, placeHolderText="", btnText="", iconBtn="", parent=None):
        placeHolderText= placeHolderText or "Pick Maya Object"
        btnText = btnText or "<"
        super(MayaPickerWidget, self).__init__(label, placeHolderText, btnText, iconBtn, parent)
    
    def onClicked(self):
        selection = cmds.ls(sl=True)
        if selection:
            self._line.setText(selection[0])
        
        
class FolderPickerWidget( AbstractPickerWidget ):
    
    def __init__(self, label, placeHolderText="", btnText="", iconBtn="", parent=None):
        iconBtn = iconBtn or ":/folder-closed.png"
        placeHolderText= placeHolderText or "Select Folder"
        super(FolderPickerWidget, self).__init__(label, placeHolderText, btnText, iconBtn, parent)
    
    
    def onClicked(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory( self, "Select Folder" )
        self._line.setText(dir)


class MyWindow(MayaQWidgetDockableMixin, QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("Exporter")
        
        lay = QtWidgets.QVBoxLayout(self)
        
        
        self.rootFolder = FolderPickerWidget("Export Folder", parent=self)
        lay.addWidget(self.rootFolder)
        
        label = QtWidgets.QLabel("Rig Export :", self)
        lay.addWidget(label)
        
        layName = QtWidgets.QVBoxLayout(self)
        layName.setContentsMargins(10,0,10,0)
        
        label = QtWidgets.QLabel("Rig Name :", self)
        layName.addWidget(label)
        
        self.rigName = QtWidgets.QLineEdit('', self)
        self.rigName.setPlaceholderText("Rig Name")
        layName.addWidget(self.rigName)
        lay.addLayout(layName)
        
        
        self.rigRoot = MayaPickerWidget("Rig Root Object", parent=self)
        lay.addWidget(self.rigRoot)
        
        lay.addStretch()
        
        btn = QtWidgets.QPushButton("EXPORT", self)
        btn.clicked.connect(self.onExport)
        lay.addWidget(btn)
        

    def onExport(self):
        print "EXPORT"
        
        

        

win = MyWindow()
win.show(dockable=True)
