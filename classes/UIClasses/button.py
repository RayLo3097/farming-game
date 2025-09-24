import pygame
import time


class Button:

    x: int
    y: int
    name: str

    def __init__(self, x, y, image, scale, name, action=None):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.name = name
        self.action = action

        # self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        # if self.rect.collidepoint(pos):
        # self.rect.transform.scale(self.image, (int(self.image.get_width() * 1.1), int(self.image.get_height() * 1.1)))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)

    def update(self, mouse):

        pressed = False
        if self.rect.collidepoint(mouse):

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not self.clicked:
                            self.clicked = True
                            print(self.name + " button clicked")
                            return 1
                            break
        else:
            self.clicked = False
        return None

    def check_for_input(self, position):
        if self.rect.collidepoint(position):
            return True
        else:
            return False
        return False
