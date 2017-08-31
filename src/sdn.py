#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner
# V = 1.0

import click
import json, requests
from controllers import devices
from controllers import accessLists
from models.config import Config

config = Config()

### --------------------------------------
@click.group()
def cli():
	""" Aplicação para gerenciamento de controladoras SDN, com interface em linha de comando 
	
	\b
	V 0.1 - 2017 
	Autor: Fagner Jefferson 
	Organização: IFPB
	"""
	pass
	
### --------------------------------------
@cli.command()
@click.argument('ip', nargs=1, metavar='<ip_controlador>')
@click.argument('port', nargs=1, metavar='<porta>')
@click.argument('name', nargs=1, metavar='<nome>')
def conf(ip, port, name):
	"""CONFIGURAÇÃO INICIAL!

	\b
	Grava em um banco de dados
	o IP a PORTA usados no controlador para envio das 
	requisições na rest api do controlador.
	"""
	config.setConfig(ip, port, name)


### --------------------------------------
@cli.command()
def show_conf():
	"""Exibe as configurações atuais.
	"""
	click.echo( config.toString() )

### --------------------------------------
@cli.command()
def switchs():
	"""LISTA DE SWITCHS

	\b
	Mostra o json com a 
	lista dos switchs conectados 
	ao controlador.
	"""
	devices.switchs(config)

### --------------------------------------
@cli.command()
def flow():
	"""LISTA DE FLUXOS

	\b
	Mostra o json com a 
	lista fluxos OpenFlow instalados no controlador
	"""
	devices.sw_infor(config)

### --------------------------------------
@cli.command()
def device():
	"""Lista de dispositivos

	\b
	Mostra o json com a 
	lista dos dispositivos agregado
	na topologia da rede
	"""
	devices.devices(config)

### --------------------------------------
@cli.command()
@click.option('--deny', '-d', nargs=2, type=click.Tuple([unicode, unicode, ]), default=(None, None),
	help='Nega Conexao')
@click.option('--allow', '-a', nargs=2, type=click.Tuple([unicode, unicode, ]), default=(None, None),
	help='Permite Conexao')
@click.option('--prot', '-p', type=click.Choice(['tcp', 'udp', 'icmp']),
	help='Protocolo')
@click.option('--port_number', '-n', default=0, 
	help='Porta usada pelo protocolo, OBS: Nao e obrigatorio, e nao e usado com ICMP')
@click.option('--list', '-l', is_flag=True, 
	help='Lista regras de ACL instaladas')
def acl(list, prot, deny, allow, port_number):
	"""CONTROLE DE ACL

	\b
	(Access Control List) 
	Gerenciamento de de listas de controle de aceso 
	"""
	if list:
		accessLists.lista(config)
	else:	
		accessLists.aclAction(prot, deny, allow, port_number, config)



