import pygame

# ==================Player initialization==============================
class Player(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        super().__init__()

        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100
        self.speed = 5

# ===============Updates based on player movement left/right===============
    def update(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rect.x -= self.speed

            if keys[pygame.K_d]:
                self.rect.x += self.speed

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > 800:
                self.rect.right = 800
