from Load import DIALOGUE_DIR, NAMEPLATE_DIR, load_image

Nameplates = {
    "Audra": load_image("Audra.png", (53, 16), NAMEPLATE_DIR),
    "Blank": load_image("Blank.png", (53, 16), NAMEPLATE_DIR),
    "Death": load_image("Death.png", (53, 16), NAMEPLATE_DIR),
    "Lyra": load_image("Lyra.png", (53, 16), NAMEPLATE_DIR),
    "Maynne": load_image("Maynne.png", (88, 16), NAMEPLATE_DIR),
    "Mom": load_image("Mom.png", (55, 16), NAMEPLATE_DIR),

    "BlankText": load_image("BlankText.png", (280, 50), DIALOGUE_DIR),
    "continueArrow": load_image("continueArrow.png", (50, 50), DIALOGUE_DIR)
}