import click
import multiprocessing
import prettytable
import toleo
from .config import read_config


class SoftwareTable(prettytable.PrettyTable):
    def add_software_row(self, pkg, src):
        if src.version > pkg.version:
            status = 'UPDATE'
        else:
            status = 'OK'
        self.add_row([pkg.name, src.name,
                      pkg.version, src.version,
                      status])


def worker(item):
    name, data = item
    src = data.get('src')
    pkg = data.get('pkg')

    src_name = src.pop('name', name)
    src_type = src.pop('type', 'generic')
    if src_type == 'generic':
        software = toleo.GenericSoftware(src_name, **src)
    elif src_type == 'pypi':
        software = toleo.PypiSoftware(src_name, **src)
    elif src_type == 'github':
        software = toleo.GithubSoftware(src_name, **src)
    elif src_type == 'bitbucket':
        software = toleo.BitbucketSoftware(src_name, **src)

    pkg_name = pkg.pop('name', name)
    pkg_type = pkg.pop('type')
    if pkg_type == 'aur':
        package = toleo.AurPackage(pkg_name, **pkg)

    return (software, package)


@click.command()
@click.option('--collection', '-c', default='default')
def cli(collection):
    ''' Entry point for application. '''

    config = read_config()

    pool = multiprocessing.Pool()
    results = pool.map(worker, config.items())
    pool.close()
    pool.join()

    table = SoftwareTable(['PACKAGE', 'PROJECT', 'REPO', 'SOURCE', 'STATUS'])
    for result in results:
        software, package = result
        table.add_software_row(package, software)

    print(table)
