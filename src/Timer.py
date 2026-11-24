class GameTimer:
    def __init__(self, minute_total = 7):
        self.duration_ms = minute_total * 60 * 1000

        self.elapsed_ms = 0 # amount of gameplay time

        self.speed = 1.0 # timer speed (quickly drains in final room)

        self.paused = False
        self.finished = False

        self.events = [] # timed events

    def add_event(self, minutes = 0, seconds = 0, callback = None):
        trigger_ms = (minutes * 60 + seconds) * 1000 # time of event trigger

        if callback:
            self.events.append([trigger_ms, callback, False]) # if final boolean is true, event has passed

    def update(self, dt): # dt real time that has passed
        if self.paused or self.finished: # base case
            return

        self.elapsed_ms += dt * self.speed # increase elapsed game time based on timer speed

        self.elapsed_ms = min(self.elapsed_ms, self.duration_ms) # prevent timer from exceeding total time (7 mins)

        # Check timed events
        for event in self.events:
            trigger_ms, callback, triggered = event

            if not triggered and self.elapsed_ms >= trigger_ms:
                event[2] = True # event passed/occurred, not triggered again
                callback()

        if self.elapsed_ms >= self.duration_ms: # checking if time is run out
            self.finished = True

    def get_remaining_ms(self):
            return max(0, self.duration_ms - self.elapsed_ms) # max to prevent negative time

    def get_countdown(self): # for printing onto game screen
        remaining = int(self.get_remaining_ms() / 1000)

        minutes = remaining // 60
        seconds = remaining % 60

        return f"{minutes:01}:{seconds:02}"

    def set_speed(self, multiplier):
        self.speed = max(0, multiplier)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False