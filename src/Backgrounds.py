from Background import Background
from Load import load_image, BACKGROUND_DIR, START_DIR, BUTTON_DIR, BEDROOM_DIR
from Load import KITCHEN_DIR, NEIGHBOURHOOD_DIR, CAMPUS_DIR

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
            load_image("Background.png", None, KITCHEN_DIR),
            screen_width,
            screen_height,
            left_target="bedroom",
            right_target="neighbourhood"
        ),
        "neighbourhood": Background(
            load_image("Neighbourhood.png", None, NEIGHBOURHOOD_DIR),
            screen_width,
            screen_height,
            left_target="kitchen"
        ),
        "campus": Background(
            load_image("Background.png", None, CAMPUS_DIR),
            screen_width,
            screen_height,
            left_target="neighbourhood"
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