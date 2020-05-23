import json as j


class Value:

    def __init__(self, key, data=None):
        """
        Value class handles the writing and reading of the
        json files at {self.name}.json
        :param key: Key object with name for the data requested
        :type key: Key
        :param data: Value to enter into key file
        :type data: any
        """
        self.key = key
        self.data = data
        self.name = self.key.name
        self.file_path = self.key.key_file

    def update(self):
        """
        Write self.data to the key file in json format
        :return: None
        :rtype: None
        """
        with open(self.file_path, 'w') as f:
            j.dump({'data': self.data}, f)

    @property
    def load(self):
        """
        Get the json object for the self.key file
        :return: json dict for key file
        :rtype: dict
        """
        if not self.key.exists:
            raise NotImplementedError
        val = None
        with open(self.file_path, 'r') as f:
            val = j.load(f)
        return val['data']
