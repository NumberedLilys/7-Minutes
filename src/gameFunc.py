import pygame
import sys
from Player import Player
from Load import load_animations
from Backgrounds import create_backgrounds, create_buttons

# ====================== basic setup ==================

all_sprites = pygame.sprite.Group()

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

BUTTON_WIDTH, BUTTON_HEIGHT = 355, 90

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 1280, 720 default
clock = pygame.time.Clock()

# ============================ setting up display initializations ==============================

pygame.display.set_caption('7-Minutes')

animations = load_animations((128, 128))

backgrounds = create_backgrounds(SCREEN_WIDTH, SCREEN_HEIGHT)
# current_background = "opening_screen"

my_character = Player(animations, 375, 275, SCREEN_WIDTH)

all_sprites = pygame.sprite.Group()
all_sprites.add(my_character)

def game():
    current_background = "bedroom"

    while True:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

def start_screen():
    current_background = "opening_screen"
    start_buttons = create_buttons(BUTTON_WIDTH, BUTTON_HEIGHT)

    while True:
        backgrounds[current_background].draw(screen)

        mouse = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        play_button = pygame.Rect(695, 301, BUTTON_WIDTH, BUTTON_HEIGHT)
        quit_button = pygame.Rect(756, 420, BUTTON_WIDTH, BUTTON_HEIGHT)

        if play_button.collidepoint(mouse):
            if mouse_pressed[0]:  # Left mouse button is pressed
                button_image = start_buttons["start_click"]
            else:
                button_image = start_buttons["start_hover"]
        else:
            button_image = start_buttons["regular"]

        screen.blit(button_image, play_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(mouse):
                    game()

            if quit_button.collidepoint(mouse):
                pygame.quit()
                sys.exit()

        pygame.display.flip()