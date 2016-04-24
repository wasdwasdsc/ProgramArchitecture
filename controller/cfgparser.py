"""config file parser module"""
from serialization.tojson import read as json_read, write as json_write
from serialization.topickle import read as pickle_read, write as pickle_write
from serialization.toyaml import read as yaml_read, write as yaml_write
import configparser


def cfgparse(fname="data/defaults.cfg"):
    """
    parse configure file
    :param fname: configure file name
    :return: functions read/write
    """
    parser = configparser.ConfigParser()
    parser.read(fname)
    type = parser['serialization']['type']
    if type == 'json':
        return json_read, json_write
    elif type == 'pickle':
        return pickle_read, pickle_write
    elif type == 'yaml':
        return yaml_read, yaml_write
    else:
        raise AttributeError('Incorrect serialization type')