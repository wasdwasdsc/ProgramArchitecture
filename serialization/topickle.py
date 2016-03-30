from pickle import dump, load


def read(filename):
    """
    read from pickle file
    :param filename: file name
    :return: deserialized object
    """
    with open(filename, 'rb') as f:
        data = load(f)
        return data


def write(filename, data):
    """
    write into pickle file
    :param filename: file name
    :param data: object to serialize
    :return: nothing
    """
    with open(filename, 'wb') as f:
        dump(data, filename)