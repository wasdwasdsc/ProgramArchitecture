"""

>>> from model.Accounting import Accounting
>>> from model.charge import Charge
>>> from model.petrol import Petrol

>>> chrg = Charge()
>>> ptr = Petrol()
>>> accounting = Accounting()

>>> chrg.add_car('test1', 100)
'test1'

>>> chrg.change_car('test1', 200)
200

>>> chrg.get_charge_of_car('test1')
200

>>> chrg.del_car('test1')
200

>>> chrg.add_car('test1', 100)
'test1'

>>> ptr.add('test1', 20.5)
'petrol test1 added'

>>> ptr.change('test1', 30.5)
'petrol test1 changed'

>>> ptr.get_price('test1')
30.5

>>> ptr.delete('test1')
30.5

>>> ptr.add('test1', 20.5)
'petrol test1 added'

>>> accounting.add('car3', 'Ai92', 348)
False

>>> accounting.add('car3', 'Ai92', 348)
False

>>> accounting.add('car2', 'Ai98', 154)
False

>>> accounting.petrol_price.add('Ai92', 19.5)
'petrol Ai92 added'

>>> accounting.petrol_price.add('Ai98', 0.5)
'petrol Ai98 added'

>>> accounting.petrol_price.add('diesel', 99.1)
'petrol diesel added'

>>> accounting.charge_of_gasoline.add_car('test1', 100)
'test1'

>>> accounting.show_petrol()
Petrol - [('Ai92', 19.5), ('Ai98', 0.5), ('diesel', 99.1)]

>>> accounting.show_car()
Cars - [('test1', 100)]

>>> accounting.add('test1', 'Ai98', 200)
True

>>> accounting.show_expense()
Expense - [('2016-04-25', {'test1': 10000.0})]
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
