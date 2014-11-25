import click
import toleo
from .config import read_config
from .table import create_table


@click.command()
@click.option('--collection', '-c', default='default')
def cli(collection):
    ''' Entry point for application. '''
    config = read_config(collection)
    results = toleo.process(config)
    table = create_table(results)
    print(table)
