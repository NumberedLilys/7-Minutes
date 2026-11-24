import pygame
from Audio import audio

def text_wrap(text, font, max_width):
    # Measure with the actual font so wrapping accounts for glyph widths rather
    # than assuming every character takes the same amount of space.
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

            # Keep normal words intact; only break a word when it is wider than
            # the entire available line by itself.
            if font.size(word)[0] <= max_width:
                current_line = word
                continue

            # Build a too-wide word character by character, flushing each
            # segment as soon as adding another character would exceed max_width.
            # Split unusually long words so no rendered line exceeds the box width.
            current_line = ""
            for character in word:
                if current_line and font.size(current_line + character)[0] > max_width:
                    lines.append(current_line)
                    current_line = character
                else:
                    current_line += character

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
        audio.play_dialogue_line(tree[start_node].get("speaker"))

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
            audio.play_dialogue_line(self.tree[next_node].get("speaker"))

    def handle_event(self, event):
        if not self.active:
            return  # BASE CASE - Do nothing if dialogue box is closed 

        options = self.tree[self.current_node_id].get("options", [])

        if event.type == pygame.MOUSEMOTION: # finding where mouse is hovering
            for i in range(len(self.option_rects)):
                if self.option_rects[i].collidepoint(
                    (event.pos[0] / self.scale, event.pos[1] / self.scale)
                ):
                    if self.selected_index != i:
                        audio.play_sound("click")
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
                audio.play_sound("click")

            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(options)
                audio.play_sound("click")

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
        box_w, box_h = 280, 50 # was 280, 50
        padding = 8
        text_top_padding = 12
        line_height = self.font.get_linesize()
        text_lines = text_wrap(node["text"], self.font, box_w - padding * 2)

        options = node.get("options", []) or []
        # Choices are indented inside the box. Reserve space for both that indent
        # and the selection marker before wrapping their text.
        text_x_offset = padding + 15
        option_width = box_w - padding - text_x_offset
        prefix_width = self.font.size("   ")[0]
        wrapped_options = [
            text_wrap(option["text"], self.font, option_width - prefix_width)
            for option in options
        ]
        # Leave a small gap between successive rendered lines within an option.
        line_spacing = line_height + 1

        # Calculate the height from wrapped text and choices before drawing.
        # This lets the background grow with the content while keeping the
        # original 50-pixel height for short dialogue.
        options_height = sum(len(lines) * line_spacing for lines in wrapped_options)
        if options:
            options_height += 2
        content_height = (
            text_top_padding
            + len(text_lines) * line_height
            + options_height
            + padding
        )
        box_h = max(box_h, content_height)
        screen_h = surface.get_height()
        # Keep the original position for short dialogue. As the box grows, move
        # it upward only as far as needed, while reserving room for the nameplate.
        box_top = min(screen_h - box_h - 8, screen_h - 50 - 115)
        box_top = max(8, box_top)

        box_rect = pygame.Rect(
            (surface.get_width() - box_w) // 2,
            box_top,
            box_w,
            box_h,
        )
        # Stretch the existing artwork to the measured height without changing its width.
        stretched_box = pygame.transform.scale(self.box_image, box_rect.size)
        surface.blit(stretched_box, box_rect)

        speaker_key = node.get("speaker") # get matching name
        if speaker_key in self.nameplates:
            plate_img = self.nameplates[speaker_key]
            # Keep the plate overlapping the box as before, but clamp its top to
            # the screen so tall dialogue cannot push it out of view.
            name_rect = plate_img.get_rect(
                topleft=(box_rect.left + 8, 
                         max(0, box_rect.top - plate_img.get_height() + 8)) # 4
                         ) # estimated numbers
            
            surface.blit(plate_img, name_rect) # draw nameplate over top left of text box
        text_x = box_rect.left + padding
        text_y = box_rect.top + text_top_padding

        for line_number, line in enumerate(text_lines):
            text_surface = self.font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (text_x, text_y + line_number * line_height))

        # ============ TEXT OPTIONS =============
        self.option_rects = []
        options = node.get("options", []) or [] # get all options for current node/text in dictionary
        options_start_y = text_y + len(text_lines) * line_height + 2

        # Give each choice a hitbox spanning all of its wrapped lines.
        for i, option in enumerate(options):
            is_selected = i == self.selected_index
            prefix = "> " if is_selected else "   "
            color = (255, 225, 110) if is_selected else (200, 200, 200)
            option_x = text_x + 15
            option_y = options_start_y
            option_lines = wrapped_options[i]

            self.option_rects.append(
                pygame.Rect(
                    option_x,
                    option_y,
                    option_width,
                    len(option_lines) * line_spacing,
                )
            )

            for line_number, line in enumerate(option_lines):
                line_prefix = prefix if line_number == 0 else "   "
                option_surface = self.font.render(line_prefix + line, True, color)
                surface.blit(
                    option_surface,
                    (option_x, option_y + line_number * line_spacing),
                )

            options_start_y += len(option_lines) * line_spacing