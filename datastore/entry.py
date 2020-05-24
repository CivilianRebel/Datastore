from os.path import join
import datastore.io_util as io


class DataEntry:

    def __init__(self, config=None, key=None):
        self.config = config
        self.key = key

    @property
    def file_path(self):
        return join(self.config.storage_path, f'{self.key}.json')

    @property
    def value(self):
        return io.read(self.file_path)

    def write(self, v):
        io.write(self.file_path, v)
