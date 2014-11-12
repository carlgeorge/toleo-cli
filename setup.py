import setuptools

setuptools.setup(
    name = 'toleo-cli',
    version = '0.0.1',
    description = 'CLI interface to toleo library.',
    author = 'Carl George',
    author_email = 'carl@cgtx.us',
    url = 'https://github.com/cgtx/toleo-cli',
    packages = ['toleo_cli'],
    install_requires = ['toleo', 'click', 'prettytable'],
    entry_points = {'console_scripts': ['toleo = toleo_cli:cli']}
)
