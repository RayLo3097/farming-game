
'''

Class attributes:
    - _price: An integer representing the price of the soil.
    - _fertilizer_amount: An integer representing the amount of fertilizer in the soil.
    - _water_amount: An integer representing the amount of water in the soil.

Class methods:

    - __init__(self, fertilizer_amount: int = 0, water_amount: int = 0): Initializes the Soil object with the given fertilizer and water amounts.
    - __eq__(self, __value: object) -> bool: Compares the Soil object with another object to check if they are equal.
    - fertilizer_amount(self): Getter method for the fertilizer amount.
    - water_amount(self): Getter method for the water amount.
    - price(self): Getter method for the price.
    - fertilizer_amount(self, value: int): Setter method for the fertilizer amount.
    - water_amount(self, value: int): Setter method for the water amount.
    - is_fertilized(self) -> bool: Checks if the soil is fertilized.
    - is_watered(self) -> bool: Checks if the soil is watered.

Created by Raymond Lo.
Documented by Prince S.

'''
# Class for the soil
class Soil:
    _price: int = 0

    # Initializer method
    def __init__(self, fertilizer_amount: int = 0, water_amount: int = 0):
        self.fertilizer_amount = fertilizer_amount
        self.water_amount = water_amount
    # Comparison method
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Soil):
            return False
        return (self._fertilizer_amount == __value._fertilizer_amount 
                and self._water_amount == __value._water_amount)

    # Getters
    @property
        # Get the amount of fertilizer in the soil
    def fertilizer_amount(self):
        return self._fertilizer_amount
    
    @property
        # Get the amount of water in the soil
    def water_amount(self):
        return self._water_amount
    
    @property
        # Get the price of the soil
    def price(self):
        return self._price

    # Setters
    @fertilizer_amount.setter
    def fertilizer_amount(self, value: int):
        if value < 0:
            raise ValueError("Fertilizer amount cannot be negative")
        elif value > 100:
            self._fertilizer_amount = 100
        else:
            self._fertilizer_amount = value

    @water_amount.setter
    def water_amount(self, value: int):
        if value < 0:
            raise ValueError("Water amount cannot be negative")
        elif value > 100:
            self._water_amount = 100
        else:
            self._water_amount = value

    # Methods
    def is_fertilized(self) -> bool:
        """
        Determines if the soil is fertilized

        Returns:
            bool: True if the soil is fertilized, False otherwise
        """
        return self._fertilizer_amount > 0
    
    def is_watered(self) -> bool:
        """
        Determines if the soil is watered

        Returns:
            bool: True if the soil is watered, False otherwise
        """
        return self._water_amount > 0
    
    def remove_Water(self, amount) -> None:
        """
        Removes water from the soil

        Parameters:
            amount: Amount of water to be removed
        """
        self._water_amount -= amount
        if self._water_amount < 0:
            self._water_amount = 0
    
    def remove_Fertilizer(self, amount) -> None:
        """
        Removes fertilizer from the soil

        Parameters:
            amount: Amount of fertilizer to be removed
        """
        self._fertilizer_amount -= amount
        if self._fertilizer_amount < 0:
            self._fertilizer_amount = 0