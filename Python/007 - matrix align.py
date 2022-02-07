import maya.cmds as cmds
import maya.api.OpenMaya as OM

def transformMatrix(obj):
    m = cmds.xform(obj, q=True, ws=True, m=True)
    return OM.MMatrix(m)
    
def setTransformMatrix(obj, m):
    cmds.xform(obj, ws=True, m=m)

a,b,c = cmds.ls(sl=True)
am = transformMatrix(a)
bm = transformMatrix(b)
cm = transformMatrix(c)

local = am.inverse() * bm
result = cm * local
setTransformMatrix(b, result)