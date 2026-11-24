import pygame

#Implimenting text_wrap 
def text_wrap(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

class DialogueManager:
    def __init__(self, font, box_image, nameplates, scale):
        self.font = font
        self.box_image = box_image
        self.nameplates = nameplates
        self.scale = scale
        self.choice_history = []

        self.dialogue_queue = []

        self.actions = {}

        self.active = False # True if dialogue box open, false if not
        self.tree = None # holds dictionary of modes (depending on conversation/text)
        self.current_node_id = None # tracks which dictionary key in self.tree is active on screen ("start", etc)
        self.selected_index = 0 # tracks which option player is on/choosing (0, 1, 2...)

        self.option_rects = [] # list to store clickble option hitboxes

    def start(self, tree, start_node="start"):
        self.tree = tree # loads dictionary text
        self.current_node_id = start_node # sets starting point with "start" default
        self.selected_index = 0 # resets starting index point
        self.active = True # sets dialogue to appear on screen

    def _select_option(self, index): # option selection, sets next node
        options = self.tree[self.current_node_id].get("options", []) # get list of options from dictionary

        if not options: # base case, if no options exit out of text box
            self._start_next()
            return

        selected_option = options[index]
        if "ending_entry" in selected_option and selected_option["ending_entry"] not in self.choice_history:
            self.choice_history.append(selected_option["ending_entry"])

        action = selected_option.get("action")

        if action:
            action()

        next_node = selected_option["next"] # find current option and find its next

        if next_node is None:
            self._start_next() # close text box if no next (None)
        else:
            self.current_node_id = next_node # set curerent node to next one
            self.selected_index = 0 # reset choice index

    def handle_event(self, event):
        if not self.active:
            return  # BASE CASE - Do nothing if dialogue box is closed 

        options = self.tree[self.current_node_id].get("options", [])

        if event.type == pygame.MOUSEMOTION: # finding where mouse is hovering
            for i in range(len(self.option_rects)):
                if self.option_rects[i].collidepoint(
                    (event.pos[0] / self.scale, event.pos[1] / self.scale)
                ):
                    self.selected_index = i

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # if click using mouse
            for i in range(len(self.option_rects)):
                if self.option_rects[i].collidepoint(
                    (event.pos[0] / self.scale, event.pos[1] / self.scale)
                ):
                    self._select_option(i)
                    return

        elif event.type == pygame.KEYDOWN:
            if not options: # base case
                return

            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(options)

            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(options)

            elif event.key in (pygame.K_RETURN, pygame.K_SPACE): # if enter or space bar, select option
                self._select_option(self.selected_index)

 # ================ Dialogue queue to avoid overwriting ================
    def queue(self, tree, start_node="start"):
        self.dialogue_queue.append((tree, start_node)) # appending the next dialogue to queue 

        if not self.active:
            self._start_next()

    def _start_next(self):
        if self.dialogue_queue:
            tree, start_node = self.dialogue_queue.pop(0)
            self.start(tree, start_node)
        else:
            self.active = False

    # ============= drawing to screen =============

    def draw(self, surface):
        if not self.active: # base case, close text box if no text
            return

        node = self.tree[self.current_node_id] # set current node from dictionary
        screen_w, screen_h = surface.get_size()
        box_w, box_h = 280, 50 # was 280, 50
        box_rect = pygame.Rect(
            (surface.get_width() - box_w) // 2,
            surface.get_height() - box_h - 115,
            box_w,
            box_h,
        )
        surface.blit(self.box_image, box_rect)

        speaker_key = node.get("speaker") # get matching name
        if speaker_key in self.nameplates:
            plate_img = self.nameplates[speaker_key]
            name_rect = plate_img.get_rect(
                topleft=(box_rect.left + 8, 
                         box_rect.top - plate_img.get_height() + 8) # 4
                         ) # estimated numbers
            
            surface.blit(plate_img, name_rect) # draw nameplate over top left of text box
        padding = 8
        text_x = box_rect.left + padding
        text_y = box_rect.top + 12 # 12
        line_height = self.font.get_linesize()
        text_lines = text_wrap(node["text"], self.font, box_w - padding * 2)

        #text_lines is a list of wrapped strings from above functino
        #enumerate goes through that list and provides each line's index and text
        #text_surface is the drawable piece of text surface.blit can display 
        
        for line_number, line in enumerate(text_lines):
            text_surface = self.font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (text_x, text_y + line_number * line_height))

        # ============ TEXT OPTIONS =============
        self.option_rects = []
        options = node.get("options", []) or [] # get all options for current node/text in dictionary
        options_start_y = text_y + len(text_lines) * line_height + 2
        line_spacing = line_height + 1

        for i in range(len(options)): # go through each option
            option = options[i] # current option 
            is_selected = (i == self.selected_index) # shows which option player is on
            prefix = "> " if is_selected else "   " 
            color = (255, 225, 110) if is_selected else (200, 200, 200) # highlighting for visual cue

            opt_surf = self.font.render(prefix + option["text"], True, color) # set up text
            opt_rect = opt_surf.get_rect(topleft=(text_x + 15, options_start_y + i * line_spacing)) # hitbox area

            click_rect = opt_rect.inflate(20, 8) # creates larger clickable area than text (+10 on either x, +4 on either y)
            self.option_rects.append(click_rect) # saves each option hitbox to list in order

            surface.blit(opt_surf, opt_rect) # prints each option onto screen