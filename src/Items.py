from Objects import Object
from Load import load_image, BEDROOM_OBJECT_DIR, load_animations

def create_bedroom_items():

    items = {
        "bed": Object(
            "Bed",
            load_image("Bed.png", (200, 150), BEDROOM_OBJECT_DIR),
            300, 400,
            200, 150
        ),

        "flowers": Object(
            "Flowers",
            load_image("Lilies.png", (80, 120), BEDROOM_OBJECT_DIR),
            700, 350,
            80, 120
        ),

        "wall_decor": Object(
            "Decor",
            load_image("door.png", (100, 200), BEDROOM_OBJECT_DIR),
            1100, 300,
            100, 200
        )
    }

    return items