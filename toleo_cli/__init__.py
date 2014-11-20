import click
import prettytable
from .config import read_config
from .multi import handle


class SoftwareTable(prettytable.PrettyTable):
    def add_software_row(self, pkg, src):
        if src.version > pkg.version:
            status = 'UPDATE'
        else:
            status = 'OK'
        self.add_row([pkg.name, src.name,
                      pkg.version, src.version,
                      status])


@click.command()
@click.option('--collection', '-c', default='default')
def cli(collection):
    ''' Entry point for application. '''

    config = read_config()
    results = handle(config)

    table = SoftwareTable(['PACKAGE', 'PROJECT', 'REPO', 'SOURCE', 'STATUS'])
    for result in results:
        software, package = result
        table.add_software_row(package, software)

    print(table)
