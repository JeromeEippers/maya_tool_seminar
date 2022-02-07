import yaml
import pymel.core as pm
import os
from SceneImporter import SceneImporter

def load( assetPath, scenePath ):
	
	metaGuids = dict()
	for dirPath, dirs, files in os.walk( assetPath ):
		for filePath in files:
			if '.meta' in filePath:
				fullpath = os.path.join( dirPath, filePath )
				with open(fullpath) as f:
					yaml_meta = yaml.safe_load(f)
					guid = yaml_meta['guid']
					metaGuids[guid] = fullpath[:-5]
	
	
	unityScenePath = os.path.join( assetPath, scenePath )
	sceneRoot = pm.createNode( 'transform', name = 'sceneRoot')
	sceneRoot.scale.set([-1,1,1])
	SceneImporter().spawn(unityScenePath, sceneRoot, metaGuids)
		
		
		
		
		
		
		
		
		