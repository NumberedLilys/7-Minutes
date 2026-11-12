import pathlib
import pygame

ROOT_DIR = pathlib.Path(__file__).parent.parent
MAYNNE_DIR = ROOT_DIR / "assets" / "characters" / "Maynne"
WALK_DIR = MAYNNE_DIR / "Walk"
IDLE_DIR = MAYNNE_DIR / "Idle"

BACKGROUND_DIR = ROOT_DIR / "assets" / "environments"
START_DIR = BACKGROUND_DIR / "StartScreen"
BUTTON_DIR = START_DIR / "Buttons"

def load_image(name, size, path):
    path = path.joinpath(name)
    try:
        img = pygame.image.load(str(path)).convert_alpha()
    except FileNotFoundError:
        print(f"Error: Could not find image at {path}. Using placeholder.")
        img = pygame.Surface(size)
        img.fill((0, 255, 0))
    return pygame.transform.scale(img, size)


def load_animations(size):
    walk_right = [load_image(f"MaynneWalk_{i:04d}.png", size, WALK_DIR) for i in range(1, 10)]
    walk_left = [pygame.transform.flip(f, True, False) for f in walk_right]

    idle_right = [load_image(f"MaynneIdle_{i:04d}.png", size, IDLE_DIR) for i in range(1, 10)]
    idle_left = [pygame.transform.flip(f, True, False) for f in idle_right]

    return {
        "walk_right": walk_right,
        "walk_left": walk_left,
        "idle_right": idle_right,
        "idle_left": idle_left,
    }

