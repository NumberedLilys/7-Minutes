from Background import Background
from Load import load_image, BACKGROUND_DIR

def create_backgrounds(screen_width, screen_height):
    size = (screen_width, screen_height)

    backgrounds = {
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