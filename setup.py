import setuptools
import sys


if not sys.version_info >= (3, 4):
    sys.exit('requires Python 3.4 or newer')


setuptools.setup(
    name='toleo-cli',
    version='0.0.1',
    description='CLI interface to toleo library.',
    author='Carl George',
    author_email='carl@cgtx.us',
    url='https://github.com/cgtx/toleo-cli',
    packages=['toleo_cli'],
    install_requires=['toleo', 'click', 'prettytable', 'pyxdg'],
    entry_points={'console_scripts': ['toleo=toleo_cli:cli']},
    classifiers=[ 'Programming Language :: Python :: 3.4' ]
)
