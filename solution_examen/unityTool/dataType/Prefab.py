from Component import Component

class Prefab(Component):
	
	def __init__(self, fileId, data, file):
		super(Prefab, self).__init__(fileId, data, file, 'Prefab')
	
	def parentPrefabGuid(self):
		return self._data['m_ParentPrefab']['guid']
		
	def isPrefabParent(self):
		return self._data['m_IsPrefabParent']