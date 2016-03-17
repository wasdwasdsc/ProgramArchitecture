"""Menu for user interaction with program"""

from controller.data_control import get_expense_by_date_and_car,\
    add_car, add_petrol, add_record, change_car, \
    change_petrol, del_car, del_petrol, get_charge_of_car, \
    get_expense_by_date, get_price_of_petrol, show_car, \
    show_petrol
import datetime


def run():
    """This function calls for main menu"""

    main_menu()


def main_menu():
    """Main menu"""

    while True:
        print("""
        1. Petrol.
        2. Car.
        3. Accounting.
        4. Quit
        """)
        option = input("What would you like to do? ")
        if option == '1':
            petrol_menu()
        elif option == '2':
            car_menu()
        elif option == '3':
            account_menu()
        elif option == '4':
            raise SystemExit
        elif option != "":
            print("Invalid input. Try again\n")


def petrol_menu():
    """2nd level menu for petrol."""

    while True:
        print("""
        1. Add petrol.
        2. Delete petrol.
        3. Change petrol.
        4. Get price of petrol.
        5. Show available petrol.
        6. Go back to main menu.
        """)
        option = input("What would you like to do? ")
        if option == '1':
            p_name = input("Enter petrol name.")
            p_price = float(input("Enter petrol price."))
            add_petrol(p_name, p_price)
        elif option == '2':
            p_name = input("Enter petrol name to delete.")
            del_petrol(p_name)
        elif option == '3':
            p_name = input("Enter petrol name to change.")
            p_price = float(input("Enter new petrol price."))
            change_petrol(p_name, p_price)
        elif option == '4':
            p_name = input("Enter petrol name to check price.")
            get_price_of_petrol(p_name)
        elif option == '5':
            show_petrol()
        elif option == '6':
            return
        elif option != "":
            print("Invalid input. Try again\n")


def car_menu():
    """2nd level menu for cars."""

    while True:
        print("""
        1. Add car.
        2. Delete car.
        3. Change car.
        4. Get charge of car.
        5. Show available cars.
        6. Go back to main menu.
        """)
        option = input("What would you like to do? ")
        if option == '1':
            c_name = input("Enter car name.")
            c_charge = float(input("Enter car charge."))
            add_car(c_name, c_charge)
        elif option == '2':
            c_name = input("Enter car name to delete.")
            del_car(c_name)
        elif option == '3':
            c_name = input("Enter car name to change.")
            c_charge = float(input("Enter new car charge."))
            change_car(c_name, c_charge)
        elif option == '4':
            c_name = input("Enter car name to check charge.")
            get_charge_of_car(c_name)
        elif option == '5':
            show_car()
        elif option == '6':
            return
        elif option != "":
            print("Invalid input. Try again\n")


def account_menu():
    """2nd level menu for accounting."""

    while True:
        print("""
        1. Add record.
        2. Expense by date.
        3. Expense by car.
        4. Go back to main menu.
        """)
        option = input("What would you like to do? ")
        if option == '1':
            c_name = input("Enter car name.")
            p_name = input("Enter petrol name.")
            dist = float(input("Enter distance."))
            add_record(c_name, p_name, dist)
        elif option == '2':
            year = int(input("Enter year."))
            month = int(input("Enter month."))
            day = int(input("Enter day."))
            if year < 2017 and 0 < month < 13 and 0 < day < 31:
                print(get_expense_by_date(datetime.date(year, month, day)))
            else:
                print("You have entered wrong date.\n")
        elif option == '3':
            year = int(input("Enter year."))
            month = int(input("Enter month."))
            day = int(input("Enter day."))
            c_name = input("Enter car name.")
            if year < 2017 and 0 < month < 13 and 0 < day < 31:
                print(get_expense_by_date_and_car(datetime.date(year, month,
                                                                day), c_name))
            else:
                print("You have entered wrong date.\n")
        elif option == '4':
            return
        elif option != "":
            print("Invalid input. Try again\n")
