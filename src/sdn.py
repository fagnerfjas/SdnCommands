# -*- coding: utf-8 -*-

import click
import json, requests
from controllers import devices
from controllers import accessLists
from models.config import Config

config = Config()

@click.group()
def cli():
	pass
	
@cli.command()
@click.argument('ip', nargs=1)
@click.argument('port', nargs=1)
@click.argument('name', nargs=1)
def conf(ip, port, name):
	config.setConfig(ip, port, name)

@cli.command()
def show_conf():
	click.echo( config.toString() )

@cli.command()
def switchs():
	devices.switchs(config)

@cli.command()
def flow():
	devices.sw_infor(config)

@cli.command()
def device():
	devices.devices(config)

@cli.command()
@click.option('--deny', '-d', nargs=2, type=click.Tuple([unicode, unicode, ]), default=(None, None))
@click.option('--allow', '-a', nargs=2, type=click.Tuple([unicode, unicode, ]), default=(None, None))
@click.option('--prot', '-p', type=click.Choice(['tcp', 'udp', 'icmp']))
@click.option('--port_number', '-n', default=0)
def acl(prot, deny, allow, port_number):
	accessLists.aclAction(prot, deny, allow, port_number, config)


@cli.command()
def acllista():
	accessLists.lista(config)

