import click
import pathlib
import toleo
import xdg.BaseDirectory
from .table import create_table


@click.command()
@click.option('--collection', '-c', 'collection_name', default='default')
def cli(collection_name):
    ''' Entry point for application. '''
    xdg_config_home = pathlib.Path(xdg.BaseDirectory.xdg_config_home)
    config_dir = xdg_config_home / 'toleo'
    config = (config_dir / collection_name).with_suffix('.yaml')
    collection = toleo.Collection(config)
    results = toleo.process(collection)
    table = create_table(results)
    print(table)
