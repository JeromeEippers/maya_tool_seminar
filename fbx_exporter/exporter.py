from PySide2 import QtWidgets, QtGui
import maya.cmds as cmds
import maya.mel as mel
import os
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
        
        layName = QtWidgets.QVBoxLayout(self)
        layName.setContentsMargins(10,0,10,0)
        
        label = QtWidgets.QLabel("Rig Name :", self)
        layName.addWidget(label)
        
        self.rigName = QtWidgets.QLineEdit('', self)
        self.rigName.setPlaceholderText("Rig Name")
        layName.addWidget(self.rigName)
        lay.addLayout(layName)
        
        label = QtWidgets.QLabel("Rig Export :", self)
        lay.addWidget(label)
        
        self._exportRig = QtWidgets.QCheckBox("Export Rig", self)
        lay.addWidget(self._exportRig)
        
        
        self.rigRoot = MayaPickerWidget("Rig Root Object", parent=self)
        lay.addWidget(self.rigRoot)
        
        
        label = QtWidgets.QLabel("Anim Export :", self)
        lay.addWidget(label)
        
        self._exportAnim = QtWidgets.QCheckBox("Export Anim", self)
        lay.addWidget(self._exportAnim)
        
        label = QtWidgets.QLabel("Anim Name :", self)
        lay.addWidget(label)
        
        self._animName = QtWidgets.QLineEdit("", self)
        lay.addWidget(self._animName)
        
        self.animRoot = MayaPickerWidget("Anim Root Object", parent=self)
        lay.addWidget(self.animRoot)
        
        label = QtWidgets.QLabel("start frame :", self)
        lay.addWidget(label)
        
        self._startFrame = QtWidgets.QLineEdit("", self)
        lay.addWidget(self._startFrame)
        
        label = QtWidgets.QLabel("end frame :", self)
        lay.addWidget(label)
        
        self._endFrame = QtWidgets.QLineEdit("", self)
        lay.addWidget(self._endFrame)
        
        lay.addStretch()
        
        btn = QtWidgets.QPushButton("EXPORT", self)
        btn.clicked.connect(self.onExport)
        lay.addWidget(btn)
        

    def onExport(self):
        exportFolder = os.path.normpath ( str( self.rootFolder._line.text() ) )
        rigRoot = str( self.rigRoot._line.text() )
        rigName = str( self.rigName.text() )
        animName = str( self._animName.text() )
        animRoot = str( self.animRoot._line.text() )
        startFrame = int( self._startFrame.text() )
        endFrame = int( self._endFrame.text() )
        
        print startFrame,  endFrame
        
        if exportFolder and rigRoot and rigName and self._exportRig.isChecked() :
            print "EXPORTING RIG", rigName
            
            cmds.select( rigRoot )
            
            filePath = os.path.join(exportFolder, rigName+ '.fbx')
            
            mel.eval('FBXExportAnimationOnly -v false')       
            mel.eval('FBXExportBakeComplexAnimation -v true')
            mel.eval('FBXExportBakeComplexStart -v 0')
            mel.eval('FBXExportBakeComplexEnd -v 0')
            mel.eval('FBXExportBakeResampleAnimation -v true')
            mel.eval('FBXExportConstraints -v false')
            mel.eval('FBXExportInputConnections -v false')
            mel.eval('FBXExportSkeletonDefinitions -v true')
            mel.eval('FBXExportSkins -v true')
            mel.eval('FBXExport -f "{0}" -s'.format( filePath.replace('\\', '/') ) )
            
        else:
            print "DO NOT EXPORT RIG"
            
        
        if exportFolder and animRoot and rigName and animName and self._exportAnim.isChecked() :
            print "EXPORTING ANIM", rigName, animName
            
            cmds.select( animRoot )
            
            filePath = os.path.join(exportFolder, rigName + '@' + animName + '.fbx')
            
            mel.eval('FBXExportAnimationOnly -v false')       
            mel.eval('FBXExportBakeComplexAnimation -v true')
            mel.eval('FBXExportBakeComplexStart -v {0}'.format(startFrame))
            mel.eval('FBXExportBakeComplexEnd -v {0}'.format(endFrame))
            mel.eval('FBXExportBakeResampleAnimation -v true')
            mel.eval('FBXExportConstraints -v false')
            mel.eval('FBXExportInputConnections -v false')
            mel.eval('FBXExportSkeletonDefinitions -v true')
            mel.eval('FBXExportSkins -v true')
            mel.eval('FBXExport -f "{0}" -s'.format( filePath.replace('\\', '/') ) )
        

        

win = MyWindow()
win.show(dockable=True)
