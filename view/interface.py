class Interface:
    def __init__(self):
        pass

    @staticmethod
    def print_main_menu():
        print("""
            1. Petrol.
            2. Car.
            3. Accounting.
            4. Quit
            """)

    @staticmethod
    def print_petrol_menu():
            print("""
            1. Add petrol.
            2. Delete petrol.
            3. Change petrol.
            4. Get price of petrol.
            5. Show available petrol.
            6. Go back to main menu.
            """)

    @staticmethod
    def print_car_menu():
            print("""
            1. Add car.
            2. Delete car.
            3. Change car.
            4. Get charge of car.
            5. Show available cars.
            6. Go back to main menu.
            """)

    @staticmethod
    def print_account_menu():
        print("""
            1. Add record.
            2. Show expense records.
            3. Go back to main menu.
            """)

    @staticmethod
    def print_error(err):
        print("Error: %s" % err)

    @staticmethod
    def print_data(str):
        print(str)

    @staticmethod
    def input_my(str):
        return input(str)
