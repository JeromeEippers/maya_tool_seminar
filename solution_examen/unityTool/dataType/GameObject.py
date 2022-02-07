from Component import Component

class GameObject(Component):
	
	def __init__(self, fileId, data, file):
		super(GameObject, self).__init__(fileId, data, file, 'GameObject')
		
		
	def name(self):
		return self._data['m_Name']
		
		
	def transform(self):
		for transform in self._file.componentsByTypeName( 'Transform' ):
			if transform.gameObjectFileID() == self.fileID():
				return transform
				
	def tagString(self):
		return self._data['m_TagString']