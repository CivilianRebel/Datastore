import json as j


class Value:

    def __init__(self, key, data=''):
        self.key = key
        self.data = data
        self.name = self.key.name
        self.file_path = self.key.key_file


    def __getattr__(self, item):
        return self.json[item]

    def update(self):
        with open(self.file_path, 'w') as f:
            j.dump({self.name: self.data}, f)

    @property
    def json(self):
        if not self.key.exists:
            raise NotImplementedError
        val = None
        with open(self.file_path, 'r') as f:
            val = j.load(f)
        return val
