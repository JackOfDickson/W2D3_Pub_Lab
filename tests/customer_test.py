import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("George", 200, 19)

    def test_customer_has_name(self):
        self.assertEqual("George", self.customer.name)
    
    def test_customer_has_cash(self):
        self.assertEqual(200, self.customer.wallet)
    
    def test_customer_has_age(self):
        self.assertEqual(19, self.customer.age)

    def test_remove_money_from_wallet(self):
        self.customer.reduce_money_in_wallet(50)
        self.assertEqual(150, self.customer.wallet)
    
    def test_not_drunk(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_increase_drunkeness(self):
        drink = Drink("Tennants", 3.50, 2.1)
        self.customer.increase_drunkenness(drink.units)
        self.assertEqual(2.1, self.customer.drunkenness)