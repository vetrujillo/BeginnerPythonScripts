class Restaurant():
    """Store restaurant info"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describes restaurant"""
        print("This restaurant's name is " + self.name.title() + ".")
        print("This restaurant's cuisine is " + self.cuisine.title() + ".")
        print("This restaurant has served " + str(self.number_served) + " customers.")

    def open_restaurant(self):
        """Prints string saying restaurant is open"""
        print(self.name.title() + " is open!")

    def set_number_served(self, served):
        """Set number of customers served"""
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You can't unserve people!")

    def increment_served(self, increment):
        """Incrementally increase number served"""
        self.number_served += increment

my_restaurant = Restaurant('bella sera', 'italian')
my_restaurant.open_restaurant()

my_restaurant.number_served = 5
my_restaurant.increment_served(100)
my_restaurant.describe_restaurant()