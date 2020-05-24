from datastore.storage_util import Storage
from datastore.settings import Settings


class DiskStore:

    def __init__(self):
        """
        Handles higher level reading and writing (key, value) pairs to files on disk
        :type loc: str
        :param loc: base folder to store data, if does not exist it will be created
        """
        self.__dict__['storage_helper'] = Storage(Settings())

    def __setattr__(self, key, value):
        """
        Writes key, value pair to file
        uses format: datastore_instance.{key}
        for example:
            data.entry1 = 'data1'
            same as
            data['entry1'] = 'data1'
        :param key: Name of key in pair
        :type key: any
        :param value: Value to be written to corresponding key
        :type value: any
        :return: none
        :rtype: None
        """
        self.storage_helper.set_key(key, value)


    def __getattr__(self, item):
        """
        Gets the json dict for the specified key
        Uses attribute format for example
            print(data.entry1)
            would output same as
            print(data['entry1'])
        :param item: Key to grab from disk
        :type item: str
        :return: value contained in key file
        :rtype: any
        """
        return self.storage_helper.get_key(item)

    def __getitem__(self, item):
        """
        Same as __getattr__ except with dictionary style
        :param item: Key to grab value from
        :type item: str
        :return: value in key file
        :rtype: any
        """
        return self.storage_helper.get_key(item)

    def __setitem__(self, key, value):
        """
        Same as __setattr__ except with dictionary style
        :param key: Key name to write to disk
        :type key: str
        :param value: data to assign to key file
        :type value: any
        :return: None
        :rtype: None
        """
        self.storage_helper.set_key(key, value)


if __name__ == '__main__':
    ds = DiskStore()
    ds.yo = 'test'
    print(ds.yo)
