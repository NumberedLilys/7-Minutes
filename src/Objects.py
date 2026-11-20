import pygame
#from dialogueTest import startInteraction

class Object:
    def __init__(self, name, image, item_x, item_y,
                 item_width=None, item_height=None, dialogue = None):

        self.name = name
        self.image = image
        self.dialogue = dialogue

        #unless specified use the actual dimensions
        if item_width is None:
            item_width = image.get_width()

        if item_height is None:
            item_height = image.get_height()

        self.rect = pygame.Rect(
            item_x, item_y, item_width, item_height
        )

        self.hitbox = self.rect.copy()

    def check_click(self, mouse_pos):
        if self.hitbox.collidepoint(mouse_pos):
            print(f"{self.name} WAS CLICKED")
            return self.dialogue
        return None

    def draw(self, screen, camera_x=0):
        screen.blit(
            self.image,
            (self.rect.x - camera_x, self.rect.y)
        )