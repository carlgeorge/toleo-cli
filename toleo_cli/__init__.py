import click
from .config import read_config
from .multi import handle
from .table import create_table


@click.command()
@click.option('--collection', '-c', default='default')
def cli(collection):
    ''' Entry point for application. '''
    config = read_config()
    results = handle(config)
    table = create_table(results)
    print(table)
