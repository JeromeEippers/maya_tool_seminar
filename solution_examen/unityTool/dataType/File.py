class File(object):
	
	def __init__(self):
		self._components = list()
		
	def addComponent(self, comp):
		self._components.append( comp )
		
	def componentByFileID(self, fileId):
		for comp in self._components:
			if comp.fileID() == fileId:
				return comp
				
	def componentsByTypeName(self, typeName):
		result = list()
		for comp in self._components:
			if comp.typeName() == typeName:
				result.append(comp)
		return result