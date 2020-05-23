import os
from os.path import join, exists

from datastore.key import Key


def key_file(k_o):
    return join(k_o.data_path, f'{k_o.name}.json')


class FileUtils:

    def __init__(self, key_obj):
        pass

