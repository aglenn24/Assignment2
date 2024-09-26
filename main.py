import data
import cashier
import sandwich_maker
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():

    while True:
        user_choice = input("What type of sandwich would you like?\n small, medium, large: ")
        cashier_instance.process_coins()
        if cashier_instance.transaction_result(cashier_instance.coins, recipes[user_choice]["cost"]):
            sandwich_maker_instance.make_sandwich(user_choice, recipes[user_choice]["ingredients"])
        user_choice = input("Would you like to make another sandwich? (yes/no): ")
        if not user_choice.lower() == "yes" or user_choice.lower() == "y":
            print("Have a good day!")
            break


if __name__=="__main__":
    main()
