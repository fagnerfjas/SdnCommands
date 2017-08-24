from db import Db


class Config:

	ip = ''
	port = 0
	name = ''

	def __init__(self):
		dbDados = Db()
		lista = dbDados.getConfig()
		self.ip = dados[0][0]
		self.port = dados[0][1]
		self.name = dados[0][2]



