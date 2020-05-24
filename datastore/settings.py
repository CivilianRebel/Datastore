import os
from os.path import exists, join
import json

defaults = {'base_dir': 'datastore',
            'data_dir': 'data'}
defaults['storage_path'] = join(defaults['base_dir'], defaults['data_dir'])


class Settings:

    def __init__(self, config_file='config.json', **kwargs):
        self.config_file = config_file
        if exists(self.config_file):
            self.load()
        else:
            self.load(default=True)

    def load(self, default=False):
        if default:
            for k, v in defaults.items():
                self.__setattr__(k, v)
            with open(self.config_file, 'w') as f:
                json.dump(defaults, f)
            return

        with open(self.config_file, 'r') as f:
            data = json.load(f)
            for k, v in data.items():
                self.__setattr__(k, v)
        return
