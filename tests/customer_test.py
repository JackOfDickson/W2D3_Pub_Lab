import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("George", 200)

    def test_customer_has_name(self):
        self.assertEqual("George", self.customer.name)
    
    def test_customer_has_cash(self):
        self.assertEqual(200, self.customer.wallet)