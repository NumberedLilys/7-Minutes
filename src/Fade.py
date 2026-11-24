import pygame

class Fade:
    def __init__(self, width, height, duration=2000):
        self.surface = pygame.Surface((width, height))
        self.surface.fill((0, 0, 0))

        self.duration = duration
        self.elapsed = 0

        self.active = False
        self.finished = False

    def start(self):
        self.active = True
        self.finished = False
        self.elapsed = 0

    def update(self, dt):
        if not self.active or self.finished:
            return

        self.elapsed += dt

        if self.elapsed >= self.duration:
            self.elapsed = self.duration
            self.finished = True

    def draw(self, screen):
        if not self.active:
            return

        opacity = int((self.elapsed / self.duration) * 255)
        self.surface.set_alpha(opacity)
        screen.blit(self.surface, (0, 0))