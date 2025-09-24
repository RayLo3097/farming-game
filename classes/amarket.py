from classes.item import Items
from classes.inventory import Inventory
from classes.player import Player
from classes.seed import Seed

"""
This is the Market class. It contains all the data and methods related to the market in the game.
This is the rudimentary version of the market. It is used to store the products in the market and the capacity of the market.

The class has the following methods:
    - __init__: This method is used to initialize the market object. It takes in the products as a parameter. It initializes the market with the given products.
    - listProducts: This method is used to list all the products in the market.
    - getProducts: This method is used to get the products in the market.
    - getMarketCap: This method is used to get the capacity of the market.
    - addProduct: This method is used to add a product to the market. It takes in the name, price, quantity, description, image, and seed as parameters. It adds the product to the market.
    - removeProduct: This method is used to remove a product from the market. It takes in the name of the product as a parameter. It removes the product from the market.
    - sellProduct: This method is used to sell a product from the inventory. It takes in the product as a parameter. It adds the money to the player's account.
    - buyProduct: This method is used to buy a product from the market. It takes in the product as a parameter. It removes the money from the player's account.

The class has the following attributes:
    - products: A list representing the products in the market.
    - marketCapacity: An integer representing the capacity of the market.


Created by Prince S.
Documented by Prince S.


"""


class Market:
    # Constructor

    # What does the market contain?
    # The market contains a list of products
    # User can sell harvested materials here
    # User can buy equipment here
    # User can buy seeds here

    def __init__(self, products=[], inventory: Inventory = None, player: Player = None):
        self.products = products
        self.marketCapacity = 25  # Maximum number of products in the market
        self.inventory = inventory
        self.player = player

    # Method0

    def listProducts(products):
        """List all products in the market"""
        for product in products:
            print(product)

    def getProducts(self):
        return self.products

    def getMarketCap(self):
        return self.marketCapacity

    def addProduct(
        self,
        name: str,
        price: float,
        sellprice: float,
        quantity: int,
        description: str,
        image: str,
        seed: Seed = None,
    ):
        """Add a product to the market. Raises an exception if the market is full."""
        # Check if adding this product would exceed the market's capacity
        if len(self.products) >= self.marketCapacity:
            raise Exception("Cannot add product: market is at full capacity.")

        # Proceed to add the product if capacity allows
        item = Items(name, price, sellprice, quantity, description, image, seed)
        self.products.append(item)

    def removeProduct(self, name: str):
        """Remove a product from the market"""
        for product in self.products:
            if product.get_name() == name:
                self.products.remove(product)
                return True
        return False

    # Sell product chosen from inventory
    # Add money to player's account
    def sellProduct(self, product: Items):
        if product.name in self.inventory.get_handContents():
            retrived_item = self.inventory.get_handContents().get(product.name)
            if retrived_item.quantity == 1:
                self.inventory.remove_handitem(retrived_item)
        if product.name in self.inventory.get_contents():
            retrived_item = self.inventory.get_contents().get(product.name)
            self.inventory.rem_item(retrived_item)
            self.player.incMoney(retrived_item.sellprice)
        else:
            print("You do not have this item in your inventory")
            return False

    # Buy product from market
    # Remove money from player's account
    def buyProduct(self, product):
        if product in self.products:
            if self.player.getMoney() >= product.get_price():
                self.player.decMoney(product.get_price())
                self.inventory.add_item(product)
                return True
            else:
                print("You do not have enough money to buy this item")
                return False
        else:
            print("This item is not available in the market")
            return False