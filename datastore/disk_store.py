from datastore.file_utils import FileHelper


class DiskStore:

    def __init__(self, loc):
        """
        DiskStore can be accessed like a dictionary and stores information on disk
        'loc/[prefix: optional]/{key}.json
        :type loc: str
        :param loc: base folder to store data, if does not exist it will be created
        """
        self.file_helper = FileHelper(loc)

    def __setattr__(self, key, value):
        """

        :param key:
        :type key:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        if key != 'file_helper':
            self.file_helper.set_key(key, value)
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        """

        :param item:
        :type item:
        :return:
        :rtype:
        """
        return self.file_helper.get_key(item)

    def __getitem__(self, item):
        """
        TODO: Docstring
        :param item:
        :type item:
        :return:
        :rtype:
        """
        return self.file_helper.get_key(item)

    def __setitem__(self, key, value):
        """

        :param key:
        :type key:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.file_helper.set_key(key, value)


if __name__ == '__main__':
    ds = DiskStore('wrap')
    print(ds.yo)