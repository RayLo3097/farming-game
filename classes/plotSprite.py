import pygame
from classes.plot import Plot
from classes.inventory import Inventory
from classes.item import Items
from classes.Time import shared_time as Time

'''
This class is used to create a sprite for each plot on the farm. 
It is used to display the plot on the screen and to handle the user's interaction with the plot.
This is a very crucial class for the game, created by Raymond.

The class has the following methods:
    - __init__: This method is used to initialize the plot sprite. It takes in the name of the plot, the x and y coordinates of the plot, and the plot object as parameters. It initializes the plot sprite with the given parameters.
    - create_hover_text: This method is used to create a tooltip for the plot information. It takes in the screen, event, and hover as parameters. It creates a tooltip with information about the plot's water and fertilizer levels.
    - update: This method is used to update the plot sprite. It takes in the event, player_inventory, and screen as parameters. It updates the plot sprite based on the user's interaction with the plot.

The class has the following attributes:
    - name: A string representing the name of the plot.
    - x_coord: An integer representing the x coordinate of the plot.
    - y_coord: An integer representing the y coordinate of the plot.
    - sprites: A list of images representing the different states of the plot (with and without soil).
    - current_sprite: An integer representing the index of the current sprite in the sprites list.
    - image: An image representing the current state of the plot.
    - rect: A rectangle representing the position and size of the plot sprite.
    - isHovering: A boolean representing whether the mouse is hovering over the plot sprite.
    - mousePos: A tuple representing the position of the mouse.
    - _plot: A Plot object representing the plot associated with the plot sprite.

The class currently has the following functionality:
    - The ability to create a tooltip for the plot information.
    - The ability to water the plot by clicking on it.
    - The ability to update the plot sprite based on the user's interaction with the plot.

The class will have the following functionality in the future:
    - The ability to fertilize the plot.
    - The ability to plant seeds in the plot.
    - The ability to harvest crops from the plot.
    - The ability to display the crop's growth stage on the plot sprite.
    - The ability to display the time remaining for the crop to be ready for harvest.
    - The ability to display the crop's name on the plot sprite.
    - The ability to display the plot's water and fertilizer levels on the plot sprite.

    ~~ Class documentation by Prince S.
'''

plot_image = pygame.image.load("assets/nosoilplot.png")

plot_size = 200

plot_image = pygame.transform.scale(plot_image, (plot_size, plot_size))

watered_plot_image = pygame.image.load("assets/plot.png")
watered_plot_image = pygame.transform.scale(watered_plot_image, (plot_size, plot_size))

unwatered_fertilized_image = pygame.image.load("assets/fertilizer_unwatered.png")
unwatered_fertilized_image = pygame.transform.scale(unwatered_fertilized_image, (plot_size, plot_size))

watered_fertilized_image = pygame.image.load("assets/fertilizer_watered.png")
watered_fertilized_image = pygame.transform.scale(watered_fertilized_image, (plot_size, plot_size))

planted_blueberry_image = pygame.image.load("assets/blueberry_seeds_plot.png")
planted_blueberry_image = pygame.transform.scale(planted_blueberry_image, (plot_size, plot_size))

planted_corn_image = pygame.image.load("assets/corn_seeds_plot.png")
planted_corn_image = pygame.transform.scale(planted_corn_image, (plot_size, plot_size))

planted_hemp_image = pygame.image.load("assets/hemp_seeds_plot.png")
planted_hemp_image = pygame.transform.scale(planted_hemp_image, (plot_size, plot_size))

planted_potato_image = pygame.image.load("assets/potato_seeds_plot.png")
planted_potato_image = pygame.transform.scale(planted_potato_image, (plot_size, plot_size))

planted_raspberry_image = pygame.image.load("assets/raspberry_seeds_plot.png")
planted_raspberry_image = pygame.transform.scale(planted_raspberry_image, (plot_size, plot_size))

seed_dictionary = {
    "blueberry seeds": planted_blueberry_image,
    "corn seeds": planted_corn_image,
    "watermelon seeds": planted_hemp_image,
    "potato seeds": planted_potato_image,
    "raspberry seeds": planted_raspberry_image
}

debug = True


# Class for the plot sprite
class PlotSprite(pygame.sprite.Sprite):
    def __init__(self, name: str, x_coord: int, y_coord: int, plot: Plot) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.readytoharvest = False

        self.plantedTime = 0
        self.soil_degrade_time = 0
        self.ferilizer_degrade_time = 0
        self.grow_time = 0

        self.image = plot_image

        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord)
        self.isHovering = False

        self.mousePos = pygame.mouse.get_pos()
        self._plot = plot

    @property
    def plot(self):
        return self._plot
    
    def plotDegradation(self):
        if self._plot.seed is not None and self.readytoharvest == False:
            if (Time.delay_condition(self.soil_degrade_time, 5) == True):
                if self._plot.soil.water_amount > 0:
                    self._plot.soil.water_amount -= 1
                self.soil_degrade_time = Time.get_time()
            if (Time.delay_condition(self.ferilizer_degrade_time, 10) == True):
                if self._plot.soil.fertilizer_amount > 0:
                    self._plot.soil.fertilizer_amount -= 1
                self.ferilizer_degrade_time = Time.get_time()
            

    def isPlayerNear(self, playerX, playerY):
        return (playerX >= self.x_coord - 100 and playerX <= self.x_coord + 70) and (playerY >= self.y_coord - 150 and playerY <= self.y_coord + 80)
    
    # Draw a alert message when the plot is ready to harvest and it goes away when player is near the plot
    def draw_harvest_alert(self, screen, playerX, playerY):
        if self.readytoharvest == True:
            if not self.isPlayerNear(playerX, playerY):
                harvest_text = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 30).render(
                    f"Ready to harvest", True, (255, 255, 255)
                )
                # Floating effect for the alert
                screen.blit(harvest_text, (self.x_coord - 70, self.y_coord - 150))

    def draw_harvest_directions(self, screen, playerX, playerY):
        # Draw the harvest directions for the plot
        if self.readytoharvest == True:
            # When player is near the plot
            if (playerX >= self.x_coord - 100 and playerX <= self.x_coord + 70) and (playerY >= self.y_coord - 150 and playerY <= self.y_coord + 80):
                harvest_text = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 30).render(
                    f"Press 'H' to harvest", True, (255, 255, 255)
                )
                screen.blit(harvest_text, (self.x_coord - 70, self.y_coord - 150))

    # Draw the progress bar for the plot to show how long until the crop is ready
    def draw_progress_bar(self, screen):
        # Get the time when the seed was planted
        if self._plot.seed is not None and self.readytoharvest == False:
            # Get the current time
            currentTime = Time.get_time()
            # Calculate the time that has passed since the seed was planted
            timePassed = Time.time_elapsed(self.plantedTime, currentTime)     

            # Depending on how much fertilizer is in the soil, the crop will grow faster
            

            
            timeLeft = (self.grow_time) - timePassed
            
            if timeLeft < 0:
                timeLeft = 0

            progress = (timePassed / (self.grow_time)) * 100

            # Draw the progress bar
            pygame.draw.rect(screen, (255, 255, 255), (self.x_coord - 50, self.y_coord - 50, 100, 10))

            if timeLeft > 0:
                pygame.draw.rect(screen, (0, 255, 0), (self.x_coord - 50, self.y_coord - 50, progress, 10))
            else:
                self.readytoharvest = True
                pygame.draw.rect(screen, (0, 255, 0), (self.x_coord - 50, self.y_coord - 50, 100, 10))
            # Draw the progress bar
        
    # This method is used to create a tooltip for the plot information
    def create_hover_text(self, screen, event, hover):
        # Create ToolTip for plot information

        if not self.readytoharvest and screen is not None:
            textbg = pygame.Surface((110, 35))
            textbg.fill((51, 51, 51))
            textbg.set_alpha(100)
            screen.blit(textbg, (self.x_coord - 52, self.y_coord - 150))

            # If plot has a seed planted
            if self._plot.seed is not None:
                timetextbg = pygame.Surface((110, 110))
                timetextbg.fill((51, 51, 51))
                timetextbg.set_alpha(100)
                screen.blit(timetextbg, (self.x_coord + 90, self.y_coord - 75))

            if (self._plot.soil.water_amount < 25):
                color_water = (224, 54, 71)
            elif (self._plot.soil.water_amount >= 25 and self._plot.soil.water_amount < 50):
                color_water = (224, 136, 54)
            elif (self._plot.soil.water_amount >= 50 and self._plot.soil.water_amount < 75):
                color_water = (176, 224, 54)
            elif (self._plot.soil.water_amount >= 75 and self._plot.soil.water_amount <= 90):
                color_water = (54, 224, 54)
            else:
                color_water = (255, 255, 255)
            #---
            # Controls color of fertilizer text
            if (self._plot.soil.fertilizer_amount < 25):
                color_fertilizer = (224, 54, 71)
            elif (self._plot.soil.fertilizer_amount >= 25 and self._plot.soil.fertilizer_amount < 50):
                color_fertilizer = (224, 136, 54)
            elif (self._plot.soil.fertilizer_amount >= 50 and self._plot.soil.fertilizer_amount < 75):
                color_fertilizer = (176, 224, 54)
            elif (self._plot.soil.fertilizer_amount >= 75 and self._plot.soil.fertilizer_amount <= 90):
                color_fertilizer = (54, 224, 54)
            else:
                color_fertilizer = (255, 255, 255)

            text = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 11).render(
                f"Fertilizer: {self._plot.soil.fertilizer_amount}", True, color_fertilizer
            )
            screen.blit(text, (self.x_coord - 47, self.y_coord - 133))
            water_text = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 11).render(
                f"Water: {self._plot.soil.water_amount}", True, color_water
            )
            screen.blit(water_text, (self.x_coord - 47, self.y_coord - 148))
            
            if self._plot.seed is not None:
                # Print amount of time that has passed since the seed was planted
                timePassed = Time.time_elapsed(self.plantedTime, Time.get_time())

                timeLeft = self.grow_time - timePassed
                timeLeft = round(timeLeft, 2)
                if timeLeft < 0:
                    timeLeft = 0


            if self._plot.seed is not None:
                timetext = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 8).render(
                    f"Growth Time: {self.grow_time}", True, (255, 255, 255)
                )

                # Round the time left to whole numbers
                timeLeftTillHarvest = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 8).render(
                    f"Time Left: {timeLeft}", True, (255, 255, 255)
                )

                croptext = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 8).render(
                    f"Crop: {self.plot.seed.crop_name}", True, (255, 255, 255)
                    # f"Crop: ", True, (255, 255, 255)
                )

                screen.blit(croptext, (self.x_coord + 95, self.y_coord - 65))
                screen.blit(timetext, (self.x_coord + 95, self.y_coord - 45))
                screen.blit(timeLeftTillHarvest, (self.x_coord + 95, self.y_coord - 30))

    # This method is used to update the plot sprite
    def update(self, event=None, player_inventory: Inventory = None, screen=None):
        """
        Updates the plot sprite based on the user's interaction with the plot

        Parameters:
            event: The player's interaction with the plot
            player_inventory: The player's inventory
            screen: The game screen
        """
        hit = self.rect.collidepoint(pygame.mouse.get_pos()) # Check if the mouse is hovering over the plot

        if hit and not self.readytoharvest: # If the mouse is hovering over the plot display the hover text
            if self.isHovering == False:
                self.create_hover_text(screen, event, True)

        if event is not None:
            current_hand_item: Items = None
            # If the plot is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                if player_inventory == None: #Player has no inventory
                    pass
                elif player_inventory.get_handContents() == {}: #Player has no item in hand
                    pass
                else: #Player has an item in hand and is clicking on a plot
                    current_key = list(player_inventory.get_handContents().keys())[0]
                    current_hand_item = player_inventory.get_handContents()[current_key]
                    if (current_hand_item.get_name() == "water"): #Player has water in hand
                        if (self._plot.soil.water_amount < 100): #If the plot is not fully watered then water the plot
                            self._plot.water_plot(25) #Water the plot
                    
                            if (current_hand_item.quantity == 1): 
                                player_inventory.remove_handitem(current_hand_item)

                            for key, item in player_inventory.get_contents().items():
                                if key == "water":
                                    player_inventory.rem_item(item)
                                    break
                        elif(debug == True):
                            print(f"{self.name} is already watered. Cannot water it again.")
                        
                    elif (current_hand_item.get_name() == "fertilizer"):
                        if (self._plot.soil.fertilizer_amount < 100): #If the plot is not fully fertilized then fertilize the plot
                            self._plot.add_fertilizer(25) #Fertilize the plot
                            if (current_hand_item.quantity == 1): 
                                player_inventory.remove_handitem(current_hand_item)

                            for key, item in player_inventory.get_contents().items():
                                if key == "fertilizer":
                                    player_inventory.rem_item(item)
                                    break
                        elif(debug == True):
                            print(f"{self.name} is already fertilized. Cannot fertilize it again.")

                    elif ("seeds" in current_hand_item.get_name()):
                        if current_hand_item.seed is None: #If item doesn't have a seed then raise an error
                            raise ValueError(f"Tried to plant seed but there was no seed in the item. Item name: {current_hand_item.get_name()}")
                        
                        if self.plot.soil.fertilizer_amount > 1 and self.plot.soil.water_amount > 1: #If the plot is fertilized and watered
                            if self.plot.seed is None: #If the plot has no seed planted
                                self.plot.plant_seed(current_hand_item.seed)
                                
                                # Calculate the time it takes for the seed to grow
                                self.grow_time = self._plot.seed.growth_time * 60
                                if self._plot.soil.fertilizer_amount == 100:
                                    self.grow_time = round(self.grow_time / 2.5)
                                elif self._plot.soil.fertilizer_amount >= 75:
                                    self.grow_time = round(self.grow_time / 2)
                                elif self._plot.soil.fertilizer_amount >= 50:
                                    self.grow_time = round(self.grow_time / 1.5)

                                self.plantedTime = Time.get_time() # Get the time when the seed was planted
                                self.soil_degrade_time = Time.get_time() #Prepare the time for soil degradation
                                self.ferilizer_degrade_time = Time.get_time() #Prepare the time for fertilizer degradation
                                self.image = seed_dictionary[current_hand_item.get_name()]  # Change the plot image to the seed image
                                player_inventory.remove_handitem(current_hand_item) #Remove the seed from the player's inventory
                            
                                for key in player_inventory.get_contents(): #Remove the seed from the player's inventory
                                    if key == current_hand_item.get_name():
                                        player_inventory.rem_item(player_inventory.get_contents().get(key))
                                        break

                if debug == True and self.plot.seed is not None:
                   print(f"{self.name} has been clicked at {event.pos}. It's coords are ({self.x_coord}, {self.y_coord}) and seed: {self.plot.seed.seed_name},{self.plot.seed.crop_name}.")
        
        if self.plot.seed is None:
            if self.plot.soil.is_watered() and self.plot.soil.is_fertilized(): #If the plot is watered and fertilized
                self.image = watered_fertilized_image
                # Update the hover text with crop information

            elif self.plot.soil.is_watered() and not self.plot.soil.is_fertilized(): #If the plot is watered but not fertilized
                self.image = watered_plot_image
            elif not self.plot.soil.is_watered() and self.plot.soil.is_fertilized(): #If the plot is fertilized but not watered
                self.image = unwatered_fertilized_image
            else: #If the plot is neither watered nor fertilized
                self.image = plot_image 

