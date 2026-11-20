from Objects import Object
from Load import load_image, BEDROOM_OBJECT_DIR, BEDROOM_DIR
from Dialogue import BEDROOM_DIALOGUES

def create_bedroom_items():

    items = {
        "bed": Object(
            "Bed",
            load_image("Bed.png", (400, 500), BEDROOM_DIR),
            300, 400,
            400, 500,  # Must match the dimensions in the load_image
            dialogue = BEDROOM_DIALOGUES["bed"]
        ),

        "flowers": Object(
            "Flowers",
            load_image("Lilies.png", (80, 120), BEDROOM_OBJECT_DIR),
            700, 350,
            80, 120,
            dialogue = BEDROOM_DIALOGUES["flowers"]
        ),

        "wall_decor": Object(
            "Decor",
            load_image("WallDecor.png", (100, 200), BEDROOM_OBJECT_DIR),
            1100, 300,
            100, 200,
            dialogue = BEDROOM_DIALOGUES["wall decor"]
        )
    }

    return items