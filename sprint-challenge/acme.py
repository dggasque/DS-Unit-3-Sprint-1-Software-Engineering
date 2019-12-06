"""
Some explanatory text here
"""

import random


class Product:
    """
    An abstract representation of an Acme product
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 10000000)

    def stealability(self):
        """
        Method that calculates the stealability of a product
        """
        steal_ratio = self.price/self.weight
        if steal_ratio < 0.5:
            return "Not so stealable."
        if steal_ratio >= 0.5 and steal_ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """
        Method that determines weather a product will explode
        """
        boom_ratio = self.flammability*self.weight
        if boom_ratio < 10:
            return "...fizzle."
        if boom_ratio >= 10 and boom_ratio < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """
    A subclass of the product class
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        if self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
