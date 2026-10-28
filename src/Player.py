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

# # ======================basic setup==================

# all_sprites = pygame.sprite.Group()

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# # ==========================Loading asset from assets==========================
# current_dir = pathlib.Path(__file__).parent
# image_path = current_dir.parent.joinpath("assets", "MC-SCREENSHOT.png")

# try:
#     player_image = pygame.image.load(str(image_path)).convert_alpha()
# except FileNotFoundError:
#     print(f"Error: Could not find image at {image_path}. Using placeholder.")
#     player_image = pygame.Surface((64, 64))
#     player_image.fill((0, 255, 0))

# # ============================setting up display==============================
# pygame.display.set_caption('Random title')

# my_character = Player(player_image, 375, 275)
# my_character.rect.x = 375
# my_character.rect.y = 175

# all_sprites.add(my_character)

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit(); sys.exit()
#             running = False

#     all_sprites.update()

#     screen.fill((0, 0, 0))

#     all_sprites.draw(screen) # "draws" sprites in group onto screen
#     pygame.display.flip()

#     clock.tick(60)
# pygame.quit()
# sys.exit()