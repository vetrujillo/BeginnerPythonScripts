from random import randint

class Die():
    """Virtual die"""

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        result = randint(1, self.sides)
        print("The die reads: " + str(result))

    def roll_10(self):
        for x in range(10):
            print("The die reads: " + str(randint(1,self.sides)))

class Die_10(Die):
    """Virtual 10-sided die"""

    def __init__(self):
        """Initialize attr of parent class"""    
        super().__init__()
        self.sides = 10

class Die_20(Die):
    """Virtual 20-sided die"""

    def __init__(self):
        """Initialize attr of parent class"""
        super().__init__()
        self.sides = 20

die_roll = Die()
die_roll.roll_10()

die_roll10 = Die_10()
print("\n")  
die_roll10.roll_10()

die_roll20 = Die_20()
print("\n")
die_roll20.roll_10()