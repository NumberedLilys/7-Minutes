import pygame

# ==================Player initialization==============================
class Player(pygame.sprite.Sprite):
    def __init__(self, animations, x, y, screen_width):
        super().__init__()

        self.animations = animations
        self.screen_width = screen_width
        self.facing = "right"
        self.moving = False

        self.frame_index = 0
        self.frame_timer = 0
        self.frame_duration = 125   # ms per frame

        self.image = self.animations["idle_right"][0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

# ===============Updates based on player movement left/right===============
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.moving = False

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.facing = "left"
            self.moving = True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.facing = "right"
            self.moving = True

        if (keys[pygame.K_a] and keys[pygame.K_d]
                or keys[pygame.K_a] and keys[pygame.K_RIGHT]
                or keys[pygame.K_LEFT] and keys[pygame.K_d]
                or keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):

            self.moving = False

        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, self.screen_width)

        self.animate(dt)

    def animate(self, dt):
        state = "walk" if self.moving else "idle"
        frames = self.animations[f"{state}_{self.facing}"]

        self.frame_timer += dt
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.frame_index += 1

        self.frame_index %= len(frames)
        self.image = frames[self.frame_index]