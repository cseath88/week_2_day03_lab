import unittest

from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Dreadnought", 1000)

    def test_pub_has_name(self):
        self.assertEqual("Dreadnought", self.pub.name)

    def test_pub_has_money_in_till(self):
        self.assertEqual(1000, self.pub.till)

    # def test_can_pub_increase_till(self):
    #     self.pub.increase_cash(6)
    #     self.assertEqual(1006, self.pub.till)

    # def test_can_pub_decrease_till(self):
    #     self.pub.decrease_cash(-50)
    #     self.assertEqual(950, self.pub.till)

    
