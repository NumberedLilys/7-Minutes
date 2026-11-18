import pygame
# import (currently) non-existent dialogue option to call with interactive

# Each object will have a boolean when called (formatted like backgrounds) to determine if you can interact?
class Object(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, interactable):
        super().__init__()
        self.image = image
        self.width = width
        self.interactable = interactable

    # def interactive(self):
        