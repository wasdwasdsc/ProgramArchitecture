""" This is module for data control."""

from model.models import petrol_price, charge_of_gasoline, expense_accounting
import datetime
import time


def add_petrol(name, price):
    """Function to add new petrol.

    :param name: petrol name.
    :param price: petrol price.
    :returns: updates dictionary of petrols.

    >>> add_petrol('diesel', '99.1')
    'petrol diesel added'
    """
    petrol_price.update({name: price})
    return "petrol %s added" % name


def get_price_of_petrol(name):
    """Function to get price of existing petrol.

    :param name: petrol name.
    :returns: price by name.

    >>> get_price_of_petrol('Ai92')
    19.5
    """
    return petrol_price.get(name)


def del_petrol(name):
    """Function to delete existing petrol.

    :param name: petrol name.
    :returns: deletes petrol from dictionary.

    >>> del_petrol('Ai95')
    20.8
    """
    return petrol_price.pop(name)


def change_petrol(name, new_price):
    """Function to change existing petrol.

    :param name: petrol name.
    :param new_price: new price of a petrol.
    :returns: changes petrol price.

    >>> change_petrol('Ai98', 0.5)
    'petrol Ai98 changed'
    """
    petrol_price.update({name: new_price})
    return "petrol %s changed" % name


def get_charge_of_car(name):
    """Function to get charge of car.

    :param name: car name.
    :returns: charge of named car.

    >>> get_charge_of_car('car2')
    9
    """
    return charge_of_gasoline.get(name)


def add_car(name, charge):
    """Function to add new car.

    :param name: car name.
    :param charge: car charge.
    :returns: updates dictionary of cars.

    >>> add_car('bentley', 8.6)
    'bentley'
    """
    charge_of_gasoline.update({name: charge})
    return name


def del_car(name):
    """Function to delete existing car.

    :param name: car name.
    :returns: deletes car from dictionary.

    >>> del_car('car1')
    6.5
    """
    return charge_of_gasoline.pop(name)


def change_car(name, new_charge):
    """Function to change existing car.

    :param name: car name.
    :param new_charge: new charge of a car.
    :returns: modifies car dictionary.

    >>> change_car('car3', 12.1)
    12.1
    """
    charge_of_gasoline.update({name: new_charge})
    return new_charge


def add_record(car, petrol, distance):
    """Function to add new record.

    :param car: car name.
    :param petrol: petrol name.
    :param distance: distance made by a car.
    :returns: False if car or petrol is not existing or new record.

    >>> add_record('car3', 'Ai92', 348)
    True
    """
    date = datetime.datetime.today()
    if car in charge_of_gasoline.keys():
        if petrol in petrol_price.keys():
            new_record = {date: {car: petrol_price.get(petrol) * distance * charge_of_gasoline[car]}}
            expense_accounting.update(new_record)
            return True
        return False
    return False


def get_expense_by_date(date):
    """Function to get expenses by date.

    :param date: date to look for.
    :returns: money spent at this day.

    >>> add_record('car3', 'Ai92', 348)
    True
    >>> get_expense_by_date(datetime.datetime.today())
    13572.0
    """
    #print(date)
    res = 0
    """format = "%a %b %d %H:%M:%S %Y"
    for date_, car in expense_accounting.items():
        if date.strftime(format) == date_.date().strftime(format):
            res += [j for i, j in car.items()][0]"""

    for i in expense_accounting.items():
        if i[0].month == date.month and i[0].year == date.year and i[0].day == date.day:
            for j in i[1].items():
                res += j[1]
    return res


def get_expense_by_date_and_car(date, car):
    """Function to get expenses of car by date.

    :param date: date to look for.
    :param car: car name to look for.
    :returns: money spent at this day by this car.

    >>> add_record('car2', 'Ai98', 154)
    True
    >>> get_expense_by_date_and_car(datetime.datetime.today(), 'car2')
    77.0
    """
    res = 0
    # format = "%a %b %d %H:%M:%S %Y"
    # for date_, car_ in expense_accounting.items():
    #     if date.strftime(format) == date_.date().strftime(format) \
    #             and car == [i for i, j in car_.items()][0]:
    #         res += [j for i, j in car_.items()][0]

    for i in expense_accounting.items():
        if i[0].month == date.month and i[0].year == date.year and i[0].day == date.day:
            res += i[1].get(car, 0)
    return res

    return res


def show_petrol():
    """Shows all petrol and their price.

    >>> show_petrol()
    Petrol - [('Ai92', 19.5), ('Ai98', 0.5), ('diesel', '99.1')]
    """

    mass = [item for item in petrol_price.items()]
    mass.sort(key=lambda x: x[0])
    print("Petrol - %s" % mass)


def show_car():
    """Shows all cars and their charges.


    >>> show_car()
    Cars - [('bentley', 8.6), ('car2', 9), ('car3', 12.1)]
    """
    mass = [item for item in charge_of_gasoline.items()]
    mass.sort(key=lambda x: x[0])
    print("Cars - %s" % mass)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
