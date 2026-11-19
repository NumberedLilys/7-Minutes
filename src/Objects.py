import pygame
from dialogueTest import startInteraction

class Object:
    def __init__(self, name, image, item_x, item_y,
                 item_width, item_height):

        self.name = name
        self.image = image

        self.rect = pygame.Rect(
            item_x, item_y, item_width, item_height
        )

        self.hitbox = self.rect.copy()

    def check_click(self, mouse_pos):
        if self.hitbox.collidepoint(mouse_pos):
            # startInteraction(self.name)
            print(f"{self.name} WAS CLICKED")

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# IN WHILE LOOP OF GAME:
#   FOR ITEM IN BEDROOM_ITEMS:
        # items[ITEM].draw(screen)