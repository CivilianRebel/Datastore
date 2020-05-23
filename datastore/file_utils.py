import glob
import os
from os.path import join, exists

from datastore.key import Key
from datastore.value import Value


class FileHelper:

    def __init__(self, base, *args, data_folder_name='data', **kwargs):
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
        self.base = base
        self.done_init = False
        self.full_path = None
        self.data_folder_name = data_folder_name
        self.initialize(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        """
        Create data and base folders if they do not exist
        :param args: Not handled
        :type args: list
        :param kwargs: Not handled
        :type kwargs: dict
        """
        if not exists(self.base):
            self.create_structure('all')
        else:
            if not exists(self.data_path):
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
            os.mkdir(self.base)
            os.mkdir(self.data_path)
        elif 'data' in args:
            os.mkdir(self.data_path)

    def set_key(self, k, v):
        """
        Set key(k) to value(v)
        :param k: Name of key
        :type k: str
        :param v: Value to write to key
        :type v: any
        """
        k_file = Key(k, data_path=self.data_path)
        value = Value(k_file, v)
        value.update()

    def get_key(self, k):
        """
        Returns the value of the requested key(k)
        :param k: Key to read from disk
        :type k: str
        :return: Value stored, throws KeyError if none exist
        :rtype: any
        """
        k_file = Key(k, data_path=self.data_path)
        v = Value(key=k_file)
        return v.json[k]

    @property
    def data_path(self):
        """
        Returns string for the path to store json files in
        :return:
        :rtype:
        """
        return join(self.base, self.data_folder_name)

    @property
    def glob_all(self):
        """
        Grabs list of all json files in data path
        :return: List of json file paths for all key entries stored on disk
        :rtype: list
        """
        return glob.glob(join(self.data_path, '*.json'))


if __name__ == '__main__':
    b = FileHelper(base='testingloc')
    b.set_key('testing', {'test': False})
    print(b.get_key('testing'))
