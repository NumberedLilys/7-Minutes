import pygame

class Background:
    def __init__(self, image, screen_width, screen_height,
                 left_target=None, right_target=None):
        
        self.image = image
        self.rect = self.image.get_rect(topleft=(0, 0))

        #visible screen dimensions
        self.screen_width = screen_width
        self.screen_height = screen_height

        #actual dimensions of the background image
        self.world_width = self.image.get_width()
        self.world_height= self.image.get_height()

        #starting camera position
        self.camera_x = 0

        #hitbox is 50 px, found at the left and right edges of the background image
        self.left_hitbox = pygame.Rect(0, 0, 50, self.world_height)
        self.right_hitbox = pygame.Rect(self.world_width - 50, 0, 50, self.world_height)

        self.left_target = left_target # The image to be loaded when going to the left 
        self.right_target = right_target # The image to be loaded when going to the right

    def update_camera(self, player_rect):
        # keep player near the centre of the visible screen
        self.camera_x = player_rect.centerx - self.screen_width // 2

        # keeping camera from going out of bounds
        self.camera_x = max(
            0,
              min(self.camera_x, self.world_width - self.screen_width)
            )
        
    def check_transition(self, player_rect):
        if self.left_hitbox.colliderect(player_rect):
            return self.left_target

        if self.right_hitbox.colliderect(player_rect):
            return self.right_target

        return None

    def draw(self, screen):
        screen.blit(self.image, (-self.camera_x, 0))
