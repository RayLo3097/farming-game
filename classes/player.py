from classes.inventory import Inventory

"""
    This class contains all the data and methods related to the player in the game.
    It is used to store the player's name, age, money, and inventory.

    The class has the following methods:
        - __init__: This method is used to initialize the player object. It takes in the name, age, and money as parameters. It initializes the player with the given name, age, and money.
        - getName: This method is used to get the name of the player.
        - getAge: This method is used to get the age of the player.
        - getMoney: This method is used to get the money of the player.
        - setName: This method is used to set the name of the player. It takes in the new name as a parameter. It sets the name of the player to the new name.
        - setAge: This method is used to set the age of the player. It takes in the new age as a parameter. It sets the age of the player to the new age.
        - incMoney: This method is used to increase the money of the player. It takes in the value to increase as a parameter. It increases the money of the player by the given value.
        - decMoney: This method is used to decrease the money of the player. It takes in the value to decrease as a parameter. It decreases the money of the player by the given value.

    The class has the following attributes:
        - name: A string representing the name of the player.
        - age: An integer representing the age of the player.
        - money: A float representing the money of the player.
        - inventory: An Inventory object representing the inventory of the player.

    Created by Tyler Alesse.
    Documented by Prince S.

"""


# Container for all player-related data
# such as inventory, money, etc.
class Player:

    # Attributes

    __name: str
    __maxNameLen: int = 16

    __age: int

    __money: float = 0.00
    inventory: Inventory

    # Class Initialization

    def __init__(self, name: str = "", age: int = 0, money: float = 0.00):
        self.__name = name
        self.__age = age
        self.__money = money

        self.inventory = Inventory()

    # Getters & Setters

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getMoney(self):
        return self.__money

    # Methods

    def setName(self, newName: str):
        """Set the name of the player"""

        if not isinstance(newName, str):
            raise Exception("New Name is not a String")

        nameLen = len(newName)
        if nameLen > self.__maxNameLen:
            raise Exception(f"Name exceeds {self.__maxNameLen} characters")

        self.__name = newName

    def setAge(self, newAge: int):
        """Set the age of the player"""

        if not isinstance(newAge, int):
            raise Exception("New Age is not a Number")

        if 120 < newAge or newAge < 0:
            raise ValueError("New Age is not between 0 and 120 years old")

        self.__age = newAge

    def incMoney(self, value: float):
        """Increase the player's money amount by the given value"""

        if not isinstance(value, float):
            raise Exception("Value is not a Float")

        if value < 0:
            raise ValueError("Cannot increase by a negative value")

        self.__money = self.__money + value

    def decMoney(self, value: float):
        """Decrease the player's money amount by the given value"""

        if not isinstance(value, float):
            raise Exception("Value is not a Float")

        if value < 0:
            raise ValueError("Cannot decrease by a negative value")

        if value > self.__money:
            # raise ValueError('Decrease in Value cannot exceed current value')
            pass

        self.__money = self.__money - value
