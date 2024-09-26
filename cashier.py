class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        self.coins = float(input("How many quarters do you have? " ))
        self.coins = self.coins * 0.25
        self.coins = self.coins + ( float(input("How many dimes? ")) * .10)
        

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print("Transaction successful!")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
