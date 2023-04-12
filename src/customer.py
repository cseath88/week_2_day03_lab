class Customer:
    def __init__ (self, name, cash):
        self.name = name
        self.cash = cash

    def reduce_cash(self, wallet_amount):
        self.cash -= wallet_amount