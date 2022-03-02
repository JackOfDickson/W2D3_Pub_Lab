class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
    
    def reduce_money_in_wallet(self, amount):
        self.wallet -= amount 
    

    def increase_drunkenness(self, drink_units):
        self.drunkenness += drink_units 