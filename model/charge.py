class Charge:
    def __init__(self):
        self.gasoline = {}

    def get_charge_of_car(self, name):
        """Function to get charge of car.

        :param name: car name.
        :returns: charge of named car.

        """
        return self.gasoline.get(name)

    def add_car(self, name, charge):
        """Function to add new car.

        :param name: car name.
        :param charge: car charge.
        :returns: updates dictionary of cars.

        """
        self.gasoline.update({name: charge})
        return name

    def del_car(self, name):
        """Function to delete existing car.

        :param name: car name.
        :returns: deletes car from dictionary.

        """
        return self.gasoline.pop(name)

    def change_car(self, name, new_charge):
        """Function to change existing car.

        :param name: car name.
        :param new_charge: new charge of a car.
        :returns: modifies car dictionary.

        """
        self.gasoline.update({name: new_charge})
        return new_charge
