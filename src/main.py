import pygame
import sys
from Player import Player
from Load import load_animations

# ======================basic setup==================

all_sprites = pygame.sprite.Group()

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 1280, 720 default
clock = pygame.time.Clock()

# ============================setting up display==============================
pygame.display.set_caption('7-Minutes')

animations = load_animations((128, 128))

my_character = Player(animations, 375, 275, SCREEN_WIDTH)

all_sprites = pygame.sprite.Group()
all_sprites.add(my_character)

running = True

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    screen.fill((0, 0, 0))

    all_sprites.draw(screen) # "draws" sprites in group onto screen
    pygame.display.flip()

pygame.quit()
sys.exit()