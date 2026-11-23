import pygame
import sys
from Player import Player
from Load import load_animations, ROOT_DIR, load_image
from Backgrounds import create_backgrounds, create_buttons
from Items import create_bedroom_items, create_kitchen_items
from Timer import GameTimer
from Dialogue import BEDROOM_DIALOGUES, TIMED_DIALOGUE
from timedEvents import setup_timed_events
from Audio import audio
from Fade import Fade

# ====================== basic setup ==================

pygame.init()

GAME_WIDTH, GAME_HEIGHT = 320, 180 # Logical game resolution, what assets are based on
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720 # Actual screen resolution
SCALE = 4 
BUTTON_WIDTH, BUTTON_HEIGHT = 355, 90
# Character starting location, changed for game resultion (divided by SCALE)
MAYNNE_X, MAYNNE_Y = 144, 110 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 1280, 720 default
canvas = pygame.Surface((GAME_WIDTH, GAME_HEIGHT)) # 320, 180 default

clock = pygame.time.Clock()

from DialogueManager import DialogueManager
from characterNames import Nameplates

box_image = Nameplates["BlankText"]
dialogue_font = pygame.font.Font(ROOT_DIR / "assets" / "fonts" / "fusion-pixel-10px-monospaced-kr-latin-400-normal.ttf", 10)
dialogue = DialogueManager(dialogue_font, box_image, Nameplates, SCALE)

# ============================ setting up display initializations ==============================

pygame.display.set_caption('7-Minutes')

animations = load_animations((64, 64)) #changed to accurate dimensions

backgrounds = create_backgrounds(GAME_WIDTH, GAME_HEIGHT)
# current_background = "opening_screen"

bedroom_items = create_bedroom_items()
kitchen_items = create_kitchen_items()

BEDROOM_DIALOGUES["flowers"]["start"]["options"][0]["action"] = bedroom_items["flowers"].remove

my_character = Player(animations, MAYNNE_X, MAYNNE_Y, backgrounds["bedroom"].world_width) #changed for game resolution

all_sprites = pygame.sprite.Group()
all_sprites.add(my_character)
END_DIR = ROOT_DIR / "assets" / "characters"
dialogue_images = {
    "death_ending": load_image(
        "grim_reaper_temp.png",
        (80, 80),
        END_DIR
    )
}

def game():
    current_background = "bedroom"
    my_character.world_width = backgrounds[current_background].world_width

    timer = GameTimer(7)
    # ====== adding fade for end of game ========
    fade = Fade(320, 180, duration=2000)
    ending_state = {
        "image_active": False,
        "text_active": False,
        "waiting_for_input": False
    }

    def start_ending_text():
        fade.start()

    TIMED_DIALOGUE["death_ending"]["maynne_response_6"]["options"][0]["action"] = start_ending_text

    # ====== loop ======
    def get_current_room():
        return current_background

    setup_timed_events(timer, dialogue, get_current_room, ending_state)

    while True:
        dt = clock.tick(60)
        timer.update(dt)
        fade.update(dt)
        if fade.finished and not ending_state["text_active"]:
            ending_state["text_active"] = True
            ending_state["waiting_for_input"] = True

        audio.play_ambience(current_background)

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ending_state["waiting_for_input"]:
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        pygame.quit()
                        sys.exit()

                continue

            if dialogue.active:
                dialogue.handle_event(event) # if text box open, no click items

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # if text box not open, click items
                if current_background == "bedroom":
                    camera_x = backgrounds[current_background].camera_x

                    #converting window mouse position to logical game coords
                    mouse_x = event.pos[0]/ SCALE + camera_x
                    mouse_y = event.pos[1]/ SCALE

                    logic_mouse_pos = (mouse_x, mouse_y)

                    for item in bedroom_items.values():
                        triggered_dialogue = item.check_click(logic_mouse_pos)

                        if triggered_dialogue:
                            dialogue.start(triggered_dialogue)
                            break
                elif current_background == "kitchen":
                    camera_x = backgrounds[current_background].camera_x

                    #converting window mouse position to logical game coords
                    mouse_x = event.pos[0]/ SCALE + camera_x
                    mouse_y = event.pos[1]/ SCALE

                    logic_mouse_pos = (mouse_x, mouse_y)

                    for item in kitchen_items.values():
                        triggered_dialogue = item.check_click(logic_mouse_pos)

                        if triggered_dialogue:
                            dialogue.start(triggered_dialogue)
                            break
        
        all_sprites.update(dt, dialogue.active)

        #updating camera After player movement
        backgrounds[current_background].update_camera(my_character.rect)

        backgrounds[current_background].draw(canvas)
        camera_x = backgrounds[current_background].camera_x

        # #drawing room objects
        if current_background == "bedroom":
            camera_x = backgrounds[current_background].camera_x
            for item in bedroom_items.values():
                item.draw(canvas, camera_x)
                
        elif current_background == "kitchen":
            for item in kitchen_items.values():
                item.draw(canvas, camera_x)

        # ============================ determining current room, adjusting ==============================

        next_background = backgrounds[current_background].check_transition(
            my_character.rect
        )

        # Move character to the opposite side of the new room (starting from left, outside of hitbox area, 50 pixels)

        if next_background is not None and next_background in backgrounds: 

            current_background = next_background # changing current room to the newly entered one
            my_character.world_width = backgrounds[current_background].world_width

            if my_character.rect.left <= 50:
                my_character.rect.left = (
                    backgrounds[current_background].world_width - 50 - my_character.rect.width
                )
            else:
                my_character.rect.left = 50

        # ============================ adding character sprite ==============================
        #update camera position based on character's position, then draw the background and character sprite
        camera_x = backgrounds[current_background].camera_x

        for sprite in all_sprites:
            canvas.blit(sprite.image,
                        (sprite.rect.x - camera_x, sprite.rect.y)
                    )
        
        # all_sprites.draw(screen)  # "draws" sprites in group onto screen
        
        # ============== timer ================
        timer_text = timer.get_countdown()

        timer_surface = dialogue_font.render(
            timer_text,
            True,
            (255, 255, 255)
        )

        timer_rect = timer_surface.get_rect(
            topright=(GAME_WIDTH - 8, 8)
        )

        canvas.blit(timer_surface, timer_rect)

        # ========== canvas ==========
        if ending_state["image_active"]:
            image = dialogue_images["death_ending"]
            canvas.blit(image, (200, 80))

        dialogue.draw(canvas)   
        fade.draw(canvas)

        if ending_state["text_active"]:
            ending_message = "Your Regrets:"

            text_surface = dialogue_font.render(
                ending_message,
                True,
                (255, 255, 255)
            )

            text_rect = text_surface.get_rect(
                center=(GAME_WIDTH // 2, GAME_HEIGHT // 2)
            )

            canvas.blit(text_surface, text_rect)

            prompt_surface = dialogue_font.render(
                "Press SPACE to exit game",
                True,
                (180, 180, 180)
            )

            prompt_rect = prompt_surface.get_rect(
                center=(GAME_WIDTH // 2, GAME_HEIGHT - 25)
            )

            canvas.blit(prompt_surface, prompt_rect)

        scaled_canvas = pygame.transform.scale(
            canvas,(SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        screen.blit(scaled_canvas, (0, 0))  # draws scaled canvas onto screen

        # all_sprites.draw(screen)  # "draws" sprites in group onto screen
        pygame.display.flip()



# ================ START SCREEN FUNCTION ==============
def start_screen():
    current_background = "opening_screen"
    start_buttons = create_buttons(BUTTON_WIDTH, BUTTON_HEIGHT)

    audio.play_music("start")

    while True:
        # Draw the opening background
        backgrounds[current_background].draw(screen)

        mouse = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        play_button = pygame.Rect(695, 301, BUTTON_WIDTH, BUTTON_HEIGHT)
        quit_button = pygame.Rect(756, 420, BUTTON_WIDTH, BUTTON_HEIGHT)

        # Determine which button image to display
        if play_button.collidepoint(mouse):
            if mouse_pressed[0]:  # Left mouse button is pressed
                button_image = start_buttons["start_click"]
            else:
                button_image = start_buttons["start_hover"]
        else:
            button_image = start_buttons["regular"]

        # Draw the start button
        screen.blit(button_image, play_button)

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if play_button.collidepoint(event.pos):
                    audio.play_sound("click")
                    game()
                    return

                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)