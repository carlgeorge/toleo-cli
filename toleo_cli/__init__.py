import click
import toleo
import prettytable


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
# @click.option('--upstream-only', '-u', 'action', flag_value='upstream')
# @click.option('--repo-only', '-r', 'action', flag_value='repo')
# @click.option('--verbose', '-v', count=True)
# @click.option('--collection', '-c', default='default')
# @click.option('--path-override', envvar='TOLEO_CONFIG_HOME')
# @click.option('--limit', '-l')
def cli():
    ''' Entry point for application. '''
    table = SoftwareTable(['PACKAGE', 'PROJECT', 'AUR', 'UPSTREAM', 'STATUS'])

    for name in ['click', 'docker-py', 'pluginbase']:
        aur = toleo.AurPackage('python2-' + name.rstrip('-py'), upstream=name)
        pypi = toleo.PypiSoftware(name)
        table.add_software_row(aur, pypi)

    table.add_software_row(toleo.AurPackage('supernova'),
                           toleo.PypiSoftware('supernova'))

    mint_x_icons_pkg = toleo.AurPackage('mint-x-icons')
    mint_x_icons_src = toleo.GenericSoftware('mint-x-icons',
        url='http://packages.linuxmint.com/pool/main/m/mint-x-icons/')
    table.add_software_row(mint_x_icons_pkg, mint_x_icons_src)

    mint_x_theme_pkg = toleo.AurPackage('mint-x-theme', upstream='mint-themes')
    mint_x_theme_src = toleo.GenericSoftware('mint-themes',
        url='http://packages.linuxmint.com/pool/main/m/mint-themes/')
    table.add_software_row(mint_x_theme_pkg, mint_x_theme_src)

    autokey_data_xdg_pkg = toleo.AurPackage('autokey-data-xdg', upstream='autokey')
    autokey_data_xdg_src = toleo.GenericSoftware('autokey',
        url='https://code.google.com/p/autokey/downloads/list')
    table.add_software_row(autokey_data_xdg_pkg, autokey_data_xdg_src)

    print(table)
