'''
This class handles the storage & management of items such as seeds, fertilizers, pesticides, and other resources.

Class Attributes:
    - __contents: A list representing the contents of the inventory.
    - __bagcapacity: An integer representing the capacity of the inventory.
    - __inHand: A list representing the contents of the hand.
    - __handCapacity: An integer representing the capacity of the hand.



Class Methods:
    - get_contents: This method is used to get the contents of the inventory. It returns the contents of the inventory.
    - add_item: This method is used to add an item to the inventory. It takes in the item as a parameter. It adds the item to the inventory.
    - add_handitem: This method is used to add an item to the hand. It takes in the item as a parameter. It adds the item to the hand.
    - remove_handitem: This method is used to remove an item from the hand. It takes in the item as a parameter. It removes the item from the hand.
    - rem_item: This method is used to remove an item from the inventory. It takes in the item as a parameter. It removes the item from the inventory.
    - set_capacity: This method is used to set the capacity of the inventory. It takes in the capacity as a parameter. It sets the capacity of the inventory to the given capacity.
    - get_capacity: This method is used to get the capacity of the inventory. It returns the capacity of the inventory.
    - get_handCapacity: This method is used to get the capacity of the hand. It returns the capacity of the hand.
    - get_handContents: This method is used to get the contents of the hand. It returns the contents of the hand.

    
    Created by Prince S.
    Documented by Prince S.

'''
from classes.item import Items


# Inventory Class
class Inventory:

    __contents: list
    __bagcapacity: int

    __inHand: list
    __handCapacity: int

    def __init__(self, handCapacity=1, bagcapacity=10, contents={}, handContents={}):
        # For right now, only contents and capacity
        # Contents will contain an array or hashmap of items(Generic)
        self.capacity = bagcapacity
        self.handCapacity = handCapacity
        self.contents = contents if contents is not None else {}
        self.handContents = handContents if handContents is not None else {}

    # return list of items in inventory
    def get_contents(self):
        return self.contents

    # add item to inventory
    def add_item(self, item: Items):
        if item == None:
            return
        elif item.quantity <= 0:
            item.quantity = 1

        if len(self.contents) == 0:
            self.contents[item.name] = item
            return
        if len(self.contents) <= self.capacity: # Check if inventory is full
            if item.name in self.contents: # Check if item is already in inventory
                item_object = self.contents.get(item.name)
                item_object.quantity += 1
            else: # Add item to inventory
                self.contents[item.name] = item
            
    def add_handitem(self, item: Items):
        self.handContents = {}
        if item == None:
            return
        elif item.quantity <= 0:
            item.quantity = 1

        if len(self.handContents) < self.handCapacity:
            self.handContents[item.name] = item
        

    def remove_handitem(self, item):
        if item == None:
            return
        if item.name in self.handContents:
            del self.handContents[item.name]


    # remove item from inventory
    def rem_item(self, item):
        if item == None:
            return
        if item.name in self.contents:
            retrieved_item = self.contents.get(item.name)
            if retrieved_item.quantity == 1:
                del self.contents[item.name]
            else:
                retrieved_item.quantity -= 1

    # In the case we choose to increase inventory capacity
    # via backpack or other means

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def get_handCapacity(self):
        return self.handCapacity

    def get_handContents(self):
        return self.handContents
