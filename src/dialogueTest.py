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
    # Opening - Maynne’s Room
    # Maynne's morning thoughts
    ("Maynne", "Okay. Class, notes, study group. Get through today, go home, sleep for twelve hours. Where's my charger?", "think"),
    ("Maynne", "Oh, it's under everything.", "think"),
    
    # Mom calls from downstairs
    ("Mom", "Maynne! Breakfast's ready!", "speech"),
    ("Maynne", "Coming!", "speech"),
    
    # Looking outside the window
    ("Maynne", "Looks nice outside. Shame I'll be spending most of it indoors.", "think"),
    
    # Looking at the clock
    ("Maynne", "Oh, I'm actually going to be late.", "think"),
]

interactions = {
    # Opening - Maynne’s Room
    
    # Lyra the Cat - First Interaction
    "Lyra": [
        ("Maynne", "Lyra! Hey buddy.", "speech"),
        ("Maynne", "Don't look at me like that. I fed you yesterday.", "speech"),
        ("Lyra", "*Meow*", "speech"),
        ("Maynne", "Okay, fine. I'll check your bowl.", "speech"),
    ],
    
    # LYRA THE CAT - Second Interaction
    "Lyra2": [
        ("Maynne", "I'll hang out with you when I get back, okay? I promise.", "speech"),
    ],
    
    # Backpack
    "Backpack":[
        ("Maynne", "Laptop. Notebook. Charger. Wallet. Keys?", "speech"),
        ("Maynne", "Keys. Great. I'm almost a functioning adult.", "speech"),
    ],
    
    # Flowers
    "Flowers": [
        ("Maynne", "These lilies are definitely dead.", "speech"),
        ("Maynne", "I should probably throw them out before Mom notices.", "speech"),
    ],
    
    # Flowers: Option A
    "Flowers_Throw": [
        ("Maynne", "There. One less thing to worry about.", "speech"),
    ],

    # Flowers: Option B
    "Flowers_Leave": [
        ("Maynne", "Nah, I'll do it later. I'm already done.", "speech"),
    ],
    
    # Leave
    "Leaving": [
        ("Maynne", "All right. Let's go before something else comes up.", "speech"),
    ],
    
    # Kitchen Conversation
    "Kitchen": [
        ("Mom", "Morning. You're up early.", "speech"),
        ("Maynne", "Define early.", "speech"),
        ("Mom", "You're not still in bed. I'll take it.", "speech"),
        ("Maynne", "I got class.", "speech"),
        ("Mom", "I know. I made you something to eat.", "speech"),
        ("Maynne", "Thanks Mom, but I'm kind of in a rush.", "speech"),
        ("Mom", "You always say that.", "speech"),
        ("Maynne", "Because I'm always in a rush.", "speech"),
        ("Mom", "There's food in the fridge if you change your mind. And please take something with you. You're no good to anyone when you're hungry.", "speech"),
        ("Maynne", "I'm fine. I promise...", "speech"),
        ("Mom", "You said that yesterday.", "speech"),
        ("Maynne", "I'll eat later. Okay?", "speech"),
        ("Mom", "Okay, Maynne.", "speech"),
    ],
    
    # Food
    "Food": [
        ("Maynne", "She actually made breakfast.", "think"),
        ("Maynne", "I could sit down for five minutes.", "think"),
    ],
    
    # Food Option A:
    "Food_Eat": [
        ("Maynne", "Okay, yeah. That's actually pretty good.", "speech"),
        ("Mom", "See? Was that difficult?", "speech"),
        ("Maynne", "Don't get used to it.", "speech"),
        ("Mom", "Wouldn't dream of it.", "speech"),
    ],
    
    # Food Option B:
    "Food_Leave": [
        ("Maynne", "I'll grab something on campus.", "speech"),
    ],
    
    # Lyra's Food Bowl:
    "LyraBowl": [
        ("Maynne", "Lyra, your food's right here.", "speech"),
        ("Maynne", "You're really living the life, you know that?", "speech"),
    ],
    
    # Leaving Kitchen
    "KitchenLeaving": [
        ("Mom", "Hey Maynne.", "speech"),
        ("Maynne", "Yeah?", "speech"),
        ("Mom", "Call me when you get a chance today, okay? I haven't heard much from you lately.", "speech"),
        ("Maynne", "Mom, I saw you last night.", "speech"),
        ("Mom", "I know. I just like hearing from you.", "speech"),
        ("Maynne", "Yeah. Okay. I'll call you.", "speech"),
        ("Mom", "Have a good day. Take care.", "speech"),
    ],
    
    # Leaving without engaging with Mom:
    "KitchenRush": [
        ("Mom", "Maynne? Your breakfast-", "speech"),
        ("Maynne", "I'll be fine. Love you!", "speech"),
        ("Mom", "Love you too.", "speech"),
    ],
    
    # Outside the house - Audra conversion
    "MeetAudra": [
        ("Audra", "Hey Maynne!", "speech"),
        ("Maynne", "Oh, hey! What are u doing here?", "speech"),
        ("Audra", "Waiting for the bus. Same as every other broke university student.", "speech"),
        ("Maynne", "Fair enough.", "speech"),
        ("Audra", "I texted you yesterday, by the way.", "speech"),
        ("Maynne", "Did you? Sorry, I probably missed it.", "speech"),
        ("Audra", "You missed the other three, too.", "speech"),
        ("Maynne", "Okay, when you say it like that, it sounds bad.", "speech"),
        ("Audra", "I'm not trying to make you feel bad.", "speech"),
        ("Audra", "I just haven't seen you at the study group in a while. And whenever I ask if you're coming, you say maybe.", "speech"),
        ("Maynne", "I've had a lot going on.", "speech"),
        ("Audra", "I know. We all do. I just miss hanging out with you. That's all.", "speech"),
    ],
    
    # Choice A: Apologize to Audra
    "Apologize_Audra": [
        ("Maynne", "You're right. I've been avoiding everyone, honestly. It's not your fault.", "speech"),
        ("Audra", "You don't have to tell me everything. I just want you around sometimes.", "speech"),
        ("Maynne", "Yeah. I'll try to come today.", "speech"),
        ("Audra", "Really?", "speech"),
        ("Maynne", "Yeah.", "speech"),
    ],
    
    # Choice B: Dismiss her (Audra)
    "Dimiss_Audra": [
        ("Maynne", "Audra, please. It's too early for this.", "speech"),
        ("Audra", "I'm literally just asking if you're okay.", "speech"),
        ("Maynne", "And I'm telling you I'm fine.", "speech"),
        ("Audra", "Right. Okay.", "speech"),
        ("Audra", "See you around, then.", "speech"),
    ],
    
    # Bus Stop
    "BusStop": [
        ("Maynne", "Bus should be here any second.", "think"),
        ("Maynne", "Come on. Come on.", "think"),
        ("Audra", "You could always walk with me to campus. It's not that far.", "speech"),
        ("Maynne", "And arrive late and sweaty? No thanks.", "speech"),
        ("Audra", "Your loss.", "speech"),
        ("Maynne", "See you there?, then.", "speech"),
        ("Audra", "Yeah. See you.", "speech"),
    ],
}

dialogueIndex = 0

mode = "main"

activeInteraction = None
interactionIndex = 0

lyra_interacted = False
flowers_removed = False
ate_breakfast = False
audra_response = None

# Choice Menu
choice = 0

# Interactions options
roomOptions = [
    "Interact with Lyra",
    "Check Backpack",
    "Look at Flowers",
    "Leave Bedroom"
]

kitchenOptions = [
    "Interact with food",
    "Check Lyra's food bowl",
    "Leave kitchen",
    "Rush out"
]

foodOptions = [
    "Eat something",
    "Leave without eating"
]

audraOptions = [
    "I'm sorry. I've been a terrible friend lately",
    "Can we not do this right now? I'm late."
]

clock = pygame.time.Clock()
running = True

def startInteraction(name):
    global mode, activeInteraction, interactionIndex
    
    activeInteraction = name
    interactionIndex = 0
    mode = "interaction"

def advanceDialogue():
    global dialogueIndex, interactionIndex
    global mode, activeInteraction
    global lyra_interacted, choice
    global ate_breakfast
    global audra_response
    
    if mode == "main":
        dialogueIndex += 1

        if dialogueIndex >= len(dialogue):
            mode = "room_menu"
            dialogueIndex = 0
            choice = 0
            
    elif mode == "interaction":
        interactionIndex += 1
        current_lines = interactions[activeInteraction]
        
        if interactionIndex >= len(current_lines):
            
            if activeInteraction == "Kitchen":
                mode = "kitchen_menu"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction == "Food":
                mode = "food_choice"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction == "Food_Eat":
                ate_breakfast = True
                mode = "kitchen_menu"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction == "Food_Leave":
                mode = "kitchen_menu"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction == "LyraBowl":
                mode = "kitchen_menu"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction == "KitchenLeaving":
                startInteraction("MeetAudra")
                return
            
            elif activeInteraction == "KitchenRush":
                startInteraction("MeetAudra")
                return
        
            if activeInteraction == "Lyra":
                lyra_interacted = True
            
            elif activeInteraction == "Flowers":
                mode = "flowers_choice"
                choice = 0
                return
            
            elif activeInteraction == "Leaving":
                startInteraction("Kitchen")
                return
            
            elif activeInteraction == "MeetAudra":
                mode = "audra_choice"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction in ("Apologize_Audra", "Dimiss_Audra"):
                startInteraction("BusStop")
                return
            
            elif activeInteraction == "BusStop":
                mode = "bus"
                activeInteraction = None
                return 
                                
            mode = "room_menu"
            activeInteraction = None
            choice = 0
        
def RoomOption(index):
        
    if index == 0:
        if lyra_interacted:
            startInteraction("Lyra2")
        else:
            startInteraction("Lyra")
    elif(index == 1):
        startInteraction("Backpack")
        
    elif(index == 2):
        startInteraction("Flowers")
    
    elif(index == 3):
        startInteraction("Leaving")
        
def flowerChoice(index):
    global flowers_removed
    
    if index == 0:
        flowers_removed = True
        startInteraction("Flowers_Throw")
        
    elif index == 1:
        flowers_removed = False
        startInteraction("Flowers_Leave")
        
def KitchenOption(index):
    if index == 0:
        startInteraction("Food")
        
    elif index == 1:
        startInteraction("LyraBowl")
        
    elif index == 2:
        startInteraction("KitchenLeaving")
        
    elif index == 3:
        startInteraction("KitchenRush")
        
def FoodOption(index):
    if index == 0:
        startInteraction("Food_Eat")
        
    elif index == 1:
        startInteraction("Food_Leave")
        
def AudraOption(index):
    global audra_response
    
    if index == 0:
        audra_response = "apologized"
        startInteraction("Apologize_Audra") 
    elif index == 1:
        audra_response = "dismissed"
        startInteraction("Dimiss_Audra")   

def drawMenu(options, heading):
    heading_surface = font.render(heading, True, DIALOGUE_COLOUR)
    canvas.blit(heading_surface, (25, 20))
    choiceRects = []
    
    choiceX = 25
    choiceY = 42
    choiceWidth = 270
    choiceHeight = 17
    choiceGap = 3
    
    for i, option in enumerate(options):
        rect = pygame.Rect(choiceX, choiceY + i * (choiceHeight + choiceGap), choiceWidth,choiceHeight)
        
        choiceRects.append(rect)
        
        if i == choice:
            bg_colour = (55, 43, 75)
            bonder_colour = (190, 165, 220)
            marker = ">"
        else:
            bg_colour = (25, 22, 35)
            bonder_colour = (100, 90, 120)
            marker = " "
        
        pygame.draw.rect(canvas, bg_colour, rect)
        pygame.draw.rect(canvas, bonder_colour, rect, 1)
        
        option_surface = font.render(marker + " " + option, True, DIALOGUE_COLOUR)
        canvas.blit(option_surface,(rect.x + 5, rect.y + 3))
        
    return choiceRects
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
            elif mode == "room_menu":
                if event.key == pygame.K_UP:
                    choice = (choice - 1) % len(roomOptions)
                    
                elif event.key == pygame.K_DOWN:
                    choice = (choice + 1) % len(roomOptions)
                    
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    RoomOption(choice)
                    choice = 0
                    
            elif mode == "flowers_choice":
                if event.key == pygame.K_UP:
                    choice = (choice - 1) % 2

                elif event.key == pygame.K_DOWN:
                    choice = (choice + 1) % 2
                    
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    flowerChoice(choice)
                    choice = 0
                    
            elif mode == "kitchen_menu":
                if event.key == pygame.K_UP:
                    choice = (choice - 1) % len(kitchenOptions)

                elif event.key == pygame.K_DOWN:
                    choice = (choice + 1) % len(kitchenOptions)

                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    KitchenOption(choice)
                    choice = 0
                    
            elif mode == "food_choice":
                if event.key == pygame.K_UP:
                    choice = (choice - 1) % len(foodOptions)
                    
                elif event.key == pygame.K_DOWN:
                    choice = (choice + 1) % len(foodOptions)
                    
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    FoodOption(choice)
                    choice = 0
            
            elif mode == "audra_choice":
                if event.key == pygame.K_UP:
                    choice = (choice - 1) % len(audraOptions)
                    
                elif event.key == pygame.K_DOWN:
                    choice = (choice + 1) % len(audraOptions)
                    
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    AudraOption(choice)
                    choice = 0
                    
            elif mode in ("main", "interaction"):
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    advanceDialogue()
                
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx = event.pos[0] // scale
                my = event.pos[1] // scale
                
                if mode == "room_menu":
                    rects = drawMenu(roomOptions, "What would you like to do?")
                    
                    for i, rect in enumerate(rects):
                        if rect.collidepoint(mx, my):
                            RoomOption(i)
                            choice = 0
                            break

            elif mode == "flowers_choice":
                rects = drawMenu(
                    ["Throw them away", "Leave them"],
                    "What should Maynne do?"
                )

                for i, rect in enumerate(rects):
                    if rect.collidepoint(mx, my):
                        flowerChoice(i)
                        choice = 0
                        break

            elif mode == "kitchen_menu":
                rects = drawMenu(
                    kitchenOptions,
                    "What would you like to do?"
                )

                for i, rect in enumerate(rects):
                    if rect.collidepoint(mx, my):
                        KitchenOption(i)
                        choice = 0
                        break

            elif mode == "food_choice":
                rects = drawMenu(
                    foodOptions,
                    "What should Maynne do?"
                )

                for i, rect in enumerate(rects):
                    if rect.collidepoint(mx, my):
                        FoodOption(i)
                        choice = 0
                        break
            
            elif mode == "audra_choice":
                rects = drawMenu(
                    audraOptions,
                    "How does Maynne respond?"
                )
                
                for i, rect in enumerate(rects):
                    if rect.collidepoint(mx, my):
                        AudraOption(i)
                        choice = 0
                        break

            elif mode in ("main", "interaction"):
                if arrowRect.collidepoint(mx, my):
                    advanceDialogue()

    canvas.fill((10, 9, 14))
    
    if mode == "main":
        speaker, line, dialogue_type = dialogue[dialogueIndex]
    elif mode == "interaction":
        current_lines = interactions[activeInteraction]
        speaker, line, dialogue_type = current_lines[interactionIndex]
        
    else:
        speaker = None
        line = None
        dialogue_type = None
        
    if mode in ("main", "interaction"):
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
        
    elif mode == "room_menu":
        canvas.blit(dialogueBox, (boxX, boxY))
        drawMenu(roomOptions, "What would you like to do?")
        
    elif mode == "flowers_choice":
        canvas.blit(dialogueBox, (boxX, boxY))
        drawMenu(
            ["Throw them away",
            "Leave them"],
            "What should Maynne do?"
        )
        
    elif mode == "kitchen_menu":
        canvas.blit(dialogueBox, (boxX, boxY))
        drawMenu(kitchenOptions, "What would you like to do?")
        
    elif mode == "food_choice":
        canvas.blit(dialogueBox, (boxX, boxY))        
        drawMenu(foodOptions, "What should Maynne do?")
        
    elif mode == "audra_choice":
        canvas.blit(dialogueBox, (boxX, boxY))        
        drawMenu(audraOptions, "How should Maynne respond?")
        
    elif mode == "bus":
        canvas.blit(dialogueBox, (boxX, boxY))
        end_text = font.render("The bus pulls away...", True, DIALOGUE_COLOUR)
        canvas.blit(end_text, (boxX + 12, boxY + 12))    

    scaled = pygame.transform.scale(canvas, screen.get_size())
    screen.blit(scaled, (0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()            