import click
import json, requests
from controllers import switch
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
	switch.switchs(config)

@cli.command()
def flow():
	switch.sw_infor(config)
