import click
import pathlib
import prettytable
import toleo
import xdg.BaseDirectory
import yaml


class ToleoConfig():
    def __init__(self, config_file):
        self.config_file = config_file
        self.load()

    def load(self):
        if self.config_file.is_file():
            with self.config_file.open() as f:
                self.data = yaml.load(f)
        else:
            raise FileNotFoundError('cannot read {}'.format(config_file))


class ToleoItem():
    def __init__(self, data):
        pass

    def simple_src_load(self):
        pass

    def complex_src_load(self):
        pass


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


def software_parse(item):
    name, data = item
    software_type, kwargs = list(data.items())[0]
    if 'name' in kwargs:
        name = kwargs.pop('name')
    if software_type.lower() == 'generic':
        return toleo.GenericSoftware(name, **kwargs)
    elif software_type.lower() == 'pypi':
        return toleo.PypiSoftware(name, **kwargs)
    elif software_type.lower() == 'github':
        return toleo.GithubSoftware(name, **kwargs)
    elif software_type.lower() == 'bitbucket':
        return toleo.BitbucketSoftware(name, **kwargs)


def parse(item):
    name, data = item
    upstream = data.get('upstream')
    downstream = data.get('downstream')
    if isinstance(upstream, str):
        software_type = 'generic'
    elif isinstance(upstream, dict):
        







@click.command()
@click.option('--collection', '-c', default='default')
def cli(collection):
    ''' Entry point for application. '''
    config = read_config()
    for item in config.items():
        upstream, downstream = parse(item)
        print(upstream.name)
        print(upstream.version)

    # for item in config:
        # src_data = config.get(item).get('src')
        # if isinstance(src_data, str):
        #     src_type = simple_src_parse(src_data)
        # if isinstance(src_data, dict):
        #     src_type = complex_src_parse(src_data)

        # software = src_info.get('software') or 'generic'
        # src_name = src_info.get('name') or item

        # if software == 'generic':
        #     src = GenericSoftware(
        #         src_name,
        #         url=src_info.get('url'),
        #         pattern=src_info.get('pattern'),
        #         use_headers=src_info.get('use_headers'))
        # elif software == 'pypi':
        #     src = PypiSoftware(src_name)
        # elif software == 'github':
        #     src = GithubSoftware(
        #         src_name,
        #         owner=)
        # elif software == 'bitbucket':
        #     src = BitbucketSoftware(src_name)

        # owner = src_info.get('owner')
        # tag_trims = src_info.get('tag_trims')

        # pkg = config.get(item).get('pkg')
        # pkgname = pkg.get('name') or item

        # table.add_software_row(src, pkg)

    # print(config)

    # table = SoftwareTable(['PACKAGE', 'PROJECT', 'AUR', 'UPSTREAM', 'STATUS'])

    # for name in ['click', 'docker-py', 'pluginbase']:
    #     aur = toleo.AurPackage('python2-' + name.rstrip('-py'), upstream=name)
    #     pypi = toleo.PypiSoftware(name)
    #     table.add_software_row(aur, pypi)

    # table.add_software_row(toleo.AurPackage('supernova'),
    #                        toleo.PypiSoftware('supernova'))

    # mint_x_icons_pkg = toleo.AurPackage('mint-x-icons')
    # mint_x_icons_src = toleo.GenericSoftware('mint-x-icons',
    #     url='http://packages.linuxmint.com/pool/main/m/mint-x-icons/')
    # table.add_software_row(mint_x_icons_pkg, mint_x_icons_src)

    # mint_x_theme_pkg = toleo.AurPackage('mint-x-theme', upstream='mint-themes')
    # mint_x_theme_src = toleo.GenericSoftware('mint-themes',
    #     url='http://packages.linuxmint.com/pool/main/m/mint-themes/')
    # table.add_software_row(mint_x_theme_pkg, mint_x_theme_src)

    # autokey_data_xdg_pkg = toleo.AurPackage('autokey-data-xdg',
    #                                         upstream='autokey')
    # autokey_data_xdg_src = toleo.GenericSoftware('autokey',
    #     url='https://code.google.com/p/autokey/downloads/list')
    # table.add_software_row(autokey_data_xdg_pkg, autokey_data_xdg_src)

    # print(table)
