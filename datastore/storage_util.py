import glob
import os
from os.path import join, exists

from datastore.entry import DataEntry
from datastore.settings import Settings


class Storage:

    def __init__(self, config=None):
        """
        Handles most of the file checking and some medium level key, value pair methods
        Ensures base and data_folder_name directories exist
        Some string building for folder/file paths that may be moved later

        :param base: Folder to store data in, note another directory will be created with
                     the name data_folder_name inside of 'base' directory
        :type base: str
        :param args: Extra positional arguments, none are handled as of now
        :type args: list
        :param kwargs: Extra keyword arguments, none are handled as of now
        :type kwargs: dict
        """
        self.config = config
        self.initialize()

    def initialize(self):
        """
        Create data and base folders if they do not exist
        """
        if not exists(self.config.base_dir):
            self.create_structure('all')
        else:
            if not exists(self.config.storage_path):
                self.create_structure('data')

    def create_structure(self, *args):
        """
        Create folder structure according to args strings
        :param args: List of strings specifying which folders to create
                     'all': creates entire folder structure from scratch
                     'data': only creates data_folder_name inside of base dir
        :type args: list
        """
        if 'all' in args:
            os.mkdir(self.config.base_dir)
            os.mkdir(self.config.storage_path)
        elif 'data' in args:
            os.mkdir(self.config.storage_path)

    def set_key(self, k, v):
        """
        Set key(k) to value(v)
        :param k: Name of key
        :type k: str
        :param v: Value to write to key
        :type v: any
        """
        entry = DataEntry(config=self.config, key=k)
        entry.write(v)

    def get_key(self, k):
        """
        Returns the value of the requested key(k)
        :param k: Key to read from disk
        :type k: str
        :return: Value stored, throws KeyError if none exist
        :rtype: any
        """
        entry = DataEntry(self.config, key=k)
        return entry.value


if __name__ == '__main__':
    b = Storage(config=Settings())
    b.set_key('test_set', 'lets see')
    print(b.get_key('test_set'))
