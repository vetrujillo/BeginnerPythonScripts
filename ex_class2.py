class User():

    def __init__(self, first_name, last_name,
            department, age):
            """Stores information about user"""
            self.first_name = first_name
            self.last_name = last_name
            self.department = department
            self.age = age
            

    def describe_user(self):
        """Prints summary of user information"""
        print("\nPrinting summary of user info:")
        full_name = self.first_name + " " + self.last_name
        print("\nName: " + full_name.title())
        print("Department: " + self.department.title())
        print("Age: " + str(self.age))

    def greet_user(self):
        """Greets user"""
        full_name = self.first_name + " " + self.last_name
        print("\nHello, " + full_name.title() + "!")

user = User('victor', 'trujillo', 'IT', '28')
user.describe_user()
user.greet_user()

user2 = User('kayna', 'trujillo', 'engineering', 26)
user2.describe_user()
user2.greet_user()