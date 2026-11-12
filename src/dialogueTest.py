import pygame
from pathlib import Path

pygame.init()


GAME_WIDTH, GAME_HEIGHT = 320, 180 
scale= 4

screen = pygame.display.set_mode(
    (GAME_WIDTH*scale, GAME_HEIGHT*scale))

pygame.display.set_caption("Dialogue Box Test")

canvas = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

ROOT_DIR = Path(__file__).parent.parent
DIALOGUE_DIR = ROOT_DIR / "assets" / "ui" / "dialogue"
NAMEPLATE_DIR = DIALOGUE_DIR / "nameplates"

def load_image(path):
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")
    return pygame.image.load(str(path)).convert_alpha()



dialogueBox = load_image(DIALOGUE_DIR / "blankText.png")
arrow = load_image(DIALOGUE_DIR / "continueArrow.png")

nameplates= {
    "Maynne": load_image(NAMEPLATE_DIR / "maynne.png"),
    "Audra": load_image(NAMEPLATE_DIR / "audra.png"),
    "Death": load_image(NAMEPLATE_DIR / "death.png"),
    "Lyra": load_image(NAMEPLATE_DIR / "lyra.png"),
    "Mom": load_image(NAMEPLATE_DIR / "mom.png"),
    "Blank": load_image(NAMEPLATE_DIR / "blank.png")

}
dialogueIndex = 0

boxX, boxY = 19 , 124
nameplateX, nameplateY = 27, 116
arrowX, arrowY = 283, 158

arrowRect = pygame.Rect(
    arrowX -4,
    arrowY -4, 
    arrow.get_width() + 8, 
    arrow.get_height() + 8
    )
FONT_DIR = ROOT_DIR / "assets" / "fonts"

font = pygame.font.Font(
    str(FONT_DIR / "fusion-pixel-10px-monospaced-kr-latin-400-normal.ttf"),
    10
)
DIALOGUE_COLOUR = (232, 228, 240)
THINK_COLOUR = (170, 155, 205)

def textWrap(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = word if current_line == "" else current_line + " " + word

        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

dialogue = [
    ("Audra", "Hey Maynne! I didn't see you at class yesterday?", "speech"),
    ("Maynne", "Oh, right. Yeah, I wasn't feeling well, so I stayed home.", "speech"),
    ("Audra", "Aw, I'm sorry to hear that- blah blah blah", "speech"),
    ("Maynne", "I keep wondering whether things would have been different if I had made another choice.", "think"),
]

clock = pygame.time.Clock()
running = True

def advanceDialogue():
    global dialogueIndex
    dialogueIndex += 1

    if dialogueIndex >= len(dialogue):
        dialogueIndex = 0
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                advanceDialogue()
            elif event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx = event.pos[0] // scale
                my = event.pos[1] // scale

                if arrowRect.collidepoint(mx, my):
                    advanceDialogue()

    canvas.fill((10, 9, 14))

    speaker, line, dialogue_type = dialogue[dialogueIndex]

    if dialogue_type == "think":
        text_colour = THINK_COLOUR
    else:
        text_colour = DIALOGUE_COLOUR

    canvas.blit(dialogueBox, (boxX, boxY))

    if dialogue_type == "speech":
        canvas.blit(nameplates[speaker], (nameplateX, nameplateY))

    text_lines = textWrap(line, font, dialogueBox.get_width() - 24)

    text_x = boxX + 12
    text_y = boxY + 12
    line_height = font.get_linesize()

    for i, text_line in enumerate(text_lines):
        text_surface = font.render(text_line, True, text_colour)
        canvas.blit(text_surface, (text_x, text_y + i * line_height))

        canvas.blit(arrow, (arrowX, arrowY))

    scaled = pygame.transform.scale(canvas, screen.get_size())
    screen.blit(scaled, (0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()




                