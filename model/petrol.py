class Petrol:
    def __init__(self):
        self.price = {}

    def add(self, name, price):
        """Function to add new petrol.

        :param name: petrol name.
        :param price: petrol price.
        :returns: updates dictionary of petrols.

        """
        self.price.update({name: price})
        return "petrol %s added" % name

    def get_price(self, name):
        """Function to get price of existing petrol.

        :param name: petrol name.
        :returns: price by name.

        """
        return self.price.get(name)

    def delete(self, name):
        """Function to delete existing petrol.

        :param name: petrol name.
        :returns: deletes petrol from dictionary.

        """
        return self.price.pop(name)

    def change(self, name, new_price):
        """Function to change existing petrol.

        :param name: petrol name.
        :param new_price: new price of a petrol.
        :returns: changes petrol price.

        """
        self.price.update({name: new_price})
        return "petrol %s changed" % name


