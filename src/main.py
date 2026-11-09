import pygame
import sys
from Player import Player
from Load import load_animations
from Backgrounds import create_backgrounds

# ====================== basic setup ==================

all_sprites = pygame.sprite.Group()

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 1280, 720 default
clock = pygame.time.Clock()

# ============================ setting up display initializations ==============================

pygame.display.set_caption('7-Minutes')

animations = load_animations((128, 128))

backgrounds = create_backgrounds(SCREEN_WIDTH, SCREEN_HEIGHT)
current_background = "bedroom"

my_character = Player(animations, 375, 275, SCREEN_WIDTH)

all_sprites = pygame.sprite.Group()
all_sprites.add(my_character)

# ============================ running program ==============================

running = True

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    # ============================ determining current room, adjusting ==============================

    next_background = backgrounds[current_background].check_transition(
        my_character.rect
    )

# Move character to the opposite side of the new room (starting from left, outside of hitbox area, 50 pixels)

    if next_background is not None and next_background in backgrounds: 

        current_background = next_background # changing current room to the newly entered one

        if my_character.rect.left <= 50:
            my_character.rect.left = SCREEN_WIDTH - 50 - my_character.rect.width
        else:
            my_character.rect.left = 50

    backgrounds[current_background].draw(screen) # draws current background onto screen

    # ============================ adding character sprite ==============================

    all_sprites.draw(screen)  # "draws" sprites in group onto screen
    pygame.display.flip()

pygame.quit()
sys.exit()