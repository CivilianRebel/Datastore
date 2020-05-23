from os.path import exists as file_exists, join
from datastore.io_util import FileUtils, key_file


class Key:

    def __init__(self, name, data_path=''):
        """
        Key class handles basic string and file-based operations
        :param name: Name of the key
        :type name: str
        :param data_path: Path to base_location/data_folder_name
        :type data_path: str
        """
        self.data_path = data_path
        self.name = name
        self.key_file = key_file(self)

    @property
    def exists(self):
        """
        Does the key file exist and is it non-empty
        :return: Exists and non-empty -> True, else -> False
        :rtype: bool
        """
        if file_exists(self.key_file):
            with open(self.key_file, 'r') as f:
                if len(f.read()) > 0:
                    return True
                else:
                    return False
        else:
            return False
