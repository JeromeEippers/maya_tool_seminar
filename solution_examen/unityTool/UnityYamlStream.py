class UnityYamlStream( object ):
	
	def __init__(self, path ):
		self.__file = open(path)
		self.__fileIds = list()
		
	def read(self, param):
		line = self.__file.readline()
		
		if line == None or line == '':
			self.__file.close()
			self.__fileIds.append( 0 )
			return ''
			
		if line.startswith('---'):
			tag = line.split(' ')[2]
			self.__fileIds.append( int(tag.replace('&','')) )
			line = '--- ' + tag + '\n'
			
		return line
		
	def lastFileID(self):
		return self.__fileIds[-2]