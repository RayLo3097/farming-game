import pygame

# This class is used for the hint text that appears on the screen.
#      Some use cases include:
#          - What to do next
#          - When the user tries to plant a seed without water or fertilizer
#          - When the user tries to sell an item


class Hint:

    def __init__(self, screen = None, hint = None, hint_font = None, hint_text = None):
        self.hint = hint
        self.screen = screen
        self.hint_font = pygame.font.Font(None, 36)
        self.hint_text = self.hint_font.render(self.hint, True, (255, 255, 255))

    # draw the hint text
    #      This method is used to draw the hint text on the screen.
    
    def draw(self):
        self.screen.blit(self.hint_text, (50, 50))
