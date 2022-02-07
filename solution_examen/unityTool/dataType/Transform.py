from Component import Component
import pymel.core as pm
import pymel.util as ut

class Transform(Component):
	
	def __init__(self, fileId, data, file):
		super(Transform, self).__init__(fileId, data, file, 'Transform')
	
	def parentTransformFileId(self):
		return self._data['m_Father']['fileID']
		
	def parentTransform(self):
		return self._file.componentByFileID( self.parentTransformFileId() )
		
		
	def localPosition(self):
		x = float( self._data['m_LocalPosition']['x'] )
		y = float( self._data['m_LocalPosition']['y'] )
		z = float( self._data['m_LocalPosition']['z'] )
		return [x,y,z]
	
	def localScale(self):
		x = float( self._data['m_LocalScale']['x'] )
		y = float( self._data['m_LocalScale']['y'] )
		z = float( self._data['m_LocalScale']['z'] )
		return [x,y,z]
	
	def localRotation(self):
		x = float( self._data['m_LocalRotation']['x'] )
		y = float( self._data['m_LocalRotation']['y'] )
		z = float( self._data['m_LocalRotation']['z'] )
		w = float( self._data['m_LocalRotation']['w'] )
		quat = pm.datatypes.Quaternion( [x,y,z,w] )
		euler = quat.asEulerRotation()
		degree = ut.degrees( euler )
		return degree
		
