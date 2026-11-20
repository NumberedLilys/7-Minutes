from Background import Background
from Load import load_image, BACKGROUND_DIR, START_DIR, BUTTON_DIR, BEDROOM_DIR


def create_backgrounds(screen_width, screen_height):

    backgrounds = {
        # Start screen: full window resolution
        "opening_screen": Background(
            load_image("Splash_art.png", (1280, 720), START_DIR),
            1280,
            720
        ),

        # Game rooms: logical resolution, with a wider background
        "bedroom": Background(
            load_image("Background.png", (640, 180), BEDROOM_DIR),
            screen_width,
            screen_height,
            right_target="kitchen"
        ),

        "kitchen": Background(
            load_image("temp-background-2.jpg", (640, 180), BACKGROUND_DIR),
            screen_width,
            screen_height,
            left_target="bedroom",
            right_target="living_room"
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