"""
Create a 5 side beveled polygon with curve.
Use the usual inspection method with the script editor
"""

import maya.cmds as cmds

pipe = cmds.polyCylinder(h=0.1, sx=5, sc=1)[0]
cmds.move(0, 0.2, 0, "{0}.vtx[10:11]".format(pipe))
cmds.polyBevel3(pipe, fraction=0.5, offsetAsFraction=True)