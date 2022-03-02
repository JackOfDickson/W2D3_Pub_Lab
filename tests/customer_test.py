import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("George", 200)

    def test_customer_has_name(self):
        self.assertEqual("George", self.customer.name)
    
    def test_customer_has_cash(self):
        self.assertEqual(200, self.customer.wallet)

    def test_remove_money_from_wallet(self):
        self.customer.reduce_money_in_wallet(50)
        self.assertEqual(150, self.customer.wallet)
    