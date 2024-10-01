class SandwichMaker:

    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < quantity:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity
        print(f"{sandwich_size} sandwich is ready. Bon appetit")


    def choice_decision(self, choice, recipes, cashier_instance):
        if choice in recipes:
            sandwich = recipes[choice]
            if self.check_resources(sandwich["ingredients"]):
                print(f"The cost of a {choice} sandwich is ${sandwich['cost']:.2f}")
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, sandwich["cost"]):
                    self.make_sandwich(choice, sandwich["ingredients"])
            else:
                print("Sorry, there are not enough resources to make that sandwich.")
        elif choice == "report":
            print("Current resources:")
            for resource, amount in self.check_resources().items():
                print(f"{resource}: {amount}")
        elif choice == "off":
            print("Turning off the machine. Goodbye!")
            return "off"
        else:
            print("Not a valid choice.")
        return "continue"