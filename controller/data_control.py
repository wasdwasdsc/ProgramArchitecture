"""Menu for user interaction with program"""

from model.Accounting import Accounting
import datetime
from controller.cfgparser import cfgparse
from view.interface import Interface


class Controller:
    def __init__(self):
        self.read = cfgparse()[0]
        self.write = cfgparse()[1]
        main_accounting = self.read()
        if main_accounting is None:
            main_accounting = Accounting()
        self.accounting = main_accounting
        self.interface = Interface()

    def run(self):
        """This function calls for main menu"""

        self.main_menu()

    def main_menu(self):
        """Main menu"""

        while True:
            self.interface.print_main_menu()
            option = self.interface.input_my("What would you like to do? ")
            if option == '1':
                self.petrol_menu()
            elif option == '2':
                self.car_menu()
            elif option == '3':
                self.account_menu()
            elif option == '4':
                self.write(self.accounting)
                raise SystemExit
            elif option != "":
                self.interface.print_error('wrong input_my')

    def petrol_menu(self):
        """2nd level menu for petrol."""

        while True:
            self.interface.print_petrol_menu()
            option = self.interface.input_my("What would you like to do? ")
            if option == '1':
                p_name = self.interface.input_my("Enter petrol name.")
                p_price = float(self.interface.input_my("Enter petrol price."))
                self.accounting.petrol_price.add(p_name, p_price)
            elif option == '2':
                p_name = self.interface.input_my("Enter petrol name to delete.")
                self.accounting.petrol_price.delete(p_name)
            elif option == '3':
                p_name = self.interface.input_my("Enter petrol name to change.")
                p_price = float(self.interface.input_my("Enter new petrol price."))
                self.accounting.petrol_price.change(p_name, p_price)
            elif option == '4':
                p_name = self.interface.input_my("Enter petrol name to check price.")
                self.accounting.petrol_price.get_price(p_name)
            elif option == '5':
                self.accounting.show_petrol()
            elif option == '6':
                return
            elif option != "":
                self.interface.print_error('wrong input_my')

    def car_menu(self):
        """2nd level menu for cars."""

        while True:
            self.interface.print_car_menu()
            option = self.interface.input_my("What would you like to do? ")
            if option == '1':
                c_name = self.interface.input_my("Enter car name.")
                c_charge = float(self.interface.input_my("Enter car charge."))
                self.accounting.charge_of_gasoline.add_car(c_name, c_charge)
            elif option == '2':
                c_name = self.interface.input_my("Enter car name to delete.")
                self.accounting.charge_of_gasoline.del_car(c_name)
            elif option == '3':
                c_name = self.interface.input_my("Enter car name to change.")
                c_charge = float(self.interface.input_my("Enter new car charge."))
                self.accounting.charge_of_gasoline.change_car(c_name, c_charge)
            elif option == '4':
                c_name = self.interface.input_my("Enter car name to check charge.")
                self.accounting.charge_of_gasoline.get_charge_of_car(c_name)
            elif option == '5':
                self.accounting.show_car()
            elif option == '6':
                return
            elif option != "":
                self.interface.print_error('wrong input_my')

    def account_menu(self):
        """2nd level menu for accounting."""

        while True:
            self.interface.print_account_menu()
            option = self.interface.input_my("What would you like to do? ")
            if option == '1':
                c_name = self.interface.input_my("Enter car name.")
                p_name = self.interface.input_my("Enter petrol name.")
                dist = float(self.interface.input_my("Enter distance."))
                self.accounting.add(c_name, p_name, dist)
            elif option == '2':
                self.accounting.show_expense()
            elif option == '3':
                return
            elif option != "":
                self.interface.print_error('wrong input_my')
