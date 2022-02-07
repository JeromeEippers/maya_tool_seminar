from Component import Component

class BoxCollider(Component):
	
	def __init__(self, fileId, data, file):
		super(BoxCollider, self).__init__(fileId, data, file, 'BoxCollider')
	
	def size(self):
		x = float( self._data['m_Size']['x'])
		y = float( self._data['m_Size']['y'])
		z = float( self._data['m_Size']['z'])
		return [x,y,z]

	def center(self):
		x = float( self._data['m_Center']['x'])
		y = float( self._data['m_Center']['y'])
		z = float( self._data['m_Center']['z'])
		return [-x,y,z]