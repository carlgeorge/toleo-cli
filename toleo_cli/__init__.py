import click
import pathlib
import toleo
import xdg.BaseDirectory
from .table import create_table


@click.command()
@click.option('--collection', '-c', default='default')
def cli(collection):
    ''' Entry point for application. '''
    xdg_config_home = pathlib.Path(xdg.BaseDirectory.xdg_config_home)
    config_dir = xdg_config_home / 'toleo'
    collection_config = (config_dir / collection).with_suffix('.yaml')
    collection_data = toleo.load_collection(collection_config)
    results = toleo.process(collection_data)
    table = create_table(results)
    print(table)
