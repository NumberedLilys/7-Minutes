from Objects import Object
from Load import load_image, BEDROOM_OBJECT_DIR, BEDROOM_DIR,KITCHEN_DIR, NEIGHBOURHOOD_DIR, CAMPUS_DIR
from Dialogue import BEDROOM_DIALOGUES, KITCHEN_DIALOGUE, NEIGHBOURHOOD_DIALOGUE

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
            514,105,
            dialogue = KITCHEN_DIALOGUE["breakfast"]
        ),
        "bench": Object(
            "Bench",
            load_image("Bench.png", None, KITCHEN_DIR),
            738, 127
        ),
        "calendar": Object(
            "Calendar",
            load_image("Calendar.png", None, KITCHEN_DIR),
            869, 61,
            dialogue = KITCHEN_DIALOGUE["calendar"]
        ),
        "coat_rack": Object(
            "Coat Rack",
            load_image("CoatRack.png", None, KITCHEN_DIR),
            768, 64
        )

    }

    return items

def create_neighbourhood_items():

    items = {
        "stop_sign": Object(
            "Stop Sign",
            load_image("BusStop.png", None, NEIGHBOURHOOD_DIR),
            252, 40,
            dialogue=NEIGHBOURHOOD_DIALOGUE["bus stop"]
        ),

    }

    return items

def create_campus_items():
    items ={
        "school_plaque": Object(
            "School Plaque",
            load_image("SchoolPlaque.png", None, CAMPUS_DIR),
            113,136
        ),
        "bench": Object(
            "Bench",
            load_image("Bench.png", None, CAMPUS_DIR),
            748, 141
        ),
        "classroom_door": Object(
            "Classroom Door",
            load_image("ClassroomDoor.png", None, CAMPUS_DIR),
            464,73
        ),
        "Studyroom_Door": Object(
            "Studyroom Door",
            load_image("StudyDoor.png", None, CAMPUS_DIR),
            625,73
        ),
        "FireExit_Door": Object(
            "FireExit Door",
            load_image("FireExitDoor.png", None, CAMPUS_DIR),
            874,74
        )

    }

    return items