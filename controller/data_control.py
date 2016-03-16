from model.models import petrol_price, charge_of_gasoline, expense_accounting
import datetime
import time


def add_petrol(name, price):
    petrol_price.update({name: price})
    return


def get_price_of_petrol(name):
    return petrol_price.get(name)


def del_petrol(name):
    return petrol_price.pop(name)


def change_petrol(name, new_price):
    return petrol_price.update({name: new_price})


def get_charge_of_car(name):
    return charge_of_gasoline.get(name)


def add_car(name, charge):
    return charge_of_gasoline.update({name: charge})


def del_car(name):
    return charge_of_gasoline.pop(name)


def change_car(name, new_charge):
    return charge_of_gasoline.update({name: new_charge})


def add_record(car, petrol, distance):
    date = datetime.datetime.today()
    if car in charge_of_gasoline.keys():
        if petrol in petrol_price.keys():
            new_record = {date: {car: petrol_price.get(petrol)*distance}}
            expense_accounting.update(new_record)
            return new_record
        return False
    return False


def get_expense_by_date(date):
    print(date)
    res = 0
    format = "%a %b %d %H:%M:%S %Y"
    for date_, car in expense_accounting.items():
        if date.strftime(format) == date_.date().strftime(format):
            res += [j for i, j in car.items()][0]
    return res


def get_expense_by_date_and_car(date, car):
    res = 0
    format = "%a %b %d %H:%M:%S %Y"
    for date_, car_ in expense_accounting.items():
        if date.strftime(format) == date_.date().strftime(format) and car == [i for i, j in car_.items()][0]:
            res += [j for i, j in car_.items()][0]
    return res


if __name__ == '__main__':
    add_record("car2", "Ai92", 100)
    time.sleep(0.1)
    add_record("car1", "Ai92", 200)
    time.sleep(0.1)
    add_record("car1", "Ai92", 300)
    time.sleep(0.1)
    add_record("car1", "Ai92", 400)
    print(get_expense_by_date(datetime.date(2016, 3, 17)))
    print(get_expense_by_date_and_car(datetime.date(2016, 3, 17), "car2"))
