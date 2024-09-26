
class SandwichMaker:
   
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] >= ingredients["bread"] and self.machine_resources["ham"] >= ingredients["ham"] and self.machine_resources["cheese"] >= ingredients["cheese"]:
            return True
        else:
            return False
        
        

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.check_resources(order_ingredients)
        self.machine_resources["bread"] = self.machine_resources["bread"] - order_ingredients["bread"]
        self.machine_resources["ham"] = self.machine_resources["ham"] - order_ingredients["ham"]
        self.machine_resources["cheese"] = self.machine_resources["cheese"] - order_ingredients["cheese"]
        print("Sandwich is ready!")