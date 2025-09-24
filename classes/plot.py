import pygame
from classes.soil import Soil
from classes.seed import Seed
from classes.item import Items

'''
This is an essential class for the functionality of the planting system in the game.
It is used to create a plot object that can be used to plant seeds, water the soil, and harvest crops.

The class has the following methods:
    - __init__: This method is used to initialize the plot object. It takes in the soil and seed objects as parameters. It initializes the plot with the given soil and seed.
    - __eq__: This method is used to compare the plot object with another object to check if they are equal.
    - plant_seed: This method is used to plant a seed in the plot. It takes in the seed object as a parameter. It plants the given seed in the plot.
    - remove_seed: This method is used to remove the seed from the plot. It removes the seed from the plot.
    - water_plot: This method is used to water the plot. It takes in the water amount as a parameter. It waters the soil in the plot with the given amount of water.
    - add_fertilizer: This method is used to add fertilizer to the plot. It takes in the fertilizer amount as a parameter. It adds the given amount of fertilizer to the soil in the plot.
    - harvest: This method is used to harvest the crop from the plot. It returns the name of the crop that was harvested.


The class has the following attributes:
    - soil: A Soil object representing the soil in the plot.
    - seed: A Seed object representing the seed planted in the plot.
    - price: An integer representing the price of the plot.

Created by Raymond Lo.
Documented by Prince S.

'''
crop_image_path = {
    "blueberry": "assets/itemImages/blueberries.png",
    "corn": "assets/itemImages/corn.png",
    "potato": "assets/itemImages/potato.png",
    "watermelon": "assets/itemImages/watermelon.png",
    "raspberry": "assets/itemImages/raspberries.png"
}

class Plot:
    def __init__(self, soil: Soil = None, seed: Seed = None):
        self.soil = soil
        self.seed = seed
        self._price = 0


    def __eq__(self, __other: object) -> bool:
        if not isinstance(__other, Plot):
            return False
        return (self._soil == __other._soil 
                and self._seed == __other._seed)

    # Getters
    @property
    def soil(self) -> Soil:
        return self._soil

    @property
    def seed(self) -> Seed:
        return self._seed

    @property
    def price(self) -> int:
        return self._price

    
    # Setters
    @soil.setter
    def soil(self, soil: Soil) -> None:
        if soil == None:
            self._soil = None
            return
        if isinstance(soil, Soil) == False:
            raise ValueError("The given soil is not a Soil object")
        self._soil = soil

    @seed.setter
    def seed(self, seed: Seed) -> None:
        if seed == None:
            self._seed = None
            return
        if isinstance(seed, Seed) == False:
            raise ValueError("The given seed is not a Seed object")
        self._seed = seed

    def plant_seed(self, seed: Seed) -> None:
        """
        Plant a seed in the plot
        
        Parameters:
            seed: Seed object to be planted
        """
        if isinstance(seed, Seed) == False:
            raise ValueError("The given seed is not a Seed object")
        if self._seed is not None:
            raise ValueError("Plot already has a seed planted")
        self._seed = seed

    def remove_seed(self) -> None:
        """Removes seed from the plot"""
        self._seed = None

    def water_plot(self, water_amount: int) -> None:
        """
        Waters the plot with the given amount of water

        Parameters:
            water_amount: Amount of water to be added to the soil   
        """
        if self._soil is None:
            raise ValueError("Plot has no soil")
        if water_amount < 0:
            raise ValueError("Water amount cannot be negative")
        self._soil.water_amount += water_amount
    
    def add_fertilizer(self, fertilizer_amount: int) -> None:
        """
        Adds fertilizer to the plot with the given amount

        Parameters:
            fertilizer_amount: Amount of fertilizer to be added to the soil
        """
        if self._soil is None:
            raise ValueError("Plot has no soil")
        if fertilizer_amount < 0:
            raise ValueError("Fertilizer amount cannot be negative")
        self._soil.fertilizer_amount += fertilizer_amount

    def harvest(self):
        """
        Harvest the grown crop from the plot
        """
        if self._seed is None: # No seed planted cannot harvest
            return None 
        crop_name = self._seed.crop_name
        sell_price_formula = self._seed.price * 2.5 
        self._seed = None
        crop_item = Items(crop_name, 0, sell_price_formula, 1, crop_name + " crop", crop_image_path[crop_name], None) # Create crop item
        return crop_item

        
