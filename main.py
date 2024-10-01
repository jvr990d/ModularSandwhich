from random import choice

import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():

    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()
        result = sandwich_maker_instance.choice_decision(choice, recipes, cashier_instance)
        if result == "off":
            break

if __name__=="__main__":
    main()
