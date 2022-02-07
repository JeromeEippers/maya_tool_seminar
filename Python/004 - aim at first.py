"""
create a aim constraint with the target being the first selected element
"""

import maya.cmds as cmds

selection = cmds.ls( os=True )
if len(selection)>=2:
    
    target = selection[0]
    selection = selection[1:]
    
    for sel in selection:
        cmds.aimConstraint(target, sel, aimVector=(0,-1,0))