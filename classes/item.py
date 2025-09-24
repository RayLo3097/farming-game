import pygame
from classes.seed import Seed

"""
Item Generic class to be used for all items in the game

Class attributes:
    - name: A string representing the name of the item.
    - price: An integer representing the price of the item.
    - description: A string representing the description of the item.
    - quantity: An integer representing the quantity of the item.
    - image: A string representing the image of the item.
    - seed: A Seed object representing the seed associated with the item.


Class Methods:
    - update_price: This method is used to update the price of the item. It takes in the new price as a parameter. It updates the price of the item to the new price.
    - get_price: This method is used to get the price of the item.
    - get_name: This method is used to get the name of the item.
    - get_description: This method is used to get the description of the item.
    - get_image: This method is used to get the image of the item.

    Created by Daniel Barrera.
    Documented by Prince S.
"""


class Items:
    def __init__(
        self,
        name,
        price: float,
        sellprice: float,
        quantity,
        description,
        image,
        seed: Seed = None,
    ):
        self.name = name
        self.price = price
        self.sellprice = sellprice
        self.quantity = quantity
        self.description = description
        self.image = pygame.image.load(image)
        self.seed = seed


    def __eq__(self, value: object) -> bool:
        if value is None:
            return False
        
        if (self.name == value.name and 
            self.price == value.price and
            self.sellprice == value.sellprice and
            self.quantity == value.quantity and
            self.description == value.description and
            self.description == value.description and
            self.image == value.image):
            if self.seed == None and value.seed == None:
                return True
            elif self.seed == None or value.seed == None:
                return False
            elif self.seed == value.seed:
                return True 
        return False 

    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_sellprice(self):
        return self.sellprice

    def get_quantity(self):
        return self.quantity

    def get_description(self):
        return self.description

    def get_image(self):
        return self.image

    def __str__(self):
        return f"{self.name}: Price: {self.price}, Sell Price: {self.sellprice}, Quantity: {self.quantity}, Description: {self.description}"