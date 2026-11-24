"""Game audio. Everything needed is in this file.

    from Audio import audio

    audio.play_music("start")           start screen and loading screen
    audio.play_ambience("bedroom")      when a scene or room begins (safe to call every frame)
    audio.play_dialogue_line(speaker)   when a new dialogue line appears
    audio.play_sound("click")           when a menu option is moved or picked

Music and ambience loop until the next scene begins.
Scene names: bedroom, living_room, kitchen, outside, bus, hallway, study, death.

To add a sound: put the file in assets/audio and add a line to SOUNDS.
Credits are in assets/audio/CREDITS.md.
"""

import pathlib
import re

import pygame

AUDIO_DIR = pathlib.Path(__file__).parent.parent / "assets" / "audio"
AUDIO_EXTENSIONS = (".wav", ".mp3", ".ogg", ".flac")

# name: (file, volume from 0 to 1)
SOUNDS = {
    "start": ("Start screen and loading.mp3", 0.5),
    "morning": ("Morning ambience.wav", 0.2),
    "outdoor": ("Outdoor ambience.wav", 0.6),
    "bus": ("Inside bus.wav", 0.6),
    "hallway": ("Hallway.wav", 0.3),
    "study": ("Quiet study.wav", 0.5),
    "death": ("Death.wav", 0.4),
    "lyra": ("Lyra noises.wav", 0.5),
    "click": ("Click and textbox.flac", 0.6),
    "textbox": ("Click and textbox.flac", 0.3),
}

SCENE_AMBIENCE = {
    "bedroom": "morning",
    "living_room": "morning",
    "kitchen": "morning",
    "outside": "outdoor",
    "bus": "bus",
    "hallway": "hallway",
    "study": "study",
    "death": "death",
}


def simplify(name):
    return re.sub(r"[\s_\-]+", " ", name).strip().lower()


class AudioManager:
    def __init__(self):
        self.enabled = False
        self.volume = 1.0
        self.loaded = {}
        self.warned = set()
        self.current_music = None
        self.current_ambience = None

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.set_num_channels(16)
            pygame.mixer.set_reserved(2)
            self.ambience_channels = [pygame.mixer.Channel(0), pygame.mixer.Channel(1)]
            self.active_ambience = 0
            self.enabled = True
        except pygame.error as error:
            print(f"Audio disabled: {error}")

    def find_file(self, name):
        filename, _ = SOUNDS[name]
        exact = AUDIO_DIR / filename
        if exact.exists():
            return exact

        wanted = simplify(pathlib.Path(filename).stem)
        if AUDIO_DIR.exists():
            for path in AUDIO_DIR.iterdir():
                if path.suffix.lower() in AUDIO_EXTENSIONS and simplify(path.stem) == wanted:
                    return path

        if name not in self.warned:
            self.warned.add(name)
            print(f"[audio] no file found for '{name}' (looking for {filename})")
        return None

    def get_sound(self, name):
        if not self.enabled:
            return None
        if name not in self.loaded:
            path = self.find_file(name)
            sound = None
            if path:
                try:
                    sound = pygame.mixer.Sound(str(path))
                except pygame.error as error:
                    print(f"[audio] could not load {path.name}: {error}")
            if sound:
                sound.set_volume(SOUNDS[name][1] * self.volume)
            self.loaded[name] = sound
        return self.loaded[name]

    def play_music(self, name, fade_ms=1000):
        if not self.enabled or name == self.current_music:
            return
        self.current_music = name
        path = self.find_file(name)
        if path:
            try:
                pygame.mixer.music.load(str(path))
                pygame.mixer.music.set_volume(SOUNDS[name][1] * self.volume)
                pygame.mixer.music.play(-1, fade_ms=fade_ms)
            except pygame.error as error:
                print(f"[audio] could not play {path.name}: {error}")

    def stop_music(self, fade_ms=1000):
        if self.enabled:
            self.current_music = None
            pygame.mixer.music.fadeout(fade_ms)

    def play_ambience(self, scene, fade_ms=1500):
        if not self.enabled:
            return
        if scene not in SCENE_AMBIENCE:
            if scene not in self.warned:
                self.warned.add(scene)
                print(f"[audio] no ambience set for scene '{scene}'")
            return

        name = SCENE_AMBIENCE[scene]
        if name == self.current_ambience:
            return
        self.current_ambience = name

        self.stop_music(fade_ms)
        self.ambience_channels[self.active_ambience].fadeout(fade_ms)

        sound = self.get_sound(name)
        if sound:
            self.active_ambience = 1 - self.active_ambience
            self.ambience_channels[self.active_ambience].play(sound, loops=-1, fade_ms=fade_ms)

    def stop_ambience(self, fade_ms=1500):
        if self.enabled:
            self.current_ambience = None
            self.ambience_channels[self.active_ambience].fadeout(fade_ms)

    def play_sound(self, name):
        sound = self.get_sound(name)
        if sound:
            sound.play()

    def play_dialogue_line(self, speaker):
        self.play_sound("lyra" if speaker == "Lyra" else "textbox")

    def set_volume(self, level):
        self.volume = level
        for name, sound in self.loaded.items():
            if sound:
                sound.set_volume(SOUNDS[name][1] * level)
        if self.enabled and self.current_music:
            pygame.mixer.music.set_volume(SOUNDS[self.current_music][1] * level)

    def stop_all(self, fade_ms=1000):
        self.stop_music(fade_ms)
        self.stop_ambience(fade_ms)


audio = AudioManager()