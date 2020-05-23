import os
from os.path import join, exists
import glob
from datastore.value import Value
from datastore.key import Key


class FileHelper:

    def __init__(self, base, *args, **kwargs):
        """
        TODO: Docstring
        :param base:
        :type base:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """
        self.base = base
        self.done_init = False
        self.full_path = None
        self.data_folder_name = kwargs.get('data_folder_name', 'data')
        self.initialize(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        """
        TODO: Docstring
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """
        if not exists(self.base):
            self.create_structure('all')
        else:
            if not exists(self.data_path):
                self.create_structure('data')

    def create_structure(self, *args):
        """
        TODO: Docstring
        :param args:
        :type args:
        """
        if 'all' in args:
            os.mkdir(self.base)
            os.mkdir(self.data_path)
        elif 'data' in args:
            os.mkdir(self.data_path)

    def set_key(self, k, v):
        """
        TODO: Docstring
        :param k:
        :type k:
        :param v:
        :type v:
        """
        k_file = Key(k, data_path=self.data_path)
        value = Value(k_file, v)
        value.update()

    def get_key(self, k):
        """
        TODO: Docstring
        :param k:
        :type k:
        :return:
        :rtype:
        """
        k_file = Key(k, data_path=self.data_path)
        v = Value(key=k_file)
        return getattr(v, k)

    @property
    def data_path(self):
        """
        TODO: Docstring
        :return:
        :rtype:
        """
        return join(self.base, self.data_folder_name)

    @property
    def path(self):
        """
        TODO: Docstring
        :return:
        :rtype:
        """
        return self.data_path

    @property
    def glob_all(self):
        """
        TODO: Docstring
        :return:
        :rtype:
        """
        return glob.glob(join(self.data_path, '*.json'))


if __name__ == '__main__':
    b = FileHelper(base='testingloc')
    b.set_key('testing', {'test': False})
    print(b.get_key('testing'))
