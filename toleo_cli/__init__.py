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
    try:
        collection = toleo.Collection(config)
    except OSError as err:
        msg = 'no config for collection "{}" ({})'
        raise click.ClickException(msg.format(config.stem, err.filename))
    except AttributeError as err:
        raise click.ClickException(err)
    else:
        results = toleo.process(collection)
        table = create_table(results)
        print(table)
