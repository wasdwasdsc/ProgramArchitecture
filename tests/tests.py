"""

>>> from model.Accounting import Accounting

>>> accounting = Accounting()

>>> accounting.add('car3', 'Ai92', 348)
False

>>> accounting.add('car3', 'Ai92', 348)
False

>>> import datetime

>>> accounting.get_expense_by_date(datetime.datetime.today())
0

>>> accounting.add('car2', 'Ai98', 154)
False

>>> accounting.get_expense_by_date_and_car(datetime.datetime.today(), 'car2')
0

>>> accounting.petrol_price.add('Ai92', 19.5)
'petrol Ai92 added'

>>> accounting.petrol_price.add('Ai98', 0.5)
'petrol Ai98 added'

>>> accounting.petrol_price.add('diesel', 99.1)
'petrol diesel added'

>>> accounting.show_petrol()
Petrol - [('Ai92', 19.5), ('Ai98', 0.5), ('diesel', 99.1)]

>>>
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
