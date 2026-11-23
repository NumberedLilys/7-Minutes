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
    
    # University 
    "UniArrival": [
        ("Maynne", "Made it Barely.", "think"),
        ("Maynne", "Okay, Class is this way. Study room upstairs.", "think"),
        ("Maynne", "Where am I going again?", "think"),
        ("Maynne", "Professor doing the review today. I really should go.", "think"),
        ("Maynne", "But Audra wanted me to study today.", "think"),
        ("Maynne", "I can't do both, can I?", "think"),
    ],
    
    # Choice A: Attend Class
    "AttendClass": [
        ("Maynne", "Okay, Focus.", "think"),
        ("Audra", "Are you coming to the study group?", "speech"),
        ("Maynne", "Sorry, Audra. Class comes first today.", "think"),
    ],
    
    
    # Choice B: Join the Study Group
    "StudyGroup": [
        ("Audra", "You actually came!", "speech"),
        ("Maynne", "Don't make it a big deal.", "speech"),
        ("Audra", "Come on, help me with this question.", "speech"),
        ("Maynne", "Alright, let's see.", "speech"),
    ],
    
    # University Hallway
    "PhoneCall": [
        ("Maynne", "Mom?", "think"),
        ("Maynne", "Didn't I tell her I'd call her later?", "think"),
    ],
    
    # Choice A: Pick up the phone
    "PhonePickUp": [
        ("Maynne", "Hey Mom.", "speech"),
        ("Mom", "Hey, sweetheart. Just checking in. How's your day?", "speech"),
        ("Maynne", "It's okay. Just heading out of class.", "speech"),
        ("Mom", "Have you eaten?", "speech"),
        ("Maynne", "Yes Mom. I'm fine.", "speech"),
        ("Mom", "Okay. Don't stay out too late. Love you.", "speech"),
        ("Maynne", "Love you too. I'll see you later.", "speech"),
        ("Maynne", "She's always checking up on me.", "think")
    ],
    
    # Choice B: Ignore the call
    "PhoneIgnore": [
        ("Maynne", "I'll call her back when I get home.", "think"),
        ("Mom", "Call me when you can.", "speech"),
        ("Maynne", "Yeah, later.", "think"),
    ],
    
    # Strange Events - Hallway
    "HallwayScare": [
        ("Maynne", "What was that?", "speech"),
        ("Maynne", "Okay... that's weird.", "speech"),
        ("Maynne", "Hello? Is someone there?", "speech"),
        ("Maynne", "What the hell!", "speech"),
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
university_choice = None
phone_choice = None 
mom_rushed = False

# Death Menu
deathDialogue = []
deathIndex = 0

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

universityOptions = [
    "Attend Class",
    "Join the Study Group"
]

phoneOptions = [
    "Pick up", 
    "Ignore the call"
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
    global university_choice
    global phone_choice
    
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
                startInteraction("UniArrival")
                return 
            
            elif activeInteraction == "UniArrival":
                mode = "university_choice"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction in ("AttendClass", "StudyGroup"):
                startInteraction("PhoneCall")
                return
            
            elif activeInteraction in ("PhoneCall"):
                mode = "phone_choice"
                activeInteraction = None
                choice = 0
                return
            
            elif activeInteraction in ("PhonePickUp", "PhoneIgnore"):
                startInteraction("HallwayScare")
                return
            
            elif activeInteraction in ("HallwayScare"):
                mode = "hallway_run"
                activeInteraction = None
                choice = 0
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
    global mom_rushed
    
    if index == 0:
        startInteraction("Food")
        
    elif index == 1:
        startInteraction("LyraBowl")
        
    elif index == 2:
        mom_rushed = False
        startInteraction("KitchenLeaving")
        
    elif index == 3:
        mom_rushed = True
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
        
def UniversityOption(index):
    global university_choice
    
    if index == 0:
        university_choice = "class"
        startInteraction("AttendClass")
        
    elif index == 1:
        university_choice = "study_group"
        startInteraction("StudyGroup")

def PhoneOption(index):
    global phone_choice
    
    if index == 0:
        phone_choice = "answered"
        startInteraction("PhonePickUp")
        
    elif index == 1:
        phone_choice = "ignored"
        startInteraction("PhoneIgnore")
        
def buildDeathDialogue():
    # Create only the regerts caused by Maynne's actual harmful choices. 
    
    lines = [
        ("Maynne", "What?", "speech"),
        ("Death", "Someone you've been running out of time with.", "speech"),
        ("Maynne", "Who... who are you?", "speech"),
        ("Death", "You've been in such a hurry all day.", "speech"),
        ("Maynne", "I need to get home.", "speech"),
        ("Death", "Do you?", "speech"),
    ]
    
    # Regret 1: Lyra's death
    if not flowers_removed:
        lines.extend([
            ("Lyra", "*Meow*", "speech"),
            ("Maynne", "Lyra? What are you doing here?", "speech"),
            ("Maynne", "Hey buddy. Come here.", "speech"),
            ("Death", "Do you remember the flowers in your room?", "speech"),
            ("Maynne", "What? The lilies?", "speech"),
            ("Death", "You noticed they were dying.", "speech"),
            ("Maynne", "Yeah…I was going to throw them out.", "speech"),
            ("Death", "But you didn't.", "speech"),
            ("Maynne", "Wait...", "speech"),
            ("Death", "Lyra ate them while you were away.", "speech"),
            ("Maynne", "No...", "speech"),
            ("Death", "Lilies are poisonous to cats, Maynne. By the time anyone noticed, it was too late.", "speech"),
            ("Maynne", "NO, NO, NO!. She wouldn't have…", "speech"),
            ("Maynne", "I was going to throw them away. I just…I thought I'd do it later.", "speech"),
            ("Maynne", "She was waiting for me to come home, wasn't she?", "speech"),
            ("Death", "Perhaps.", "speech"),
            ("Maynne", "I promised I would play with her when I got back.", "speech"),
            ("Lyra", "*Meow*", "speech"),
            ("Maynne", "Lyra, wait! Please...", "speech"),
        ])
        
    # Regret 2: Dismissing Audra (Friendship)
    if audra_response == "dismissed":
        lines.extend([
            ("Audra", "I just miss hanging out with you. That's all.", "speech"),
            ("Maynne", "Audra...?", "speech"),
            ("Death", "She reached out to you. She texted you. She waited for you. She tried to make plans with you.", "speech"),
            ("Maynne", "I was busy. I had school and other things going on.", "speech"),
            ("Death", "She wasn't asking too much, Maynne. She just wanted you to be there.", "speech"),
            ("Maynne", "I didn't mean to hurt her.", "speech"),
            ("Death", "Do you remember what you told her?", "speech"),
            ("Maynne", "Can we not do this right now? I'm late.", "speech"),
            ("Maynne", "I was stressed. I didn't mean it like that.", "speech"),
            ("Death", "She was only trying to be there for you.", "speech"),
            ("Maynne", "I know… I should've listened.", "speech"),
        ])
        
    # Regret 3: Kitchen Rush 
    if mom_rushed:
        lines.extend([
            ("Mom", "Have a good day, honey. Take care.", "speech"),
            ("Maynne", "Mom...", "speech"),
            ("Death", "You were in such a hurry this morning.", "speech"),
            ("Maynne", "I had to get to class.", "speech"),
            ("Death", "She wanted to spend a little more time with you. You barely stopped to talk.", "speech"),
            ("Maynne", "I did say I loved her.", "speech"),
            ("Death", "You did. But you though there would always be another morning.", "speech"),
            ("Maynne", "I wanted to see her again.", "speech"),
        ])
            
    # Regret 4: Ignore Mom's Phone Call
    if phone_choice == "ignored":
        lines.extend([
            ("Maynne", "No...", "speech"),
            ("Death", "Your mother tried to reach you.", "speech"),
            ("Maynne", "What are you talking about?", "speech"),
            ("Death", "She needed you.", "speech"),
            ("Mom", "Maynne, it's Mom. Lyra isn't feeling very well. She's been acting strange, and I'm getting worried. Can you call me back?", "speech"),
            ("Maynne", "Lyra...?", "speech"),
            ("Death", "Your mother was worried about her.", "speech"),
            ("Maynne", "Why didn't she call again?", "speech"),
            ("Death", "She did. There was another missed call.", "speech"),
            ("Maynne", "No... I didn't know she was sick!", "speech"),
            ("Death", "You thought the call could wait.", "speech"),
            ("Maynne", "I should've picked up...", "speech"),
        ])
            
    elif phone_choice == "answered":
        lines.extend([
            ("Mom", "Maynne? Thank goodness. Lyra isn't feeling very well. She's been acting strange, and I'm getting worried.", "speech"),
            ("Maynne", "I remember that call...", "speech"),
            ("Death", "You heard that something was wrong. You wanted to go home.", "speech"),
            ("Maynne", "I should've gone straight home.", "speech"),
            ("Death", "You tried to get there. But the day had already run out.", "speech"),
        ])
            
    lines.extend([
        ("Maynne", "Mom...?", "speech"),
        ("Death", "She made dinner. She made your favourite.", "speech"),
        ("Maynne", "I was supposed to be home.", "speech"),
        ("Death", "She waited for the sound of the door opening.", "speech"),
        ("Maynne", "Please stop.", "speech"),
        ("Maynne", "I just want to go home.", "speech"),
        ("Death", "Then why are you still here?", "speech"),
        ("Maynne", "Because I want to see them. I want everything to go back to normal.", "speech"),
        ("Death", "Nobody knows their time will come.", "speech"),
        ("Maynne", "I wasn't ready. I still had plans. I still had things I wanted to do.", "speech"),
        ("Death", "It's not your regerts that define your life.", "speech"),
        ("Maynne", "Then why does it feel like I've already lost everything?", "speech"),
        ("Death", "Maynne, look at me.", "speech"),
        ("Death", "You still matter.", "speech"),
        ("Mom", "Love you, sweetheart. Take care.", "speech"),
        ("Audra", "Same time next week?.", "speech"),
        ("Maynne", "...I miss them.", "speech"),
    ])
    
    if not flowers_removed: 
        lines.append(
            ("Maynne", "I'm sorry, Mom. I'm sorry Lyra. I'm sorry Audra.", "speech")
        )
    else:
        lines.append(
            ("Maynne", "I'm sorry, Mom. I'm sorry Audra.", "speech") 
        )
    lines.extend([
        ("Maynne", "I'm sorry, everyone.", "speech"),
        ("Mom", "Maynne? Please call me when you see this.", "speech"),  
    ])
        
    return lines
    
def startDeathScene():
    global mode, deathDialogue, deathIndex
    deathDialogue = buildDeathDialogue()
    deathIndex = 0
    mode = "death"
    
def advanceDeathDialogue():
    global deathIndex, mode
    deathIndex += 1
    
    if deathIndex >= len(deathDialogue):
        mode = "finished"

def drawMenu(options, heading):
    heading_surface = font.render(heading, True, DIALOGUE_COLOUR)
    canvas.blit(heading_surface, (25, 87))
    choiceRects = []
    
    choiceX = 25
    choiceY = 104
    choiceWidth = 270
    choiceHeight = 14
    choiceGap = 2
    
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
        canvas.blit(option_surface,(rect.x + 5, rect.y + 1))
        
    return choiceRects

def getMenuOptions():
    if mode == "room_menu":
        return roomOptions
    
    elif mode == "flowers_choice":
        return ["Throw them away", "Leave them"]
    
    elif mode == "kitchen_menu":
        return kitchenOptions
    
    elif mode == "food_choice":
        return foodOptions
    
    elif mode == "audra_choice":
        return audraOptions
    
    elif mode == "university_choice":
        return universityOptions
    
    elif mode == "phone_choice":
        return phoneOptions
    
    return None  

def getMenuRect(options):
    choiceX = 25
    choiceY = 104
    choiceWidth = 270
    choiceHeight = 14
    choiceGap = 2
    
    return[
        pygame.Rect(choiceX, choiceY + i * (choiceHeight + choiceGap), choiceWidth, choiceHeight)
        for i in range(len(options))
    ]   
    
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
                    
            elif mode == "university_choice":
                if event.key == pygame.K_UP:
                    choice = (choice - 1) % len(universityOptions)
                    
                elif event.key == pygame.K_DOWN:
                    choice = (choice + 1) % len(universityOptions)
                    
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    UniversityOption(choice)
                    choice = 0
            
            elif mode == "phone_choice":
                if event.key == pygame.K_UP:
                    choice = (choice - 1) % len(phoneOptions)
                    
                elif event.key == pygame.K_DOWN:
                    choice = (choice + 1) % len(phoneOptions)
                    
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    PhoneOption(choice)
                    choice = 0
                    
            elif mode == "hallway_run":
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    startDeathScene()
                    
            elif mode == "death":
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    advanceDeathDialogue()
                    
            elif mode in ("main", "interaction"):
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    advanceDialogue()
                
        

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx = event.pos[0] // scale
                my = event.pos[1] // scale
                
                if mode in ("main", "interaction", "death"):
                    advanceDialogue() if mode != "death" else advanceDeathDialogue()
                
                elif mode == "hallway_run":
                    startDeathScene()
                
                else:
                    options = getMenuOptions()
                
                    if options is not None:
                        rects = getMenuRect(options)
                        
                        for i, rect in enumerate(rects):
                            if rect.collidepoint(mx, my):
                                choice = i
                                
                                if mode == "room_menu":
                                    RoomOption(i)
                                    
                                elif mode == "flowers_choice":
                                    flowerChoice(i)
                                    
                                elif mode == "kitchen_menu":
                                    KitchenOption(i)
                                    
                                elif mode == "food_choice":
                                    FoodOption(i)
                                
                                elif mode == "audra_choice":
                                    AudraOption(i)
                                
                                elif mode == "university_choice":
                                    UniversityOption(i)
                                
                                elif mode == "phone_choice":
                                    PhoneOption(i)
                                    
                                choice = 0
                                break

    canvas.fill((10, 9, 14))
    
    if mode == "main":
        speaker, line, dialogue_type = dialogue[dialogueIndex]
    elif mode == "interaction":
        current_lines = interactions[activeInteraction]
        speaker, line, dialogue_type = current_lines[interactionIndex]
    elif mode == "death":
        speaker, line, dialogue_type = deathDialogue[deathIndex]
        
    else:
        speaker = None
        line = None
        dialogue_type = None
        
    if mode in ("main", "interaction", "death"):
        if dialogue_type == "think":
            text_colour = THINK_COLOUR
        else:
            text_colour = DIALOGUE_COLOUR

        canvas.blit(dialogueBox, (boxX, boxY))

        if dialogue_type == "speech":
            canvas.blit(nameplates.get(speaker, nameplates["Blank"]), (nameplateX, nameplateY))

        text_lines = textWrap(line, font, dialogueBox.get_width() - 24)

        text_x = boxX + 12
        text_y = boxY + 12
        line_height = font.get_linesize()

        for i, text_line in enumerate(text_lines):
            text_surface = font.render(text_line, True, text_colour)
            canvas.blit(text_surface, (text_x, text_y + i * line_height))

        canvas.blit(arrow, (arrowX, arrowY))
        
    elif mode == "room_menu":
        drawMenu(roomOptions, "What would you like to do?")
        
    elif mode == "flowers_choice":
        drawMenu(
            ["Throw them away",
            "Leave them"],
            "What should Maynne do?"
        )
        
    elif mode == "kitchen_menu":
        drawMenu(kitchenOptions, "What would you like to do?")
        
    elif mode == "food_choice":
        drawMenu(foodOptions, "What should Maynne do?")
        
    elif mode == "audra_choice":
        drawMenu(audraOptions, "How should Maynne respond?")
        
    elif mode == "bus":
        end_text = font.render("The bus pulls away...", True, DIALOGUE_COLOUR)
        canvas.blit(end_text, (boxX + 12, boxY + 12))
        
    elif mode == "university_choice":
        drawMenu(universityOptions, "Where should Maynne go?") 
    
    elif mode == "phone_choice":
        drawMenu(phoneOptions, "Answer the phone?")
        
    elif mode == "hallway_run":
        end_text = font.render("Maynne runs for her life..", True, DIALOGUE_COLOUR)
        canvas.blit(end_text, (boxX + 12, boxY + 12))   
        end_text = font.render("Press SPACE to continue", True, DIALOGUE_COLOUR)
    
    elif mode == "finished":
        end_text = font.render("THE END!", True, DIALOGUE_COLOUR)
        canvas.blit(end_text, (boxX + 12, boxY + 12))   

    scaled = pygame.transform.scale(canvas, screen.get_size())
    screen.blit(scaled, (0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()            