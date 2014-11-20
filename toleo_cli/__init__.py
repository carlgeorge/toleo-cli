import click
import pathlib
import prettytable
import toleo
import xdg.BaseDirectory
import yaml


class SoftwareTable(prettytable.PrettyTable):
    def add_software_row(self, pkg, src):
        if src.version > pkg.version:
            status = 'UPDATE'
        else:
            status = 'OK'
        self.add_row([pkg.name, src.name,
                      pkg.version, src.version,
                      status])


def read_config(collection='default'):
    xdg_config_home = pathlib.Path(xdg.BaseDirectory.xdg_config_home)
    config_dir = xdg_config_home / 'toleo'
    config_file = (config_dir / collection).with_suffix('.yaml')
    if config_file.is_file():
        with config_file.open() as f:
            return yaml.load(f)
    else:
        raise FileNotFoundError('cannot read {}'.format(config_file))


@click.command()
@click.option('--collection', '-c', default='default')
def cli(collection):
    ''' Entry point for application. '''
    table = SoftwareTable(['NAME', 'PROJECT', 'REPO', 'SOURCE', 'STATUS'])

    print(table)
