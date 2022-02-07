class Component( object ):
	
	def __init__(self, fileId, data, file, typeName):
		self._fileId = fileId
		self._data = data
		self._file = file
		self._typeName = typeName
		
	def fileID(self):
		return self._fileId
		
	def typeName(self):
		return self._typeName
		
	def gameObjectFileID(self):
		if 'm_GameObject' in self._data:
			return self._data['m_GameObject']['fileID']
		return 0
		
	def gameObject(self):
		return self._file.componentByFileID( self.gameObjectFileID() )