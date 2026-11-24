from Objects import Object

class Character(Object):
    def __init__(self, name, animation, x, y, frame_duration=150):
        super().__init__(
            name,
            animation[0],
            x,
            y
        )

        self.animation = animation
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_duration = frame_duration

    def update(self, dt):
        if not self.visible:
            return

        self.frame_timer += dt

        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            self.frame_index += 1

        self.frame_index %= len(self.animation)

        self.image = self.animation[self.frame_index]