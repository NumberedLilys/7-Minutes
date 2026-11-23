import pathlib
import pygame

ROOT_DIR = pathlib.Path(__file__).parent.parent
MAYNNE_DIR = ROOT_DIR / "assets" / "characters" / "Maynne"
WALK_DIR = MAYNNE_DIR / "Walk"
IDLE_DIR = MAYNNE_DIR / "Idle"
LYRA_DIR = ROOT_DIR / "assets" / "characters" / "Lyra"

BACKGROUND_DIR = ROOT_DIR / "assets" / "environments"
BEDROOM_DIR = BACKGROUND_DIR / "Bedroom"
BEDROOM_OBJECT_DIR = BEDROOM_DIR / "Objects"
KITCHEN_DIR = BACKGROUND_DIR / "Kitchen"
START_DIR = BACKGROUND_DIR / "StartScreen"
BUTTON_DIR = START_DIR / "Buttons"

DIALOGUE_DIR = ROOT_DIR / "assets" / "ui" / "dialogue"
NAMEPLATE_DIR = DIALOGUE_DIR / "NamePlates"

def load_image(name, size=None, path=None):
    if path is None:
        raise ValueError("An asset directory must be provided.")

    image_path = path / name

    try:
        img = pygame.image.load(str(image_path)).convert_alpha()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find image: {image_path}")

    # Only resize if a valid size was provided
    if size is not None:
        if (
            not isinstance(size, (tuple, list))
            or len(size) != 2
            or not all(isinstance(value, (int, float)) for value in size)
        ):
            raise ValueError(
                f"Invalid image size for {name}: {size}"
            )

        size = (int(size[0]), int(size[1]))

        if img.get_size() != size:
            img = pygame.transform.scale(img, size)

    return img


def load_animations(size):
    walk_right = [load_image(f"MaynneWalk_{i:04d}.png", size, WALK_DIR) for i in range(1, 10)]
    walk_left = [pygame.transform.flip(f, True, False) for f in walk_right]

    idle_right = [load_image(f"MaynneIdle_{i:04d}.png", size, IDLE_DIR) for i in range(1, 10)]
    idle_left = [pygame.transform.flip(f, True, False) for f in idle_right]

    lyra_idle = [load_image(f"LyraIdle_{i:04d}.png", size, LYRA_DIR) for i in range(1, 12)]

    return {
        "walk_right": walk_right,
        "walk_left": walk_left,
        "idle_right": idle_right,
        "idle_left": idle_left,
        "lyra_idle": lyra_idle
    }

