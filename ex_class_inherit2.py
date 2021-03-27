class User():

    def __init__(self, first_name, last_name,
            department, age):
            """Stores information about user"""
            self.first_name = first_name
            self.last_name = last_name
            self.department = department
            self.age = age
            self.login_attempts = 0
            
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

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Current login attempts: " + str(self.login_attempts))

    def reset_login_attempts(self):
        if self.login_attempts > 0:
            self.login_attempts = 0
        
class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post',
                "can ban user", "can create user"]

    def show_privileges(self):
        print("\nAdmins have the following privileges: ")
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):
    """Creates Admin class inheriting from class User"""
    def __init__(self, first_name, last_name, department, 
            age):
        """Initialize attr of parent class"""
        super().__init__(first_name, last_name, department, age)
        self.admin_privileges = Privileges()

my_admin = Admin('victor', 'trujillo', 'IT', 28)
my_admin.describe_user()
my_admin.admin.admin_privileges
