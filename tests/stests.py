"""
module with unittests
for testing serialization methods
"""
import unittest
from model.Accounting import Accounting
from serialization.tojson import AccountingEncoder, encode_dict
import yaml
import json
import pickle
import datetime


class TestSerialization(unittest.TestCase):

    def create_accounting(self):
        """
        :return: Accounting object
        """
        acc = Accounting()
        acc.petrol_price.add("Ai92", 22)
        acc.add("test", "test", 200)
        acc.charge_of_gasoline.add_car("zaz01", 10)
        acc.add("zaz01", "Ai92", 100)
        return acc

    def test_yaml(self):
        """
        test yaml serialization
        :return: nothing
        """

        obj = self.create_accounting()
        stringIO = yaml.dump(obj)
        obj1 = yaml.load(stringIO)
        for p1, p2 in zip(obj.expense, obj1.expense):
            self.assertEqual(p1, p2)
        for p1, p2 in zip(obj.petrol_price.price, obj1.petrol_price.price):
            self.assertEqual(p1, p2)
        for p1, p2 in zip(obj.charge_of_gasoline.gasoline, obj1.charge_of_gasoline.gasoline):
            self.assertEqual(p1, p2)

    def test_json(self):
        """
        test json serialization
        :return: nothing
        """
        obj = self.create_accounting()
        stringIO = json.dumps(obj, cls=AccountingEncoder)
        obj1 = encode_dict(json.loads(stringIO))
        for p1, p2 in zip(obj.expense, obj1.expense):
            self.assertEqual(p1, p2)
        for p1, p2 in zip(obj.petrol_price.price, obj1.petrol_price.price):
            self.assertEqual(p1, p2)
        for p1, p2 in zip(obj.charge_of_gasoline.gasoline, obj1.charge_of_gasoline.gasoline):
            self.assertEqual(p1, p2)

    def test_pickle(self):
        """
        test pickle serialization
        :return: nothing
        """
        obj = self.create_accounting()
        stringIO = pickle.dumps(obj)
        obj1 = pickle.loads(stringIO)
        for p1, p2 in zip(obj.expense, obj1.expense):
            self.assertEqual(p1, p2)
        for p1, p2 in zip(obj.petrol_price.price, obj1.petrol_price.price):
            self.assertEqual(p1, p2)
        for p1, p2 in zip(obj.charge_of_gasoline.gasoline, obj1.charge_of_gasoline.gasoline):
            self.assertEqual(p1, p2)

if __name__ == '__main__':
    unittest.main()
