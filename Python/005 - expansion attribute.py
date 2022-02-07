"""
Create an expansion attribute on the first selected object.
Then for each following selected object create a locator at the original position (parent it under an empty group)
And create a point constraint on the selected object with the first object and the locator as targets.
And finally connect the attribute to the weights.
"""

import maya.cmds as cmds

selectionList = cmds.ls( orderedSelection=True, type='transform' )

if len( selectionList ) >= 2:
    
    #find the target in the list and remove it from the list
    targetName = selectionList[0]
    selectionList = selectionList[1:]
    
    #create the group for the locators
    locatorGroupName = cmds.createNode("transform", name="locators_grp")
    
    #create the expansion attribute if not already existing
    maxExpansion = 100
    newAttributeName = 'expansion'
    if not cmds.objExists( '{0}.{1}'.format( targetName, newAttributeName ) ):
        
        cmds.addAttr( targetName, longName=newAttributeName, shortName='exp',
                      attributeType='double', min=0, max=maxExpansion,
                      defaultValue=maxExpansion, keyable=True )
            
    #create the inverse math nodes if not already existing          
    inverseExpansionName = targetName + '_expansion_inverse_node'
    if not cmds.objExists(inverseExpansionName):
        
        #create the node
        inverseExpansionName = cmds.shadingNode('floatMath', asUtility=True, name=inverseExpansionName)
        #set the values
        cmds.setAttr( '{0}.floatA'.format(inverseExpansionName), maxExpansion )
        cmds.setAttr( '{0}.operation'.format(inverseExpansionName), 1 )
        #connect the attribute
        cmds.connectAttr( '{0}.{1}'.format( targetName, newAttributeName ), 
                          '{0}.floatB'.format(inverseExpansionName) )
    
    for objectName in selectionList:
        
        coords = cmds.getAttr( '{0}.translate'.format ( objectName ) )[0]
        
        locatorName = cmds.spaceLocator( position=coords, name='{0}_loc'.format( objectName ) )[0]
        cmds.xform(locatorName, cp=True)
        locatorName = cmds.parent(locatorName, locatorGroupName)[0]
        
        pointConstraintName = cmds.pointConstraint( [ targetName, locatorName ], objectName, name='{0}_pointConstraint'.format( objectName ) )[0]
       
        cmds.connectAttr( '{0}.outFloat'.format(inverseExpansionName), 
                          '{0}.{1}W0'.format( pointConstraintName, targetName ) )
                          
        cmds.connectAttr( '{0}.{1}'.format( targetName, newAttributeName ), 
                          '{0}.{1}W1'.format( pointConstraintName, locatorName ) )
        
    
else:
    
    print 'Please select two or more objects.'