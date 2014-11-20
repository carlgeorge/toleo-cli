import pathlib
import xdg.BaseDirectory
import yaml


def read_config(collection='default'):
    xdg_config_home = pathlib.Path(xdg.BaseDirectory.xdg_config_home)
    config_dir = xdg_config_home / 'toleo'
    config_file = (config_dir / collection).with_suffix('.yaml')
    if config_file.is_file():
        with config_file.open() as f:
            return yaml.load(f)
    else:
        raise FileNotFoundError('cannot read {}'.format(config_file))
