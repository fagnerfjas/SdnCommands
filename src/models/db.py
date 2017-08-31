#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner
# V = 1.0

import sqlite3
import os.path


'''
	Classe de gerenciamento de banco de dados
'''
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

	'''
		Faz a conexão com o banco de dados SqLite, 
		Cria o arquivo caso ele não exista
	'''
	def conect(self):
		self.conexao = sqlite3.connect(self.pathDb + 'sdnDatabase.db')
		return self.conexao.cursor()

	'''
		Disconecta do banco de dados
	'''
	def disconect(self):
		self.conexao.close()

	'''
		Salva os dados da query inseridas na conexão 
		e disconecta do banco de dados
	'''
	def salveDisconect(self):
		self.conexao.commit()
		self.conexao.close()	

	
	'''
		Cria o diretório indicado na variável <pathDb>,
		Caso não tenha permissão o diretório deverá ser criado pelo usuário
	'''
	def criaDiretorio(self):
		if not os.path.isdir(self.pathDb):
			os.mkdir(self.pathDb)
	
	'''
		Retorna a configuração atual do sistema
	'''
	def getConfig(self):
		data = self.conect()
		dados = data.execute('''select * from config''').fetchall()
		self.disconect()
		return dados


	'''
		Seta as configuração do controlador
	'''
	def setConfig(self, ip, port, name):
		data = self.conect()
		data.execute('UPDATE config set ip="{new_ip}", port={new_port}, name="{new_name}"'.format(new_ip=ip, new_port=port, new_name=name))
		self.salveDisconect()