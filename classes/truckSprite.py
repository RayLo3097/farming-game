import pygame
from classes.inventory import Inventory
from classes.item import Items
from classes.amarket import Market
from datetime import datetime


truck_image = pygame.image.load("assets/truck.png")
truck_image = pygame.transform.scale(truck_image, (200 * 1.5, 85 * 1.5))


class TruckSprite(pygame.sprite.Sprite):

    def __init__(
        self,
        x,
        y,
        market: Market,
        inventory: Inventory,
        screen=None,
        player_x=0,
        player_y=0,
    ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = truck_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.market = market
        self.inventory = inventory
        self.screen = screen
        self.player_x = player_x
        self.player_y = player_y

        self.bop_start_time = 0  # Initialize the start time for bopping
        self.bop_duration = 500  # Duration of each bop animation in milliseconds

    # draw the truck
    def draw(self):
        self.screen.blit(self.image, self.rect)

    # give truck bopping animation
    def bop(self):
        self.rect.y += 5
        self.draw()
        self.rect.y -= 10
        import pygame


from classes.inventory import Inventory
from classes.item import Items
from classes.amarket import Market


truck_image = pygame.image.load("assets/truck.png")
truck_image = pygame.transform.scale(truck_image, (200, 85))


class TruckSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, market: Market, inventory: Inventory, screen=None) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = truck_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.market = market
        self.inventory = inventory
        self.screen = screen

        self.last_bop_time = 0  # Initialize the time of the last bop
        self.bop_interval = 50  # Time interval between each bop in milliseconds

        self.allowSell = False

    # draw the truck
    def draw(self):
        self.screen.blit(self.image, self.rect)

    # give truck bopping animation
    # with a delay but no blocking call
    def bop(self):
        current_time = pygame.time.get_ticks()
        self.draw()
        if current_time - self.last_bop_time > self.bop_interval:
            # If enough time has passed since the last bop, bop again

            self.rect.y -= 2  # Move the truck up
            # pygame.time.delay(50)  # Short delay to hold the position briefly
            self.draw()
            self.rect.y += 2  # Move the truck back down
            self.last_bop_time = current_time  # Update the time of the last bop

    def isThereAnItemToSell(self):
        # get first key in handContents
        if len(self.inventory.get_handContents()) > 0:
            return True
        else:
            return False

    def getItemToSell(self):
        if len(self.inventory.get_handContents()) > 0:
            key = list(self.inventory.get_handContents().keys())[0]
            item = self.inventory.get_handContents().get(key)
            return item

    # draw sell meny if player is in range
    def draw_sell_menu(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Press 'E' to sell", True, (255, 255, 255))
        self.screen.blit(text, (self.rect.x - 50, self.rect.y - 20))

    def check_range (self, player_x, player_y):
        if (player_x > self.rect.x - 50 and player_x < self.rect.x + 50 and player_y > self.rect.y - 50 and player_y < self.rect.y + 50):
            return True
        else:
            return False
        
    def draw_hint_text(self):
        font = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 36)
        text = font.render("SOLD!", True, (255, 255, 255))
        self.screen.blit(text, (500,350))
    # check if player is in truck's range
    def check_player(self, player_x, player_y):
        if (
            player_x > self.rect.x - 50
            and player_x < self.rect.x + 50
            and player_y > self.rect.y - 50
            and player_y < self.rect.y + 50
        ):
            if self.isThereAnItemToSell():
                self.draw_sell_menu()
                self.getItemToSell()
                self.allowSell = True
                # show hint text until player is out of range
                # if self.check_range(player_x, player_y):
                #     self.draw_hint_text()
        else:
            self.allowSell = False
            pass
