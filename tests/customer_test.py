import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Stuart", 50)
        self.customer2 = Customer("Calum", 100)

    def test_does_customer_have_name(self):
        self.assertEqual("Stuart", self.customer1.name)

    def test_customer_reduce_cash(self):
        self.customer1.reduce_cash(-6)
        self.assertEqual(44, self.customer1.cash)