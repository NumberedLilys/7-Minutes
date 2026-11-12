from Background import Background
from Load import load_image, BACKGROUND_DIR, START_DIR, BUTTON_DIR

def create_backgrounds(screen_width, screen_height):
    size = (screen_width, screen_height)

    backgrounds = {
        "opening_screen": Background(
            load_image("Splash_art.png", size, START_DIR),
            1280, 720
        ),

        "bedroom": Background(
            load_image("temp-background-1.jpg", size, BACKGROUND_DIR),
            1280, 720,
            right_target="living_room"
        ),

        "living_room": Background(
            load_image("temp-background-2.jpg", size, BACKGROUND_DIR),
            1280, 720,
            left_target="bedroom",
            right_target="kitchen"
        )
    }

    return backgrounds

def create_buttons(button_width, button_height):
    size = (button_width, button_height)

    start_buttons = {
        "regular": load_image("StartRegular.png", size, BUTTON_DIR),

        "start_hover": load_image("StartHover.png", size, BUTTON_DIR),

        "start_click": load_image("StartClick.png", size, BUTTON_DIR)
    }

    return start_buttons