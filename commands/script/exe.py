import click
import sqlite3


@click.command()
def cli():
    """Example script."""
    click.echo('Hello World! dentro do pacote')
    bd = sqlite3.connect('exemplo.db')
    c = bd.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    bd.commit()
    c.close()
    bd.close()
