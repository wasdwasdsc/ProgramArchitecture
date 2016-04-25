"""module that serialize
user.User in Yaml and deserialize
user.User from file"""

import yaml
from model.Accounting import Accounting


def write(obj, fname='data/info.yaml'):
    """
    serialize user object in Yaml
    :param obj: class User to serialize
    :param fname: file name
    :return: nothing
    """
    if not isinstance(obj, Accounting):
        # obj is not User
        raise ValueError('Incorrect type of variable obj')
    with open(fname, 'wt') as file:
        yaml.dump(obj, file)


def read(fname='data/info.yaml'):
    """
    read from Yaml file object
    :param fname: file name
    :return: new User object or None
    """
    try:
        with open(fname, 'rt') as file:
            # try load
            # and return user
            return yaml.load(file)
    except (OSError, ValueError):
        # file not found or incorrect value,
        # return None
        return None
