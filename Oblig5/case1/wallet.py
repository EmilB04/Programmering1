class Wallet:
    def __init__(self, amount):
        self.amount = amount
        
    def get_amount(self):
        return self.amount
        
    def subtract_amount(self, value):
        self.amount -= value
