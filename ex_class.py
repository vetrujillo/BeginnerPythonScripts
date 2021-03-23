class Restaurant():
    """Store restaurant info"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describes restaurant"""
        print("This restaurant's name is " + self.name.title() + ".")
        print("This restaurant's cuisine is " + self.cuisine.title() + ".")

    def open_restaurant(self):
        """Prints string saying restaurant is open"""
        print(self.name.title() + " is open!")

my_restaurant = Restaurant('bella sera', 'italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()