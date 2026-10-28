import pygame
import sys
import pathlib
from Player import Player

# ======================basic setup==================

all_sprites = pygame.sprite.Group()

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# ==========================Loading asset from assets==========================
current_dir = pathlib.Path(__file__).parent
image_path = current_dir.parent.joinpath("assets", "MC-SCREENSHOT.png")

try:
    player_image = pygame.image.load(str(image_path)).convert_alpha()
except FileNotFoundError:
    print(f"Error: Could not find image at {image_path}. Using placeholder.")
    player_image = pygame.Surface((64, 64))
    player_image.fill((0, 255, 0))

# ============================setting up display==============================
pygame.display.set_caption('Random title')

my_character = Player(player_image, 375, 275)
my_character.rect.x = 375
my_character.rect.y = 175

all_sprites.add(my_character)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            running = False

    all_sprites.update()

    screen.fill((0, 0, 0))

    all_sprites.draw(screen) # "draws" sprites in group onto screen
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
sys.exit()