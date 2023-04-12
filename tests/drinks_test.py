import unittest

from src.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks1 = Drinks("Tennants", 3)
        self.drinks2 = Drinks("IPA", 6)

    def test_drink_name(self):
        self.assertEqual("Tennants", self.drinks1.name)

    