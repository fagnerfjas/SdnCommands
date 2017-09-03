#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner
# V = 1.0

import click
import json, requests
from controllers import devices
from controllers import accessLists
from controllers import flows
from models.config import Config

config = Config()

'''COLORAÇÃO DA RESPOSTA'''
def printColor(value, color):
	click.echo(click.style(value, fg=color))

### --------------------------------------
@click.group()
@click.option('--clear', is_flag=True, default=False, help='Usado juntamente com um subcomando')
def cli(clear):
	""" Aplicação para gerenciamento de controladoras SDN, com interface em linha de comando 
	
	\b
	V 0.1 - 2017 
	Autor: Fagner Jefferson 
	Organização: IFPB
	"""
	if clear:
		click.clear()	
	
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
	printColor( config.setConfig(ip, port, name), 'green' )


### --------------------------------------
@cli.command()
def show_conf():
	"""Exibe as configurações atuais.
	"""
	printColor( config.toString(), 'green' )

### --------------------------------------
@cli.command()
def switchs():
	"""LISTA DE SWITCHS

	\b
	Mostra o json com a 
	lista dos switchs conectados 
	ao controlador.
	"""
	printColor( devices.switchs(config), 'green')



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



@cli.command()
@click.option('--list', '-l', is_flag=True, help='Lista os fluxos instalados')
@click.option('--file', '-f', type=click.File('rb'), help='Adiciona conteúdo de um arquivo json como fluxo')
def flow(list, file):
	if list:
		printColor( flows.sw_infor(config), 'blue' )
	else:
		if file:
			data = file.read(1024)	
			printColor( flows.addflow(data, config), 'cyan' )			

@cli.command()
@click.argument('input', type=click.File('rb'))
def file(input):
	ch = input.read(1024)
	