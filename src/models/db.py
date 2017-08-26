import sqlite3
import os.path

class Db:
	
	conexao = ''
	pathDb = '/etc/sdnApp/'

	def __init__(self):
		self.criaDiretorio()
			
		data = self.conect()
		data.execute('''CREATE TABLE IF NOT EXISTS config(ip text, port int, name text)''')

		if len(data.execute('''select * from config''').fetchall()) < 1:
			data.execute("INSERT INTO config VALUES ('192.168.1.1', 6653, 'floodlight')")

		self.salveDisconect()


	def conect(self):
		self.conexao = sqlite3.connect(self.pathDb + 'sdnDatabase.db')
		return self.conexao.cursor()

	def disconect(self):
		self.conexao.close()

	def salveDisconect(self):
		self.conexao.commit()
		self.conexao.close()	

	def criaDiretorio(self):
		if not os.path.isdir(self.pathDb):
			os.mkdir(self.pathDb)
	
	def getConfig(self):
		data = self.conect()
		dados = data.execute('''select * from config''').fetchall()
		self.disconect()
		return dados

	def setConfig(self, ip, port, name):
		data = self.conect()
		data.execute('UPDATE config set ip="{new_ip}", port={new_port}, name="{new_name}"'.format(new_ip=ip, new_port=port, new_name=name))
		self.salveDisconect()