from db import Db

class Config:

	ip = ''
	port = 0
	name = ''
	dbDados = ''

	def __init__(self):
		self.dbDados = Db()
		lista = self.dbDados.getConfig()
		self.ip = lista[0][0]
		self.port = lista[0][1]
		self.name = lista[0][2]

	def setConfig(self, ip, port, name):
		self.dbDados.setConfig(ip, port, name)
		print 'New Conf: ' + ip + ':' + port + ' ' + name

	def toString(self):
		return 'http://%s:%d -- name: %s' % (self.ip, self.port, self.name)



