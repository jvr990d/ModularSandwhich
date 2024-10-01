class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("How many Large dollars ($1)?: "))
        half_dollars = int(input("How many half dollars dollars?: "))
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = dollars + half_dollars * 0.5 + quarters * 0.25 + dimes *0.1 + nickles * 0.05 + pennies * 0.01
        return total
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        #coins = self.process_coins()
        change = coins - cost
        if coins < cost:
            print("Sorry, that’s not enough money.Money refunded.")
            return False
        elif coins > cost:
            print(f"Here is your change: {change} ")
            return True
        else:
            return True