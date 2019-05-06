from PySide2 import QtWidgets, QtGui
import maya.cmds as cmds
import maya.mel as mel
import os
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class GroupText(QtWidgets.QWidget):
    """Group text create a line edit inside a groupbox"""
    
    def __init__(self, label, text="", placeHolderText="", parent=None):
        super(GroupText, self).__init__(parent)
        
        layV = QtWidgets.QVBoxLayout(self)
        self.setLayout(layV)
        layV.setContentsMargins(0,0,0,0)
        
        grp = QtWidgets.QGroupBox(label, self)
        layV.addWidget(grp)
        
        layH = QtWidgets.QHBoxLayout(self)
        layH.setContentsMargins(2,0,2,0)
        grp.setLayout(layH)
        
        self._line = QtWidgets.QLineEdit(text, self)
        self._line.setPlaceholderText(placeHolderText)
        layH.addWidget(self._line,100)

        layV.addStretch()
        
    def line(self):
        return self._line


class AbstractPickerWidget(QtWidgets.QWidget):
    """Base class for a picker
    You have to implement the onClicked method"""

    def __init__(self, label, text="", placeHolderText="", btnText="", iconBtn="", parent=None):
        super(AbstractPickerWidget, self).__init__(parent)
        
        layV = QtWidgets.QVBoxLayout(self)
        self.setLayout(layV)
        layV.setContentsMargins(0,0,0,0)
        
        
        grp = QtWidgets.QGroupBox(label, self)
        layV.addWidget(grp)
        
        layH = QtWidgets.QHBoxLayout(self)
        layH.setContentsMargins(2,0,2,0)
        grp.setLayout(layH)
               
        self._line = QtWidgets.QLineEdit(text, self)
        self._line.setPlaceholderText(placeHolderText)
        layH.addWidget(self._line,100)

        if iconBtn:
            icon = QtGui.QIcon(iconBtn)
            btn = QtWidgets.QPushButton(icon, btnText)
        else:
            btn = QtWidgets.QPushButton(btnText)
        btn.clicked.connect( self.onClicked )
        layH.addWidget(btn,1)
        
        layV.addStretch()
        
    def line(self):
        return self._line
        
    def onClicked(self):
        pass
            
          
            
class MayaPickerWidget( AbstractPickerWidget ):
    """Maya picker widget
    This allows to quicly pick an object in Maya"""
    
    def __init__(self, label, text="", placeHolderText="", btnText="", iconBtn="", parent=None):
        placeHolderText= placeHolderText or "Pick Maya Object"
        btnText = btnText or "<"
        super(MayaPickerWidget, self).__init__(label, text, placeHolderText, btnText, iconBtn, parent)
    
    def onClicked(self):
        selection = cmds.ls(sl=True)
        if selection:
            self._line.setText(selection[0])
        
        
        
class FolderPickerWidget( AbstractPickerWidget ):
    """Folder picker widget
    pick a folder on the disk"""
    
    def __init__(self, label, text="", placeHolderText="", btnText="", iconBtn="", parent=None):
        iconBtn = iconBtn or ":/folder-closed.png"
        placeHolderText= placeHolderText or "Select Folder"
        super(FolderPickerWidget, self).__init__(label, text, placeHolderText, btnText, iconBtn, parent)
    
    def onClicked(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory( self, "Select Folder" )
        self._line.setText(dir)


class MyWindow(MayaQWidgetDockableMixin, QtWidgets.QWidget):
    """Main exporter widget"""
    
    SAVE_OBJ = "exporter_options"
    
    def __init__(self, parent=None):
        """Set the layout"""
        
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("Exporter")
        
        lay = QtWidgets.QVBoxLayout(self)
        
        
        self.rootFolder = FolderPickerWidget("Export Folder")
        lay.addWidget(self.rootFolder)
        
        self.rigName = GroupText("Rig Name")
        self.rigName.line().textChanged.connect(self._canExportValidator)
        lay.addWidget(self.rigName)
        
        self.exportRig = QtWidgets.QGroupBox("Export Rig")
        self.exportRig.setCheckable(True)
        self.exportRig.setChecked(False)
        self.exportRig.toggled.connect(self._canExportValidator)
        groupLayout = QVBoxLayout(self)
        self.exportRig.setLayout(groupLayout)
        lay.addWidget(self.exportRig)
        
        self.rigRoot = MayaPickerWidget("Rig Root Object")
        self.rigRoot.line().textChanged.connect(self._canExportValidator)
        groupLayout.addWidget(self.rigRoot)
        
        self.exportAnim = QtWidgets.QGroupBox("Export Animation")
        self.exportAnim.setCheckable(True)
        self.exportAnim.toggled.connect(self._canExportValidator)
        groupLayout = QVBoxLayout(self)
        self.exportAnim.setLayout(groupLayout)
        lay.addWidget(self.exportAnim)
        
        self.animName = GroupText("Animation Name")
        self.animName.line().textChanged.connect(self._canExportValidator)
        groupLayout.addWidget(self.animName)
        
        self.animRoot = MayaPickerWidget("Anim Root Object")
        self.animRoot.line().textChanged.connect(self._canExportValidator)
        groupLayout.addWidget(self.animRoot)
        
        self.startFrame = GroupText("start frame", text="0")
        self.startFrameValidator = QtGui.QIntValidator()
        self.startFrame.line().setValidator(self.startFrameValidator)
        self.startFrame.line().textChanged.connect(self._canExportValidator)
        groupLayout.addWidget(self.startFrame)

        self.endFrame = GroupText("end frame", text="30")
        self.endFrameValidator = QtGui.QIntValidator()
        self.endFrame.line().setValidator(self.endFrameValidator)
        self.endFrame.line().textChanged.connect(self._canExportValidator)
        groupLayout.addWidget(self.endFrame)
        
        lay.addStretch(2000)
        
        buttonsLayout = QtWidgets.QHBoxLayout(self)
        lay.addLayout(buttonsLayout)
        
        
        self.saveBtn = QtWidgets.QPushButton("Save")
        self.saveBtn.clicked.connect(self.onSave)
        buttonsLayout.addWidget(self.saveBtn)
        
        self.exportBtn = QtWidgets.QPushButton("EXPORT")
        self.exportBtn.clicked.connect(self.onExport)
        buttonsLayout.addWidget(self.exportBtn,100)
        
        self._canExportValidator()
        
        
    def _canExportValidator(self, event=None):
        """call back on all modification, so we can enable the export button"""
        self.exportBtn.setEnabled(self.canExport())
        
        
    def options(self):
        """return the options of the tool as a dictionary"""
        
        return {
            'export_folder' : ( str( self.rootFolder.line().text() )).replace('\\', '/'),
            'rig_name' : str( self.rigName.line().text() ),
            
            'export_rig' : self.exportRig.isChecked(),
            'rig_root' : str( self.rigRoot.line().text() ),
            
            'export_animation' : self.exportAnim.isChecked(),
            'animation_name' : str( self.animName.line().text() ),
            'animation_root' : str( self.animRoot.line().text() ),
            'startFrame' : int( self.startFrame.line().text() ),
            'endFrame' : int( self.endFrame.line().text() )
        }
        
        
    def canExport(self, options=None):
        """check if we can export something using the options from the tool, or from a specific set of options"""
        
        options = options or self.options()
        
        if options['export_folder'] == '' or options['rig_name'] == '':
            return False
            
        if options['export_rig'] == False and options['export_animation'] == False:
            return False
            
        if options['export_rig'] == True:
            if options['rig_root'] == '':
                return False
                
        if options['export_animation'] == True:
            if options['animation_name'] == '' or options['animation_root'] == '':
                return False
                
        return True
        
        
    def export_fbx(self, path, root, startFrame=0, endFrame=0):
        """Export an FBX file"""
        
        cmds.select( root )
        
        mel.eval('FBXExportAnimationOnly -v false')       
        mel.eval('FBXExportBakeComplexAnimation -v true')
        mel.eval('FBXExportBakeComplexStart -v {0}'.format(startFrame))
        mel.eval('FBXExportBakeComplexEnd -v {0}'.format(endFrame))
        mel.eval('FBXExportBakeResampleAnimation -v true')
        mel.eval('FBXExportConstraints -v false')
        mel.eval('FBXExportInputConnections -v false')
        mel.eval('FBXExportSkeletonDefinitions -v true')
        mel.eval('FBXExportSkins -v true')
        mel.eval('FBXExport -f "{0}" -s'.format( path.replace('\\', '/') ) )
        

    def onExport(self, options=None):
        """export using the options from the tool, or from a specific set of options"""
        
        options = options or self.options()
        
        if self.canExport( options ):
            
            folder = os.path.normpath ( options['export_folder'] )
            
            if options['export_rig']:
                path = os.path.join(folder, options['rig_name'] + '.fbx')
                self.export_fbx(path, options['rig_root'])
                
            if options['export_animation']:
                path = os.path.join(folder, options['rig_name'] + '@' + options['animation_name'] + '.fbx')
                self.export_fbx(path, options['animation_root'], options['startFrame'], options['endFrame'])
            
            
    def onSave(self):
        """saving the options in the file"""
        if cmds.objExists( self.SAVE_OBJ ):
            cmds.delete(self.SAVE_OBJ)
            
        node = cmds.createNode('transform', name=self.SAVE_OBJ)
        cmds.addAttr( node, longName='options', dt='string' )
        cmds.setAttr( node + '.options', str(self.options()), type='string' )
        
        

win = MyWindow()
win.show(dockable=True)
