# Seed class should inherit from item class

"""
Seed class:

Attributes:
    - crop_name: str        name of the crop that the seed will grow into
    - price: int            price at which the seed is bought by the game
    - sellPrice: int        price at which the seed is sold to the player
    - growth_time: int      time in minutes
    - min_temperature: int  minimum temperature required for the seed to grow in Fahrenheit
    - max_temperature: int  maximum temperature required for the seed to grow in Fahrenheit

Methods:
    - meet_temp_requirements(temperature: int) -> bool
    - __eq__(value: object) -> bool


What does this class do?
    - The Seed class represents a seed that can be planted in a plot. 
    It has attributes such as crop name, price, growth time, and temperature requirements. 
    It also has a method to check if the seed's temperature requirements are met.

    Created by Raymond Lo.
    Documented by Prince S.

"""


class Seed:
    def __init__(
        self,
        seed_name: str = "N/A",
        crop_name: str = "N/A",
        price: int = 0,
        sellPrice: float = 0,
        growth_time: int = 0,
        min_temperature: int = 0,
        max_temperature: int = 0,
    ):
        self._seed_name = seed_name
        self._crop_name = crop_name
        self._price = price
        self._sellPrice = sellPrice
        self._growth_time = growth_time
        self._min_temperature = min_temperature
        self._max_temperature = max_temperature

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Seed):
            return False
        return (
            self._crop_name == __value._crop_name
            and self._price == __value._price
            and self._sellPrice == __value._sellPrice
            and self._growth_time == __value._growth_time
            and self._min_temperature == __value._min_temperature
            and self._max_temperature == __value._max_temperature
        )

    # Getters
    @property
    def seed_name(self):
        return self._seed_name

    @property
    def crop_name(self):
        return self._crop_name

    @property
    def price(self):
        return self._price

    @property
    def sellPrice(self):
        return self._sellPrice

    @property
    def growth_time(self):
        return self._growth_time

    @property
    def min_temperature(self):
        return self._min_temperature

    @property
    def max_temperature(self):
        return self._max_temperature

    # Setters
    @seed_name.setter
    def seed_name(self, name):
        if name == "":
            raise ValueError("Seed name cannot be empty")
        self._seed_name = name

    @crop_name.setter
    def crop_name(self, name):
        if name == "":
            raise ValueError("Crop name cannot be empty")
        self._crop_name = name

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @growth_time.setter
    def growth_time(self, time):
        if time < 0:
            raise ValueError("Growth time cannot be negative")
        self._growth_time = time

    @min_temperature.setter
    def temperature(self, temperature):
        self._min_temperature = temperature

    # Methods
    def meet_temp_requirements(self, temperature):
        """
        Check if given temperature meets the seed's temperature requirements

        Parameters:
            temperature (int): Temperature to be checked

        Returns:
            bool: True if the temperature meets the requirements, False otherwise
        """
        return self._min_temperature <= temperature <= self._max_temperature
