"""
Convert the Square pipe mel exercice into python

polyPipe -r 1 -h 2 -t 0.5 -sa 4 -sh 1 -sc 0 -ax 0 1 0 -cuv 1 -rcp 0 -ch 1;
rotate -r -os -fo 0 45 0 ;
move -r 0 0.5 0 ;
xform -ws -sp 0 0 0 -rp 0 0 0;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
"""

import maya.cmds as cmds

cmds.polyPipe( r=1, h=2, t=0.5, sa=4, sh=1, sc=0, ax=(0,1,0), cuv=1, rcp=0, ch=1 )
cmds.rotate( 0, 45, 0, r=True, os=True, fo=True )
cmds.move( 0, 0.5, 0, r=True )
cmds.xform( ws=True, sp=(0,0,0), rp=(0,0,0) )
cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1 )

#This was a straight copy from the mel version.
#A lot of flags have their default values so they don't need to be called
# minimal version :
    
import maya.cmds as cmds

cmds.polyPipe( sa=4 )
cmds.rotate( 0, 45, 0 )
cmds.move( 0, 0.5, 0 )
cmds.xform( ws=True, sp=(0,0,0), rp=(0,0,0) )
cmds.makeIdentity( apply=True )

#Now the best version is to not rely on selection anymore

import maya.cmds as cmds

pipe = cmds.polyPipe( sa=4 )[0]
cmds.rotate( 0, 45, 0, pipe )
cmds.move( 0, 0.5, 0 , pipe)
cmds.xform( pipe, ws=True, sp=(0,0,0), rp=(0,0,0) )
cmds.makeIdentity(pipe, apply=True )
