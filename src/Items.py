from Objects import Object
from Load import load_image, BEDROOM_OBJECT_DIR, BEDROOM_DIR,KITCHEN_DIR
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

def create_kitchen_items():
    
    items = {
        "cabinets": Object(
            "Cabinets",
            load_image("Cabinets.png", None, KITCHEN_DIR),
            360, 8,
        ),

        "counter": Object(
            "Counter",
            load_image("Counter.png", None, KITCHEN_DIR),
            360, 95,
        ),

        "fridge": Object(
            "Fridge",
            load_image("Fridge.png", None, KITCHEN_DIR),
            600, 40,
        ),
        "breakfast": Object(
            "Breakfast",
            load_image("Breakfast.png", None, KITCHEN_DIR),
            514,105
        ),
        "bench": Object(
            "Bench",
            load_image("Bench.png", None, KITCHEN_DIR),
            738, 127
        ),
        "calendar": Object(
            "Calendar",
            load_image("Calendar.png", None, KITCHEN_DIR),
            869, 61
        ),
        "coat_rack": Object(
            "Coat Rack",
            load_image("CoatRack.png", None, KITCHEN_DIR),
            768, 64
        )

    }

    return items