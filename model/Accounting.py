"""Data to work with"""

import datetime
from model.Charge import Charge
from model.Petrol import Petrol


class Accounting:
    def __init__(self):
        self.charge_of_gasoline = Charge()
        self.petrol_price = Petrol()
        self.expense = {}

    def add(self, car, petrol, distance):
        """Function to add new record.

        :param car: car name.
        :param petrol: petrol name.
        :param distance: distance made by a car.
        :returns: False if car or petrol is not existing or new record.

        """
        date = datetime.datetime.today()
        if car not in self.charge_of_gasoline.gasoline or petrol not in self.petrol_price.price:
            return False
        new_record = {date.strftime("%a, %d %b %Y %H:%M:%S +0000"): {car: self.petrol_price.get_price(petrol) * distance * self.charge_of_gasoline.gasoline[car]}}
        self.expense.update(new_record)
        return True

    def show_expense(self):
        """Show all expense records

        """
        mass = [item for item in self.expense.items()]
        mass.sort(key=lambda x: x[0])
        print("Expense - %s" % mass)

    def show_petrol(self):
        """Shows all petrol and their price.

        """

        mass = [item for item in self.petrol_price.price.items()]
        mass.sort(key=lambda x: x[0])
        print("Petrol - %s" % mass)

    def show_car(self):
        """Shows all cars and their charges.

        """
        mass = [item for item in self.charge_of_gasoline.gasoline.items()]
        mass.sort(key=lambda x: x[0])
        print("Cars - %s" % mass)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
