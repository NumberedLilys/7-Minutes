import pygame

class DialogueManager:
    def __init__(self, font, box_image, nameplates):
        self.font = font
        self.box_image = box_image
        self.nameplates = nameplates

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
            self.active = False
            return

        next_node = options[index]["next"] # find current option and find its next
        if next_node is None:
            self.active = False # close text box if no next (None)
        else:
            self.current_node_id = next_node # set curerent node to next one
            self.selected_index = 0 # reset choice index

    def handle_event(self, event):
        if not self.active:
            return  # BASE CASE - Do nothing if dialogue box is closed 

        options = self.tree[self.current_node_id].get("options", [])

        if event.type == pygame.MOUSEMOTION: # finding where mouse is hovering
            for i in range(len(self.option_rects)):
                if self.option_rects[i].collidepoint(event.pos):
                    self.selected_index = i

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # if click using mouse
            for i in range(len(self.option_rects)):
                if self.option_rects[i].collidepoint(event.pos):
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

    def draw(self, surface):
        if not self.active: # base case, close text box if no text
            return

        node = self.tree[self.current_node_id] # set current node from dictionary
        screen_w, screen_h = surface.get_size() # automatically adjust text box based on screen size

        box_rect = self.box_image.get_rect(midbottom=(screen_w // 2, screen_h - 30)) # draw text box near bottom of screen
        surface.blit(self.box_image, box_rect)

        speaker_key = node.get("speaker") # get matching name
        if speaker_key in self.nameplates:
            plate_img = self.nameplates[speaker_key]
            name_rect = plate_img.get_rect(topleft=(box_rect.left + 30, box_rect.top - 25)) # estimated numbers
            surface.blit(plate_img, name_rect) # draw nameplate over top left of text box

        text_x = box_rect.left + 45
        text_y = box_rect.top + 45
        text_surf = self.font.render(node["text"], True, (255, 255, 255)) # draw dialogue in textbox
        surface.blit(text_surf, (text_x, text_y))

        # ============ TEXT OPTIONS =============
        self.option_rects = []
        options = node.get("options", []) or [] # get all options for current node/text in dictionary
        options_start_y = text_y + 45 # starting y value to list options
        line_spacing = 32

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