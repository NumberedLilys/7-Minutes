import pygame
import sys
from Player import Player
from Load import load_animations
from Backgrounds import create_backgrounds, create_buttons
from Items import create_bedroom_items

# ====================== basic setup ==================

all_sprites = pygame.sprite.Group()

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720 # 1280, 720 --> Default

BUTTON_WIDTH, BUTTON_HEIGHT = 355, 90

MAYNNE_X, MAYNNE_Y = 575, 475 # character location on X, Y

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 1280, 720 default
clock = pygame.time.Clock()

# ============================ setting up display initializations ==============================

pygame.display.set_caption('7-Minutes')

animations = load_animations((225, 256)) # 128, 128 (character size)

backgrounds = create_backgrounds(SCREEN_WIDTH, SCREEN_HEIGHT)
# current_background = "opening_screen"

bedroom_items = create_bedroom_items()

my_character = Player(animations, MAYNNE_X, MAYNNE_Y, SCREEN_WIDTH)

all_sprites = pygame.sprite.Group()
all_sprites.add(my_character)

def game():
    current_background = "bedroom"

    while True:
        screen.fill((0, 0, 0)) 

        dt = clock.tick(60)
        
        backgrounds[current_background].draw(screen) # draws current background onto screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_background == "bedroom":
                    for item in bedroom_items.values():
                        item.check_click(event.pos)

        all_sprites.update(dt)
        if current_background == "bedroom":
            for item in bedroom_items.values():
                item.draw(screen)
                
        elif current_background == "kitchen":
            pass

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