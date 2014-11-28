import click
import pathlib
import toleo
import xdg.BaseDirectory
from .table import create_table


@click.command()
@click.option('-c', '--collection', 'collection_name', default='default')
@click.option('-v', '--verbose', count=True)
def cli(collection_name, verbose):
    ''' Entry point for application. '''
    xdg_config_home = pathlib.Path(xdg.BaseDirectory.xdg_config_home)
    config_dir = xdg_config_home / 'toleo'
    config = (config_dir / collection_name).with_suffix('.yaml')
    try:
        collection = toleo.Collection(config)
        results = toleo.process(collection)
    except toleo.ToleoException as e:
        if verbose > 0:
            raise e
        else:
            e.quit()
    table = create_table(results)
    print(table)
