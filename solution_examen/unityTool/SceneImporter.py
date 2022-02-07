import yaml
import pymel.core as pm
import pymel.util as ut
import UnityYamlStream as uys
import dataType as dt
import os

class SceneImporter( object ):
	
	def spawn(self, scenePath, sceneRoot, metaGuids):
		
		unityFile = dt.File()
		
		stream = uys.UnityYamlStream( scenePath )
		for node in yaml.safe_load_all( stream ):
			if 'GameObject' in node:
				comp = dt.GameObject(stream.lastFileID(), node.values()[0], unityFile)
				unityFile.addComponent(comp)
				
			if 'Transform' in node:
				comp = dt.Transform(stream.lastFileID(), node.values()[0], unityFile)
				unityFile.addComponent(comp)
			
			if 'BoxCollider' in node:
				comp = dt.BoxCollider(stream.lastFileID(), node.values()[0], unityFile)
				unityFile.addComponent(comp)
				
			if 'SphereCollider' in node:
				comp = dt.SphereCollider(stream.lastFileID(), node.values()[0], unityFile)
				unityFile.addComponent(comp)
				
			if 'Prefab' in node:
				comp = dt.Prefab(stream.lastFileID(), node.values()[0], unityFile)
				unityFile.addComponent(comp)
				
		spawnedTransform = dict()
		
		#spawn all the transforms and align
		for transform in unityFile.componentsByTypeName( 'Transform' ):
			mayanode = pm.createNode( 'transform', name=transform.gameObject().name() )
			spawnedTransform[transform.fileID()] = mayanode
			
			mayanode.translate.set( transform.localPosition() )
			mayanode.rotate.set( transform.localRotation() )
			mayanode.scale.set( transform.localScale() )
			mayanode.setParent( sceneRoot, relative=True )
		
		#reparent transforms
		for transform in unityFile.componentsByTypeName( 'Transform' ):
			parentFileID = transform.parentTransformFileId()
			if parentFileID > 0 :
				parentMayanode = spawnedTransform[parentFileID]
				mayanode = spawnedTransform[transform.fileID()]
				mayanode.setParent(parentMayanode, relative=True)
			
			
		#spawn all the boxcolliders
		for boxcollider in unityFile.componentsByTypeName( 'BoxCollider' ):
			go = boxcollider.gameObject()
			if go.tagString() == 'foreground':
				tr = go.transform()
				mayaTransform = spawnedTransform[tr.fileID()]
				w,h,d = boxcollider.size()
				mayanode = pm.polyCube(name = go.name() + '_collider', w=w,h=h,d=d)[0]
				mayanode.setParent( mayaTransform, relative=True )
				
		#spawn all the boxcolliders
		for spherecollider in unityFile.componentsByTypeName( 'SphereCollider' ):
			go = spherecollider.gameObject()
			if go.tagString() == 'foreground':
				tr = go.transform()
				mayaTransform = spawnedTransform[tr.fileID()]
				mayanode = pm.polySphere(name = go.name() + '_collider', r=0.5)[0]
				mayanode.setParent( mayaTransform, relative=True )
			
		#spawn prefabs
		for prefab in unityFile.componentsByTypeName( 'Prefab' ):
			if prefab.isPrefabParent() == 0:
				guid = prefab.parentPrefabGuid()
				filePath = metaGuids[guid]
				SceneImporter().spawn(filePath, sceneRoot, metaGuids)