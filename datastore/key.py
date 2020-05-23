from os.path import exists as file_exists, isfile, join


class Key:

    def __init__(self, name, data_path=''):
        self.data_path = data_path
        self.name = name

    @property
    def key_file(self):
        return join(self.data_path, f'{self.name}.json')

    @property
    def exists(self):
        if file_exists(self.key_file):
            with open(self.key_file, 'r') as f:
                if len(f.read()) > 0:
                    return True
                else:
                    return False
        else:
            return False
