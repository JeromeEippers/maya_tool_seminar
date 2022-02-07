import maya.cmds as cmds
import maya.api.OpenMaya as om

class Controller(object):
    
    def __init__(self, name, matrix=[1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]):
        self.name = name
        self.matrix = list(matrix)
        
    def isParentOf(self, other):        
        def isparent (child):
            p = cmds.listRelatives(child, parent=True, fullPath=True)
            if p and p[0] != None:
                pname = p[0].split('|')[-1]
                if self.name == pname:
                    return True
                return isparent(p)
            return False
        return isparent(other.name)


class Pose(object):
    
    class RotType:
        Full = 0
        ZOnly = 1
        NoRot = 2
    
    def __init__(self):
        self.controllers = list()
        
    def findController(self, name):
        for ctrl in self.controllers:
            if ctrl.name == name:
                return ctrl
        return None
        
    def store(self):
        
        #store all the matrices
        self.controllers = list()
        for node in cmds.ls("*_ctrl"):
            if 'Left' not in node and 'Right' not in node:
                matrix = self.getMatrix(node)
                self.controllers.append( Controller(node, matrix) )
            
        #sort the controllers
        for i in range(len(self.controllers)):
            for j in range(i+1, len(self.controllers)):
                if self.controllers[j].isParentOf(self.controllers[i]):
                    self.controllers[i], self.controllers[j] = self.controllers[j], self.controllers[i]
    
    def convertToMMatix(self, matrix, rotation=RotType.Full):
        if rotation == self.RotType.Full:
            return om.MMatrix( matrix )
        if rotation == self.RotType.NoRot:
            m = [1,0,0,0, 0,1,0,0, 0,0,1,0] + matrix[12:15] + [1]
            return om.MMatrix(m)
        vector = om.MVector(matrix[8:11])
        up = om.MVector([0,1,0])
        x = (up ^ vector).normal()
        z = (x ^ up).normal()
        m = list(x)+[0] + list(up)+ [0] + list(z)+ [0] + matrix[12:15] + [1]
        return om.MMatrix(m)
    
    
    def getMatrix(self, name):
        node = cmds.createNode('transform', name='get_'+name)
        cmds.delete(cmds.parentConstraint(name, node))
        matrix = cmds.xform(node, q=True, ws=True, m=True)
        #cmds.delete(node)
        return matrix
    
    def applyMatrix(self, name, matrix):
        node = cmds.createNode('transform', name='apply_'+name)
        cmds.xform(node, ws=True, m=matrix)
        cmds.delete(cmds.parentConstraint(node, name))
        #cmds.delete(node)
    
    
    def paste(self, relativeTo='', rotation=RotType.Full, mirror=False):
        
        matrices = [om.MMatrix(ctrl.matrix) for ctrl in self.controllers]
        
        if mirror == True:
            scaleX = om.MTransformationMatrix()
            scaleX.setScale([-1,1,1], 2)
            scaleX = scaleX.asMatrix()
            scaleZ = om.MTransformationMatrix()
            scaleZ.setScale([1,1,-1], 2)
            scaleZ = scaleZ.asMatrix()
            for i in range(len(matrices)):
                matrices[i] = matrices[i] * scaleX
            
        
        if relativeTo == '':
            for ctrl, matrix in zip( self.controllers, matrices):
                self.applyMatrix(ctrl.name, matrix)
        
        else:
            relativeController = self.findController(relativeTo)
            if relativeController==None:
                raise Exception("relative node not in pose")
                
            previousMMatrix = self.convertToMMatix( list(matrices[self.controllers.index(relativeController)]), rotation )
            currentMMatrix = self.convertToMMatix( self.getMatrix(relativeTo), rotation )
            convertMMatrix = previousMMatrix.inverse() * currentMMatrix
            
            for ctrl, matrix in zip( self.controllers, matrices):
                ctrlMMatrix = matrix * convertMMatrix
                self.applyMatrix(ctrl.name, ctrlMMatrix)
                
        