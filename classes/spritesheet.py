import pygame
'''
This class is used for the movement of the player's animation.

Class Attributes:
    - sheet: A surface object representing the sprite sheet.


Class Methods:
    - walk_left: This method is used to get the left walking animation of the player. It takes in the frame, width, and height as parameters. It returns the left walking animation of the player.
    - walk_up: This method is used to get the up walking animation of the player. It takes in the frame, width, and height as parameters. It returns the up walking animation of the player.
    - walk_down: This method is used to get the down walking animation of the player. It takes in the frame, width, and height as parameters. It returns the down walking animation of the player.
    - walk_right: This method is used to get the right walking animation of the player. It takes in the frame, width, and height as parameters. It returns the right walking animation of the player.
    - idle: This method is used to get the idle animation of the player. It takes in the frame, width, and height as parameters. It returns the idle animation of the player.

    Created by Prince S.
    Documented by Prince S.

'''


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def walk_left(self, frame, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.blit(self.sheet, (0, 0), ((width * 2), frame * height, width, height))
        image = pygame.transform.scale(image, (width * 3.5, height * 3.5))
        image.set_colorkey((0, 0, 0))
        return image

    def walk_up(self, frame, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.blit(self.sheet, (0, 0), ((width * 1), frame * height, width, height))
        image = pygame.transform.scale(image, (width * 3.5, height * 3.5))
        image.set_colorkey((0, 0, 0))
        return image

    def walk_down(self, frame, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.blit(self.sheet, (0, 0), ((width * 0), frame * height, width, height))
        image = pygame.transform.scale(image, (width * 3.5, height * 3.5))
        image.set_colorkey((0, 0, 0))
        return image

    def walk_right(self, frame, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.blit(self.sheet, (0, 0), ((width * 3), frame * height, width, height))
        image = pygame.transform.scale(image, (width * 3.5, height * 3.5))
        image.set_colorkey((0, 0, 0))
        return image

    def idle(self, frame, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.blit(self.sheet, (0, 0), (0, frame * height, width, height))
        image = pygame.transform.scale(image, (width * 3.5, height * 3.5))
        image.set_colorkey((0, 0, 0))
        return image
