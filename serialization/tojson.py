"""module that serialize
user.User in JSON and deserialize
user.User from file"""

import json
from model.Accounting import Accounting
from model.charge import Charge
from model.petrol import Petrol


class AccountingEncoder(json.JSONEncoder):
    """
    Serializer user.User in JSON
    """
    def default(self, o):
        """
        overriding method
        """
        if isinstance(o, Accounting):
            # accounting object
            return {"petrol": o.petrol_price.price,
                    "charge": o.charge_of_gasoline.gasoline,
                    "accounting": o.expense
                    }
        # another
        return json.JSONEncoder.default(self, o)


def write(obj, fname='data/info.json'):
    """
    serialize user object in JSON
    :param obj: class User to serialize
    :param fname: file name
    :return: nothing
    """
    if not isinstance(obj, Accounting):
        raise ValueError('Incorrect type of variable obj')
    with open(fname, 'wt') as file:
        json.dump(obj, file, cls=AccountingEncoder, indent=4)


def encode_dict(dict):
    """
    decodes user from dictionary
    :param dict: decoded user
    :return: new user
    """
    ret_obj = Accounting()
    petrol_o = Petrol()
    charge_o = Charge()
    petrol_o.price = dict['petrol']
    charge_o.gasoline = dict['charge']
    ret_obj.charge_of_gasoline = charge_o
    ret_obj.petrol_price = petrol_o
    ret_obj.expense = dict['accounting']
    return ret_obj


def read(fname='data/info.json'):
    """
    read from JSON file object
    :param fname: file name
    :return: new User object or None
    """
    try:
        with open(fname, 'rt') as file:
            return encode_dict(json.load(file))
    except (OSError, ValueError):
        return None
