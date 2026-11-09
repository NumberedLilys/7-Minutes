import pygame
import sys

class Background:
    def __init__(self, image, screen_width, screen_height,
                 left_target=None, right_target=None):
        
        self.image = image
        self.rect = self.image.get_rect(topleft=(0, 0))
        
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.left_hitbox = pygame.Rect(0, 0, 50, screen_height) # hitbox is 50 pixels
        self.right_hitbox = pygame.Rect(screen_width - 50, 0, 50, screen_height)

        self.left_target = left_target # The image to be loaded when going to the left 
        self.right_target = right_target # The image to be loaded when going to the right

    def check_transition(self, player_rect):
        if self.left_hitbox.colliderect(player_rect):
            return self.left_target

        if self.right_hitbox.colliderect(player_rect):
            return self.right_target

        return None

    def draw(self, screen):
        screen.blit(self.image, self.rect)
