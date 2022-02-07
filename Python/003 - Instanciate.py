"""
randomly instanciate one object 20 times
reparenting all the instances under one group
and hidding the original object
"""
import maya.cmds as cmds
import random

#custom seed, so we have repetitivity
random.seed(1234)

#get selection
selection = cmds.ls(sl=True)
if len(selection)!=1:
    raise Exception("please select one object")

objectToInstanciate = selection[0]
cmds.showHidden(objectToInstanciate)
#create an empty group
emptyGroup = cmds.createNode("transform", name="Instances_grp")

#loop 
for i in range(20):
    
    #instanciante
    inst = cmds.instance(objectToInstanciate)[0]
    
    #reparent the intance under the group
    inst = cmds.parent(inst, emptyGroup)[0]
    
    #random position
    x = random.uniform(-10,10)
    y = random.uniform(-10,10)
    z = random.uniform(-10,10)
    cmds.move(x,y,z, inst)
    
    #random rotation
    x = random.uniform(0,360)
    y = random.uniform(0,360)
    z = random.uniform(0,360)
    cmds.rotate(x,y,z, inst)
    
    #random scale
    x = random.uniform(0.8, 1.2)
    cmds.scale(x,x,x, inst)
    
cmds.hide(objectToInstanciate)


