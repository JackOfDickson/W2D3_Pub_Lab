class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_menu(self, drink):
        self.drinks.append(drink)
    
    def check_number_of_drinks(self):
        return len(self.drinks)

    def remove_drink_from_menu(self, drink):
        