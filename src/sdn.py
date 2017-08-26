import click
import json, requests
from controllers import devices
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
def deny():
	devices.deny(config)