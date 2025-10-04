############################################
import pygame, time, os
from classes.spritesheet import SpriteSheet
from classes.plotSprite import PlotSprite
from classes.truckSprite import TruckSprite

from classes.UIClasses.button import Button

from classes.player import Player
from classes.inventory import Inventory
from classes.item import Items

from classes.amarket import Market

from classes.seed import Seed
from classes.soil import Soil
from classes.plot import Plot

from classes.hint import Hint


pygame.init()
# Set it to borderless fullscreen
SCREEN = pygame.display.set_mode((0, 0), pygame.NOFRAME)
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()

# TEST_MODE  = 0 # 1 for testing, 0 for production



# SCREEN = pygame.display.set_mode((1, 1080))  # Screen size in (px, px)

sprite_walk = pygame.image.load("assets/OldMan/SeparateAnim/Walk.png").convert_alpha()
sprite_idle = pygame.image.load("assets/OldMan/SeparateAnim/Idle.png").convert_alpha()

sprite_sheet_walk = SpriteSheet(sprite_walk)
sprite_sheet_idle = SpriteSheet(sprite_idle)

pressedPlay = False
pressedHelp = False
pressedCredits = False

pressedControls = False
pressedFarming = False
pressedCrops = False


def generate_plots(coords_list: list):
    plot_sprites_list = []
    for coords in range(0, 6):
        plot = Plot(Soil())
        plot_sprite = PlotSprite(
            f"plot {coords + 1}", coords_list[coords][0], coords_list[coords][1], plot
        )
        plot_sprites_list.append(plot_sprite)
    return plot_sprites_list

hintText = ""
current_time = None

def playHintText(text: str, x: int, y: int, timelasting: int):
    global hintText, current_time
    
    # Display hint text
    hintText = text
    current_time = time.time()

    font = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 30)
    hint = font.render(hintText, True, (255, 255, 255))
    SCREEN.blit(hint, (x, y))


    # Check if the hint should still be displayed

# load startScreenImage
startScreenImage = pygame.image.load("assets/startScreenImage.png").convert_alpha()
scaled_startScreenImage = pygame.transform.scale(startScreenImage, (SCREEN_WIDTH, SCREEN_HEIGHT))


howToPlayScreen = pygame.image.load("assets/howToPlayScreen2.png").convert_alpha()
scaled_howToPlayScreen = pygame.transform.scale(howToPlayScreen, (SCREEN_WIDTH, SCREEN_HEIGHT))

creditsScreen = pygame.image.load("assets/CreditsScreen.png").convert_alpha()
scaled_creditsScreen = pygame.transform.scale(creditsScreen, (SCREEN_WIDTH, SCREEN_HEIGHT))

# load play button image
playButtonImage = pygame.image.load("assets/playbutton.png").convert_alpha()
# load how to play button image
howToPlayButtonImage = pygame.image.load("assets/howtoplaybutton.png").convert_alpha()
# load credits button image
creditsButtonImage = pygame.image.load("assets/CreditsButton.png").convert_alpha()




# help screen controls button
controlsButtonImage = pygame.image.load("assets/ControlsHelpButton.png").convert_alpha()
# help screen crops button
cropsButtonImage = pygame.image.load("assets/CropHelpButton.png").convert_alpha()
# help screen economy button
farmingButtonImage = pygame.image.load("assets/FarmingHelpButton.png").convert_alpha()

# help control screen
controlScreen = pygame.image.load("assets/ControlsScreen.png").convert_alpha()
scaled_controlScreen = pygame.transform.scale(controlScreen, (SCREEN_WIDTH, SCREEN_HEIGHT))

# help crops screen
cropsScreen = pygame.image.load("assets/CropScreen.png").convert_alpha()
scaled_cropsScreen = pygame.transform.scale(cropsScreen, (SCREEN_WIDTH, SCREEN_HEIGHT))

# help farming screen
farmingScreen = pygame.image.load("assets/FarmingScreen.png").convert_alpha()
scaled_farmingScreen = pygame.transform.scale(farmingScreen, (SCREEN_WIDTH, SCREEN_HEIGHT))



# help screen back button
backButtonImage = pygame.image.load("assets/HelpBackButton.png").convert_alpha()



# Will be used to draw the start screen
def draw_controls_help_screen():
    SCREEN.blit(scaled_controlScreen, (0, 0))
    global pressedHelp
    global pressedControls


    backButton = Button(50, 30, backButtonImage, 0.45, "Back")
    backButton.draw(SCREEN)
    pressedHelp = False
    if backButton.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedHelp = True
            pressedControls = False

def draw_crops_help_screen():
    SCREEN.blit(scaled_cropsScreen, (0, 0))
    global pressedHelp
    global pressedCrops
    backButton = Button(50, 30, backButtonImage, 0.45, "Back")
    backButton.draw(SCREEN)
    pressedHelp = False
    if backButton.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedHelp = True
            pressedCrops = False

def draw_credits_screen():
    # Create Buttons
    global pressedPlay
    global pressedHelp
    global pressedCredits

    SCREEN.blit(scaled_creditsScreen, (0, 0))
    backButton = Button(50, 30, backButtonImage, 0.45, "Back")
    backButton.draw(SCREEN)
    pressedHelp = False
    pressedPlay = False
    if backButton.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedPlay = False
            pressedHelp = False
            pressedCredits = False

def draw_farming_help_screen():
    SCREEN.blit(scaled_farmingScreen, (0, 0))
    global pressedHelp
    global pressedFarming
    backButton = Button(50, 30, backButtonImage, 0.45, "Back")
    backButton.draw(SCREEN)
    pressedHelp = False
    if backButton.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedHelp = True
            pressedFarming = False



def draw_helpScreen():
    # Create Buttons
    global pressedPlay
    global pressedHelp
    global pressedCredits
    
    global pressedControls
    global pressedFarming
    global pressedCrops



    SCREEN.blit(scaled_howToPlayScreen, (0, 0))
    controls_button = Button(SCREEN_WIDTH // 2 - controlsButtonImage.get_width() * 0.45 // 2, SCREEN_HEIGHT // 2.5, controlsButtonImage, 0.45, "Controls")
    crops_button = Button(SCREEN_WIDTH // 2 - cropsButtonImage.get_width() * 0.45 // 2 - 250, SCREEN_HEIGHT // 2.5, cropsButtonImage, 0.45, "Crops")
    farming_button = Button(SCREEN_WIDTH // 2 - farmingButtonImage.get_width() * 0.45 // 2 + 250, SCREEN_HEIGHT // 2.5, farmingButtonImage, 0.45, "Economy")
    backButton = Button(SCREEN_WIDTH // 2 - backButtonImage.get_width() * 0.45 // 2, SCREEN_HEIGHT // 2.5 + 400, backButtonImage, 0.45, "Back")
    # Draw Buttons

    controls_button.draw(SCREEN)
    crops_button.draw(SCREEN)
    farming_button.draw(SCREEN)
    backButton.draw(SCREEN)

    if backButton.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedHelp = False
            pressedPlay = False
    if controls_button.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedHelp = False
            pressedControls = True
    if crops_button.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedHelp = False 
            if pressedHelp == False:
                pressedCrops = True
            # pressedCrops = True
    if farming_button.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pressedHelp = False
            pressedFarming = True

def draw_startScreen():
    # Draw the scaled start screen image
    SCREEN.blit(scaled_startScreenImage, (0, 0))

    # Calculate the center of the screen
    center_x = SCREEN_WIDTH // 2

    # Define the vertical starting point for the buttons further down
    start_y = SCREEN_HEIGHT // 2.5

    gap = 100  # Vertical gap between buttons

    # Draw the buttons
    play_button = Button(center_x - playButtonImage.get_width() * 0.45 // 2, start_y, playButtonImage, 0.45, "Play")
    play_button.draw(SCREEN)

    how_to_play_button = Button(center_x - howToPlayButtonImage.get_width() * 0.45 // 2, start_y + gap, howToPlayButtonImage, 0.45, "How to Play")
    how_to_play_button.draw(SCREEN)

    credits_button = Button(center_x - creditsButtonImage.get_width() * 0.45 // 2, start_y + gap * 2, creditsButtonImage, 0.45, "Credits")
    credits_button.draw(SCREEN)

    # if play button is clicked, set pressedP   lay to True
    if play_button.check_for_input(pygame.mouse.get_pos()):
        global pressedPlay
        global pressedHelp
        global pressedCredits

        global pressedControls
        global pressedFarming
        global pressedCrops

        if pygame.mouse.get_pressed()[0]:
            pressedPlay = True
            print("Play button clicked")
            play_button.clicked = False
    if how_to_play_button.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            print("How to play button clicked")
            how_to_play_button.clicked = False
            pressedPlay = True
            pressedHelp = True

    if credits_button.check_for_input(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            print("Credits button clicked")
            credits_button.clicked = False
            pressedPlay = True
            pressedHelp = False
            pressedCredits = True

def open_market(market, market_slots, player=None):
    # Draw grey slots

    SLOT_SIZE = 75
    for slot_pos in market_slots:
        slot_surface = pygame.Surface((SLOT_SIZE, SLOT_SIZE))
        slot_surface.fill((200, 200, 200))
        slot_surface.set_alpha(128)
        SCREEN.blit(slot_surface, (slot_pos[0] - 85, slot_pos[1] + 85))
    # Draw a border on the slots
    for slot_pos in market_slots:
        pygame.draw.rect(
            SCREEN,
            (0, 0, 0),
            pygame.Rect(slot_pos[0] - 85, slot_pos[1] + 85, SLOT_SIZE, SLOT_SIZE),
            2,
        )

    # Draw items in the slots
    for item in market.getProducts():
        item_image = item.get_image()
        item_image = pygame.transform.scale(item_image, (50, 50))
        # Text for Price
        # If item cost is less than player wallet color is red
        # Else color is green
        canAffordColor = (30, 102, 49)
        cantAffordColor = (102, 30, 34)

        if item.get_price() > market.player.getMoney():
            price_text = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 12).render(
                f"${item.get_price()}", True, cantAffordColor
            )
        else:
            price_text = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 12).render(
                f"${item.get_price()}", True, canAffordColor
            )

        tooltip_text = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 12).render(
            f"{item.get_name()}", True, (255, 255, 255)
        )
        # When mouse is     ing over item, display tooltip for market items
        text_width = tooltip_text.get_width()
        if pygame.Rect(
            market_slots[market.getProducts().index(item)][0] - 85,
            market_slots[market.getProducts().index(item)][1] + 85,
            SLOT_SIZE,
            SLOT_SIZE,
        ).collidepoint(pygame.mouse.get_pos()):
            SCREEN.blit(
                tooltip_text,       
                (
                    # Keep text centered under the slot regardless of the size of the text
                    market_slots[market.getProducts().index(item)][0]
                    - 85
                    + (SLOT_SIZE - text_width) // 2,
                    # market_slots[market.getProducts().index(item)][0] - 85,
                    market_slots[market.getProducts().index(item)][1] + 165,
                ),
            )
        SCREEN.blit(
            item_image,
            (
                market_slots[market.getProducts().index(item)][0] - 75,
                market_slots[market.getProducts().index(item)][1] + 87,
                
            ),
        )
        
        SCREEN.blit(
            price_text,
            (
                market_slots[market.getProducts().index(item)][0] - 67,
                market_slots[market.getProducts().index(item)][1] + 140,
            ),
        )


# load clouds
cloud1 = pygame.image.load("assets/cloud1.png").convert_alpha()
cloud2 = pygame.image.load("assets/cloud2.png").convert_alpha()
cloud3 = pygame.image.load("assets/cloud3.png").convert_alpha()
cloud1 = pygame.transform.scale(cloud1, (100, 100))
cloud2 = pygame.transform.scale(cloud2, (100, 100))
cloud3 = pygame.transform.scale(cloud3, (100, 100))

# make clouds transparent
cloud1.set_alpha(150)
cloud2.set_alpha(150)
cloud3.set_alpha(150)


def draw_clouds():
    # make clouds smaller

    # draw clouds
    relative_positions = [(0.2, 0.01), (0.3, 0.02), (0.7, -0.005), (0.5, 0.01), (0.8, 0.01)]

    for pos in relative_positions:
        x = pos[0] * SCREEN_WIDTH
        y = pos[1] * SCREEN_HEIGHT
        SCREEN.blit(cloud1 if relative_positions.index(pos) % 2 == 0 else cloud2, (x, y))


def open_inventory(inventory, bag_slots, inventoryItems):

    bar_background = pygame.Surface((745, 75))
    bar_background.fill((200, 200, 200))
    bar_background.set_alpha(128)
    SCREEN.blit(bar_background, (SCREEN_WIDTH/4 - 10, SCREEN_HEIGHT - 110))

    for slot_pos in bag_slots:
        slot_surface = pygame.Surface((50, 50))  # Create a new surface for the slot
        # Draw a background bar for the inventory slots
        slot_surface.fill((200, 200, 200))  # Fill the surface with the desired color
        slot_surface.set_alpha(
            128
        )  # Set the alpha value to 128 (out of 255), making the surface semi-transparent
        SCREEN.blit(
            slot_surface, (slot_pos[0], slot_pos[1])
        )  # Draw the surface onto the screen
        # Draw a border on the slots
        pygame.draw.rect(
            SCREEN, (0, 0, 0), pygame.Rect(slot_pos[0], slot_pos[1], 50, 50), 2
        )

    temporary_index = 0
    for key in inventoryItems:
        # put item image on top of slot pos
        # Number each slot for numpad reference
        item = inventoryItems.get(key)
        numberText = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 12).render(
            f"{temporary_index + 1}", True, (255, 255, 255)
        )
        item_image = item.get_image()
        item_image = pygame.transform.scale(item_image, (50, 50))
        quantity_text = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 12).render(
            f"x{item.quantity}", True, (255, 255, 255)
        )
        tooltip_text = pygame.font.Font("assets/fonts/GAMEPLAY.TTF", 12).render(
            f"{item.name}", True, (255, 255, 255)
        )
        # When mouse is hovering over item, display tooltip
        if pygame.Rect(bag_slots[temporary_index][0], bag_slots[temporary_index][1], 50, 50).collidepoint(
            pygame.mouse.get_pos()
        ):
            
            SCREEN.blit(tooltip_text, (bag_slots[temporary_index][0], bag_slots[temporary_index][1] + 55))
        SCREEN.blit(item_image, (bag_slots[temporary_index][0], bag_slots[temporary_index][1]))
        SCREEN.blit(quantity_text, (bag_slots[temporary_index][0] + 35, bag_slots[temporary_index][1] + 35))
        SCREEN.blit(numberText, (bag_slots[temporary_index][0], bag_slots[temporary_index][1] + 35))
        temporary_index += 1


def play():
    # pygame setup
    global pressedPlay
    global pressedHelp
    global pressedCredits

    global pressedControls
    global pressedFarming
    global pressedCrops

    pygame.init()
    clock = pygame.time.Clock()  # Game update clock
    running = True  # Stop Flag
    dt = 0  # delta time, used for framerate
    velocity = 100  # player speed
    farmer = Player()
    market = Market(inventory=farmer.inventory, player=farmer)

    # Get the current weather information
    # Commented out because caused errors. Uncomment when weather is implemented
    # weather = RealWeather()
    # weather.requestWeather() # Sets up weather data in the variable
    # currentWeather = weather.getWeatherNow()
    # isRaining = (currentWeather.rainInches > 0)
    
    """
    INITIALIZE MARKET

    """
    blueberryseed = Seed("blueberry seeds", "blueberry", 250.0, 125.0, 25, 50, 112)
    watermelonseed = Seed("watermelon seeds", "watermelon", 25.0, 13.0, .1, 50, 112)
    cornseed = Seed("corn seeds", "corn", 50.0, 25.0, 5, 50, 112)
    potatoseed = Seed("potato seeds", "potato", 150.0, 75.0, 10, 50, 112)
    raspberryseed = Seed("raspberry seeds", "raspberry", 200.0, 100.0, 15, 50, 112)

    market.addProduct(
        watermelonseed.seed_name,
        watermelonseed.price,
        watermelonseed.sellPrice,
        0,
        "seed",
        "assets/itemImages/watermelonseeds.png",
        watermelonseed,
    )
    market.addProduct(
        cornseed.seed_name,
        cornseed.price,
        cornseed.sellPrice,
        0,
        "seed",
        "assets/itemImages/cornseeds.png",
        cornseed,
    )
    market.addProduct(
        potatoseed.seed_name,
        potatoseed.price,
        potatoseed.sellPrice,
        0,
        "seed",
        "assets/itemImages/potatoseeds.png",
        potatoseed,
    )
    market.addProduct(
        raspberryseed.seed_name,
        raspberryseed.price,
        raspberryseed.sellPrice,
        0,
        "seed",
        "assets/itemImages/raspberryseeds.png",
        raspberryseed,
    )
    market.addProduct(
        blueberryseed.seed_name,
        blueberryseed.price,
        blueberryseed.sellPrice,
        0,
        "seed",
        "assets/itemImages/blueberryseeds.png",
        blueberryseed,
    )

    market.addProduct("water", 15.0, 7.5, 0, "tool", "assets/itemImages/water.png")
    market.addProduct(
        "fertilizer", 20.0, 15.0, 0, "tool", "assets/itemImages/fertilizer.png"
    )

    # LOAD IMAGES:
    hempImage = pygame.image.load("assets/itemImages/watermelonseeds.png").convert_alpha()
    cornImage = pygame.image.load("assets/itemImages/cornseeds.png").convert_alpha()
    potatoImage = pygame.image.load("assets/itemImages/potatoseeds.png").convert_alpha()
    raspberryImage = pygame.image.load(
        "assets/itemImages/raspberryseeds.png"
    ).convert_alpha()
    blueberryImage = pygame.image.load(
        "assets/itemImages/blueberryseeds.png"
    ).convert_alpha()
    # wheatImage = pygame.image.load("assets/itemImages/wheat.png").convert_alpha()
    waterImage = pygame.image.load("assets/itemImages/water.png").convert_alpha()
    fertilizerImage = pygame.image.load(
        "assets/itemImages/fertilizer.png"
    ).convert_alpha()

    # IMAGE DICTIONARY HERE:

    # (image_url : loadedImage)
    # CURRENTLY UNUSED, BUT CAN BE USED TO DYNAMICALLY LOAD IMAGES (if needed)
    image_dict = {
        "watermelon": hempImage,
        "cornseeds": cornImage,
        "potatoseeds": potatoImage,
        "raspberryseeds": raspberryImage,
        "blueberryseeds": blueberryImage,
        # "wheat": wheatImage,
        "water": waterImage,
        "fertilizer": fertilizerImage,
    }

    #     market -> item -> inventory.item -> plot.item -> inventory.item
    farmer.incMoney(float(1000))

    animationLeft = []
    animationRight = []
    animationUp = []
    animationDown = []

    chosenAnimation = []
    animationsteps = 4
    last_update = pygame.time.get_ticks()
    animation_cooldown = 100  # in ms
    frame = 0

    idle_frame = sprite_sheet_idle.idle(0, 16, 16)

    for x in range(animationsteps):
        animationLeft.append(sprite_sheet_walk.walk_left(x, 16, 16))

    for x in range(animationsteps):
        animationDown.append(sprite_sheet_walk.walk_down(x, 16, 16))

    for x in range(animationsteps):
        animationUp.append(sprite_sheet_walk.walk_up(x, 16, 16))

    for x in range(animationsteps):
        animationRight.append(sprite_sheet_walk.walk_right(x, 16, 16))

    # initial player position
    playerPosition = pygame.Vector2(SCREEN.get_width() / 2, SCREEN.get_height() / 2)
    inventory_visible = True
    market_visible = False

    # INVENTORY SLOTS
    hand_slots = []
    bag_slots = []

    market_slots = []

    # PLOTS
    plot_coords = [
        # Adjust for screen size

        (SCREEN_WIDTH / 4 - 100, SCREEN_HEIGHT / 4 + 100),
        (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 + 100),
        (3 * SCREEN_WIDTH / 4 + 100, SCREEN_HEIGHT / 4 + 100),
        (SCREEN_WIDTH / 4 - 100, SCREEN_HEIGHT / 2 + 200),
        (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200),
        (3 * SCREEN_WIDTH / 4 + 100, SCREEN_HEIGHT / 2 + 200)

        # (190, 275),
        # (500, 275),
        # (810, 275),
        # (190, 575),
        # (500, 575),
        # (810, 575),
    ]

    plot_sprites_list = generate_plots(plot_coords)
    plot_sprites_group = pygame.sprite.Group(plot_sprites_list)
    truck = TruckSprite(SCREEN_WIDTH  - 300, SCREEN_HEIGHT / 2, market, farmer.inventory, SCREEN)

    for i in range(0, farmer.inventory.get_capacity()):
        bag_slots.append((SCREEN_WIDTH/4 + (i * 75), SCREEN_HEIGHT - 100))
        # bag_slots.append((25, 110 + (i * 75)))
        # Add a background bar for the inventory slots
    

    for i in range(0, farmer.inventory.get_handCapacity()):
        hand_slots.append((200 + (i * 75), 35))
    slot_width = 100  # CHANGE MARKET SLOT (Space in between)
    start_x = 200  # CHANGE MARKET SLOT POSITION (X-AXIS)
    start_y = 25  # CHANGE MARKET SLOT POSITION (Y-AXIS)
    for i in range(0, market.getMarketCap()):
        # put slots in middle of screen as a pop-up ui
        # every 5 slots, move down 75px
        x = start_x + (i % 5) * slot_width
        y = start_y + (i // 5) * slot_width
        market_slots.append((x, y))

    # INITIAL FARMER ITEMS

    # When objects are placed, user cant collide with them
    while running:
        # Event Polling



        moneyCount = farmer.getMoney()
        inventoryItems = farmer.inventory.get_contents()

        keys = pygame.key.get_pressed()
        # update animation
        now = pygame.time.get_ticks()
        if now - last_update >= animation_cooldown:
            frame = (frame + 1) % animationsteps
            last_update = now

        # Clear last frame on SCREEN with color / Background color
        SCREEN.fill("#264d26")

        ##  UI COMPONENTS --------------------------------------------

        # Load Images
        # Adjust for screen size
        pygame.draw.rect(SCREEN, "#287070", pygame.Rect(0, 0, SCREEN_WIDTH, 100))
        draw_clouds()
        # pygame.draw.rect(SCREEN, "#5a381c", pygame.Rect(690, 0, 310, 700))
        backpackImage = pygame.image.load(
            "assets/UI-Assets/MenuIcon.png"
        ).convert_alpha()
        # make backpack text under the backpack image
        backpackText = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 24).render(
            f"Menu", True, (255, 255, 255)
        )
        backpackTextBorder = pygame.font.Font(
            "assets/fonts/STORY NIGHT.TTF", 26
        ).render(f"Menu", True, (0, 0, 0))
        SCREEN.blit(backpackTextBorder, (25, 84))
        SCREEN.blit(backpackText, (25, 83))

        marketImage = pygame.image.load(
            "assets/UI-Assets/MarketIcon.png"
        ).convert_alpha()
        # make market text under the market image
        marketText = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 24).render(
            f"Market", True, (255, 255, 255)
        )
        marketTextBorder = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 26).render(
            f"Market", True, (0, 0, 0)
        )
        SCREEN.blit(marketTextBorder, (116, 84))
        SCREEN.blit(marketText, (116, 83))

        balanceText = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 45).render(
            f"Balance", True, (255, 255, 255)
        )
        balanceTextBorder = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 46).render(
            f"Balance", True, (0, 0, 0)
        )
        moneyCountText = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 44).render(
            f"${moneyCount}", True, (255, 255, 255)
        )
        moneyCountTextBorder = pygame.font.Font(
            "assets/fonts/STORY NIGHT.TTF", 45
        ).render(f"${moneyCount}", True, (0, 0, 0))

        inHandText = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 24).render(
            f"In Hand", True, (255, 255, 255)
        )
        inHandTextBorder = pygame.font.Font("assets/fonts/STORY NIGHT.TTF", 26).render(
            f"In Hand", True, (0, 0, 0)
        )
        SCREEN.blit(inHandTextBorder, (235, 6))
        
        SCREEN.blit(balanceTextBorder, (SCREEN_WIDTH - 200, 11))
        SCREEN.blit(balanceText, (SCREEN_WIDTH - 200, 10))
        SCREEN.blit(moneyCountTextBorder, (SCREEN_WIDTH - 200, 45))
        SCREEN.blit(moneyCountText, (SCREEN_WIDTH - 200, 46))
        SCREEN.blit(inHandText, (235, 5))
        plot_sprites_group.draw(SCREEN)

        exitToMenuButton = Button(10, 10, backpackImage, 0.15, "Inventory")
        marketButton = Button(100, 10, marketImage, 0.15, "Market")

        # Variable to track the visibility of the inventory UI

        # Draw UI
        marketButton.draw(SCREEN)
        exitToMenuButton.draw(SCREEN)
        
        hintShouldRun = False

        ## END OF UI COMPONENTS --------------------------------------------

        # Keyboard input handling

        is_Moving = False
        is_Moving_Horizontal = False
        # SCREEN_width, SCREEN_height = pygame.display.get_surface().get_size()
        SCREEN_height = 670
        if keys[pygame.K_LSHIFT]:
            velocity = 200
        else:
            velocity = 100
        if keys[pygame.K_w] and playerPosition.y - 90 - velocity * dt > 0:
            playerPosition.y -= velocity * dt
            if not is_Moving_Horizontal:
                chosenAnimation = animationUp
                SCREEN.blit(chosenAnimation[frame], playerPosition)
            is_Moving = True
        elif keys[pygame.K_s] and playerPosition.y + velocity * dt < SCREEN_HEIGHT - 90:
            playerPosition.y += velocity * dt
            if not is_Moving_Horizontal:
                chosenAnimation = animationDown
                SCREEN.blit(chosenAnimation[frame], playerPosition)
            is_Moving = True

        elif keys[pygame.K_a] and playerPosition.x - velocity * dt > 0:
            playerPosition.x -= velocity * dt
            chosenAnimation = animationLeft
            SCREEN.blit(chosenAnimation[frame], playerPosition)
            is_Moving = True
            is_Moving_Horizontal = True

        elif keys[pygame.K_d] and playerPosition.x + velocity * dt < SCREEN_WIDTH - 90:
            playerPosition.x += velocity * dt
            chosenAnimation = animationRight
            SCREEN.blit(chosenAnimation[frame], playerPosition)
            is_Moving = True
            is_Moving_Horizontal = True
        # Handle Harvesting
        elif keys[pygame.K_h]:
            for plotsprite in plot_sprites_group:
                if plotsprite.isPlayerNear(playerPosition.x, playerPosition.y) and plotsprite.readytoharvest == True:
                    crop_item = plotsprite.plot.harvest()
                    plotsprite.plantedTime = 0
                    plotsprite.growthTime = 0
                    farmer.inventory.add_item(crop_item)
                    plotsprite.readytoharvest = False
                    plotsprite.update() # Update the plot sprite
                    break # Only harvest one plot at a time
                
        # Use numbers to select items in inventory
        elif keys[pygame.K_1]:
            if len(inventoryItems) >= 1:
                key = list(inventoryItems.keys())[0]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_2]:
            if len(inventoryItems) >= 2:
                key = list(inventoryItems.keys())[1]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_3]:
            if len(inventoryItems) >= 3:
                key = list(inventoryItems.keys())[2]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_4]:
            if len(inventoryItems) >= 4:
                key = list(inventoryItems.keys())[3]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_5]:
            if len(inventoryItems) >= 5:
                key = list(inventoryItems.keys())[4]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_6]:
            if len(inventoryItems) >= 6:
                key = list(inventoryItems.keys())[5]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_7]:
            if len(inventoryItems) >= 7:
                key = list(inventoryItems.keys())[6]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_8]:
            if len(inventoryItems) >= 8:
                key = list(inventoryItems.keys())[7]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_9]:
            if len(inventoryItems) >= 9:
                key = list(inventoryItems.keys())[8]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)
        elif keys[pygame.K_0]:
            if len(inventoryItems) >= 10:
                key = list(inventoryItems.keys())[9]
                item = inventoryItems.get(key)
                farmer.inventory.add_handitem(item)

        if not is_Moving:
            SCREEN.blit(idle_frame, playerPosition)
        if not market_visible:
            plot_sprites_group.update(None, farmer.inventory, SCREEN) # Show information when hovering over plot

        # Draw the progress bar for each plot (when the seed is planted)     
        for plot in plot_sprites_group:
            plot.plotDegradation()
            plot.draw_progress_bar(SCREEN) 
            plot.draw_harvest_alert(SCREEN, playerPosition.x, playerPosition.y)
            plot.draw_harvest_directions(SCREEN, playerPosition.x, playerPosition.y)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not market_visible:
                    plot_sprites_group.update(event, farmer.inventory, SCREEN)
                mouse_pos = pygame.mouse.get_pos()
                if exitToMenuButton.check_for_input(mouse_pos):
                    pressedPlay = False
                
                    # inventory_visible = not inventory_visible
                    # inventory_debounce_time = current_time + 200
                if inventory_visible:
                    for i, slot_pos in enumerate(bag_slots):
                        slot_rect = pygame.Rect(slot_pos[0], slot_pos[1], 50, 50)
                        if slot_rect.collidepoint(mouse_pos):
                            if i < len(inventoryItems):  # Check if index is within range of inventoryItems
                                retrieved_key = list(inventoryItems.keys())[i]
                                clicked_item = inventoryItems.get(retrieved_key)
                                print(clicked_item.get_name())
                                if clicked_item.get_description(): #????
                                    # Put item in hand
                                    farmer.inventory.add_handitem(clicked_item)
                                    # Put item on hand slot

                # if user clicks on hand slot, it removes the item from hand
                if farmer.inventory.get_handContents() != {}:
                    for slot_pos in hand_slots:
                        slot_rect = pygame.Rect(slot_pos[0] + 35, slot_pos[1], 50, 50)
                        if slot_rect.collidepoint(mouse_pos):
                            current_key = list(farmer.inventory.get_handContents().keys())[hand_slots.index(slot_pos)]
                            clicked_item = farmer.inventory.get_handContents().get(current_key)
                            farmer.inventory.remove_handitem(clicked_item)
                            print("Item removed from hand")

                if marketButton.check_for_input(mouse_pos):
                    market_visible = not market_visible

                if market_visible:
                    for i, slot_pos in enumerate(market_slots):
                        # from left to right
                        slot_rect = pygame.Rect(
                            slot_pos[0] - 85, slot_pos[1] + 85, 75, 75
                        )
                        if slot_rect.collidepoint(mouse_pos):
                            if i < len(
                                market.getProducts()
                            ):  # Check if index is within range of marketItems
                                clicked_item = market.getProducts()[i]
                                if (
                                    clicked_item.get_description() == "seed"
                                    and farmer.getMoney() >= clicked_item.get_price()
                                ):
                                    farmer.inventory.add_item(clicked_item)
                                    farmer.decMoney(float(clicked_item.get_price()))
                                    # Print to console
                                    # Start Hint Text
                                    # playHintText(f"You bought {clicked_item.get_name()} for {clicked_item.get_price()}", 50, 50, 5)
                                    print(
                                        "You bought {0} for {1}".format(
                                            clicked_item.get_name(),
                                            clicked_item.get_price(),
                                        )
                                    )
                                elif (
                                    clicked_item.get_description() == "tool"
                                    and farmer.getMoney() >= clicked_item.get_price()
                                ):
                                    farmer.inventory.add_item(clicked_item)
                                    farmer.decMoney(float(clicked_item.get_price()))
                                    # Print to console
                                    print(
                                        "You bought {0} for {1}".format(
                                            clicked_item.get_name(),
                                            clicked_item.get_price(),
                                        )
                                    )
                                else:
                                    print(
                                        "You don't have enough money to buy this item"
                                    )
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    # print("E key pressed")
                    if truck.allowSell:
                        # print("Player is in range")
                        if truck.isThereAnItemToSell():
                            # print("There is an item to sell")
                            truck.getItemToSell()
                            # print("Item to sell is:", truck.getItemToSell().get_name())
                            market.sellProduct(truck.getItemToSell())
                        else:
                            print("There is no item to sell")
                    else:
                        print("Player is not in range")
                # if event.key == pygame.K_i:
                #     inventory_visible = not inventory_visible
                if event.key == pygame.K_m:
                    market_visible = not market_visible
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False

        if inventory_visible:
            open_inventory(farmer.inventory, bag_slots, inventoryItems)

        if market_visible:
            open_market(market, market_slots)
       
        for slot_pos in hand_slots:
            slot_surface = pygame.Surface((50, 50))
            slot_surface.fill((200, 200, 200))
            slot_surface.set_alpha(128)
            SCREEN.blit(slot_surface, (slot_pos[0] + 35, slot_pos[1]))
            # pygame.draw.rect(SCREEN, (200, 200, 200), pygame.Rect(slot_pos[0] + 35, slot_pos[1], 50, 50)) # Remove + 35 if > 2 hand slots

            temporary_index = 0
            if farmer.inventory.get_handContents() != {}:
                for key in farmer.inventory.get_handContents():
                    item = farmer.inventory.get_handContents().get(key)
                    if item.quantity >= 1:

                        item_image = item.get_image()
                        item_image = pygame.transform.scale(item_image, (50, 50))
                        quantity_text = pygame.font.Font(
                            "assets/fonts/GAMEPLAY.TTF", 11
                        ).render(f"x{item.quantity}", True, (255, 255, 255))
                        SCREEN.blit(
                            item_image,
                            (hand_slots[temporary_index][0] + 35, hand_slots[temporary_index][1]),
                        )
                        SCREEN.blit(
                            quantity_text,
                            (hand_slots[temporary_index][0] + 70, hand_slots[temporary_index][1] + 35),
                        )
                    temporary_index += 1
        # Draw the truck on the screen
        # So the truck is always on top of the plots
        truck.draw()
        truck.check_player(playerPosition.x, playerPosition.y)
        if pressedPlay == False:
            draw_startScreen()
        if pressedCredits == True:
            draw_credits_screen()
        if pressedHelp == True:
            draw_helpScreen()
        if pressedControls == True:
            draw_controls_help_screen()
        if pressedCrops == True:
            draw_crops_help_screen()
        if pressedFarming == True:
            draw_farming_help_screen()


        # Only count one press of the E key
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":

    play()
