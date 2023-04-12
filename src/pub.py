class Pub:
    def __init__ (self, name, till):
        self.name = name
        self.till = till
        self.customers = [ ]

    def increase_cash(self, cash_amount):
        self.till += cash_amount

    def decrease_cash(self, cash_amount):
        self.till -= cash_amount

    # def sell_drink(self, customer, drink):
        
