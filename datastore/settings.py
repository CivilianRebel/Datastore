import os
from os.path import exists, join
import json

defaults = {'base_dir': 'datastore',
            'data_dir': 'data',
            'storage_path': None}


class Settings:

    def __init__(self, config_file='config.json', **kwargs):
        self.config_file = config_file
        self.options = {}
        if exists(self.config_file):
            self.load()
        else:
            self.load(default=True)

        for k, v in kwargs.items():
            if k in self.options.keys():
                self.options[k] = v

        self.save()

    def save(self):
        self.options['storage_path'] = join(self.base_dir, self.data_dir)
        with open(self.config_file, 'w') as f:
            json.dump(self.options, f)

    def _load(self, d):
        for k, v in d.items():
            self.options[k] = v

    def load(self, default=False):
        if default:
            self._load(defaults)
            self.save()
            return

        with open(self.config_file, 'r') as f:
            data = json.load(f)
            self._load(data)
        return

    def __getattr__(self, item):
        self.load()
        return self.options[item]
