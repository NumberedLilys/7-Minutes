from Objects import Object
from Load import load_image, BEDROOM_OBJECT_DIR, BEDROOM_DIR
from Dialogue import BEDROOM_DIALOGUES

def create_bedroom_items():

    items = {
        "bed": Object(
            "Bed",
            load_image("Bed.png", None, BEDROOM_DIR),
            69, 92,
            dialogue = BEDROOM_DIALOGUES["bed"]
        ),

        "flowers": Object(
            "Flowers",
            load_image("Lilies.png", None, BEDROOM_OBJECT_DIR),
            395, 73,
            dialogue = BEDROOM_DIALOGUES["flowers"]
        ),

        "wall_decor": Object(
            "Decor",
            load_image("WallDecor.png", None, BEDROOM_OBJECT_DIR),
            354, 20,
            dialogue = BEDROOM_DIALOGUES["wall decor"]
        ),
        "book_shelf": Object(
            "Bookshelf",
            load_image("Bookshelf.png", None, BEDROOM_DIR),
            0,10
        ),
        "dresser": Object(
            "Dresser",
            load_image("Dresser.png", None, BEDROOM_DIR),
            352, 112
        ),
        "calendar": Object(
            "Calendar",
            load_image("Calendar.png", None, BEDROOM_OBJECT_DIR),
            456,41
        )

    }

    return items