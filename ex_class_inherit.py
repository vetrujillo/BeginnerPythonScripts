class Restaurant():
    """Store restaurant info"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describes restaurant"""
        print("\nThis restaurant's name is " + self.name.title() + ".")
        print("This restaurant's cuisine is " + self.cuisine.title() + ".")

    def open_restaurant(self):
        """Prints string saying restaurant is open"""
        print(self.name.title() + " is open!")

class IceCreamStand(Restaurant):
    """Creates Ice Cream stand inheriting from parent class Restaurant"""
    def __init__(self, name, cuisine):
        """Initialize attr of parent class"""
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def get_flavors(self):
        """Retrieves flavors from list and prints each one"""
        print("We have the following flavors available: ")
        for flavor in self.flavors:
            print("\n" + flavor.title())

my_ice_cream = IceCreamStand('fav flavors', 'frozen dessert')
my_ice_cream.describe_restaurant()
my_ice_cream.open_restaurant()
my_ice_cream.get_flavors()