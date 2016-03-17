""" This is module for data control."""

from model.models import petrol_price, charge_of_gasoline, expense_accounting
import datetime
import time


def add_petrol(name, price):
    """Function to add new petrol.

    :param name: petrol name.
    :param price: petrol price.
    :returns: updates dictionary of petrols."""
    return petrol_price.update({name: price})


def get_price_of_petrol(name):
    """Function to get price of existing petrol.

    :param name: petrol name.
    :returns: price by name."""
    return petrol_price.get(name)


def del_petrol(name):
    """Function to delete existing petrol.

    :param name: petrol name.
    :returns: deletes petrol from dictionary."""
    return petrol_price.pop(name)


def change_petrol(name, new_price):
    """Function to change existing petrol.

    :param name: petrol name.
    :param new_price: new price of a petrol.
    :returns: changes petrol price."""
    return petrol_price.update({name: new_price})


def get_charge_of_car(name):
    """Function to get charge of car.

    :param name: car name.
    :returns: charge of named car."""
    return charge_of_gasoline.get(name)


def add_car(name, charge):
    """Function to add new car.

    :param name: car name.
    :param charge: car charge.
    :returns: updates dictionary of cars."""
    return charge_of_gasoline.update({name: charge})


def del_car(name):
    """Function to delete existing car.

    :param name: car name.
    :returns: deletes car from dictionary."""
    return charge_of_gasoline.pop(name)


def change_car(name, new_charge):
    """Function to change existing car.

    :param name: car name.
    :param new_charge: new charge of a car.
    :returns: modifies car dictionary."""
    return charge_of_gasoline.update({name: new_charge})


def add_record(car, petrol, distance):
    """Function to add new record.

    :param car: car name.
    :param petrol: petrol name.
    :param distance: distance made by a car.
    :returns: False if car or petrol is not existing or new record."""
    date = datetime.datetime.today()
    if car in charge_of_gasoline.keys():
        if petrol in petrol_price.keys():
            new_record = {date: {car: petrol_price.get(petrol) * distance}}
            expense_accounting.update(new_record)
            return new_record
        return False
    return False


def get_expense_by_date(date):
    """Function to get expenses by date.

    :param date: date to look for.
    :returns: money spent at this day."""
    print(date)
    res = 0
    format = "%a %b %d %H:%M:%S %Y"
    for date_, car in expense_accounting.items():
        if date.strftime(format) == date_.date().strftime(format):
            res += [j for i, j in car.items()][0]
    return res


def get_expense_by_date_and_car(date, car):
    """Function to get expenses of car by date.

    :param date: date to look for.
    :param car: car name to look for.
    :returns: money spent at this day by this car."""
    res = 0
    format = "%a %b %d %H:%M:%S %Y"
    for date_, car_ in expense_accounting.items():
        if date.strftime(format) == date_.date().strftime(format) \
                and car == [i for i, j in car_.items()][0]:
            res += [j for i, j in car_.items()][0]
    return res


def show_petrol():
    """Shows all petrol and their price.

    >>> show_petrol()
    Petrol - [('Ai92', 19.5), ('Ai95', 20.8), ('Ai98', 22.3)]
    """

    mass = [item for item in petrol_price.items()]
    mass.sort(key=lambda x: x[0])
    print("Petrol - %s" % mass)


def show_car():
    """Shows all cars and their charges."""

    print("Cars - %s" % charge_of_gasoline.items())


if __name__ == '__main__':
    import doctest

    doctest.testmod()
