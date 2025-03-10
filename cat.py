"""Class with the methods and attributes for a cat. Cats can be tamed, fed and 
hit. They have names, health, fish and can given gifts."""

import random

class Cat:
    """Class for creating a cat. Cats can be tamed, fed and hit. They have 
    names, health, fish and can given gifts."""
    def __init__(self, name : str):
        """Initializes whether the cat is tame and/or, their health, number of fish, 
        if the cat gave a gift or not. Accepts cat's name as parameter."""
        self.isTame = False
        self.isAlive = True
        self.name = name
        self.health = 2.0
        self.fish = 0
        self.gift = False

    def feed(self):
        """Fish increases by 1. Health increases by 1 if it's not at its maximum of
            4. 50% chance of cat getting tamed. If the cat is overfed (more then 3
            fish), they die."""
        if self.isAlive:
            self.fish += 1
            # If there's more than 3 fish in the cat, they die
            if self.fish > 3:
                self.isAlive = False 
            # Health can be a maximum of 4
            if self.health + 1.0 <= 4.0:
                self.health += 1
            # 50% of cat becoming tamed
            tameNumber = random.randint(1,2)
            if tameNumber == 1:
                self.isTame = True
        # Exception handling
        else:
            print("You can't feed dead cats.")
    
    def hit(self):
        """Cat becomes wild. Health decreases by 1.5. If health is zero, cat dies."""
        self.isTame = False # Cat always becomes wild
        # Health can be a minimum of 0.
        if self.health - 1.5 >= 0:
            self.health -= 1.5
        # If health is below 1.5 but not zero, when the cat is hit their health shoul drop to 0
        else:
            self.health = 0
            self.isAlive = False
        
    def night(self):
        if self.isAlive:
            # If the cat is tame and has fish, it will drop a gift
            if self.isTame and self.fish > 0:
                self.gift = True
            # Fish decreases by 1 but can't be below 0
            if self.fish - 1 > 0:
                self.fish -= 1
            else:
                self.fish = 0
                # If the cat has no fish, it becomes wild
                self.isTame = False
        
    def __str__(self):
        """Returns the cat's status (if they're alive and/or tame, their name,
            health and number of fish) when object is printed. """
        # Converts booleans to string
        aliveStatement = "DEAD"
        if self.isAlive:
            aliveStatement = "Alive"
            
        tameStatement = "Wild"
        if self.isTame:
            tameStatement = "Tame"
        
        return f"{self.name}: {aliveStatement} | {tameStatement} | Health: {self.health:.1f} | Fish: {self.fish}"