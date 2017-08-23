import click
import json, requests

@click.group()
def cli():
	click.echo('funcionei')

@cli.command()
@click.argument('ip', nargs=2)
@click.option('-n', '--name', type=(unicode))
def conf(ip, name):
	click.echo(name)

@cli.command()
def hosts():
	response = requests.get("http://192.168.15.9:8080/wm/core/controller/switches/json")
	click.echo(response.content)
