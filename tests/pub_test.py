import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("Tennants", 3.50, 2.1)
        self.drink2 = Drink("Merlot", 4.50, 2.4)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_money(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)
        # self.assertEqual(102.50, self.pub.till)
    
    def test_drinks_list_is_empty(self):
        self.assertEqual([], self.pub.drinks)

    def test_add_drink_to_menu(self):
        self.pub.add_drink_to_menu(self.drink1)
        number_of_drinks = self.pub.check_number_of_drinks()

        self.assertEqual(1, number_of_drinks)
    
    def test_add_multiple_drinks_to_menu(self):
        self.pub.add_drink_to_menu(self.drink1)
        self.pub.add_drink_to_menu(self.drink2)
        number_of_drinks = self.pub.check_number_of_drinks()

        self.assertEqual(2, number_of_drinks)
    
    def test_remove_drink(self):
        self.pub.add_drink_to_menu(self.drink1)
        self.pub.remove_drink_from_menu(self.drink1)
        number_of_drinks = self.pub.check_number_of_drinks()

        self.assertEqual(0, number_of_drinks)

    def test_sell_drink(self):
        self.pub.add_drink_to_menu(self.drink1)
        customer = Customer("Derek", 100, 60)
        drink = self.drink1
        self.pub.sell_drink_to_customer(drink, customer)

        self.assertEqual(96.5, customer.wallet)
        self.assertEqual(103.5, self.pub.till)
