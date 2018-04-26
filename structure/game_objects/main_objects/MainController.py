#!/usr/bin/python3

from frame import *
from assets.GameSounds import Music


class MainController(GameObject):

    def __init__(self):
        """
        Controller for the game high level actions
        """
        super().__init__(Transform(Vector2(0, 0)))

        self.wait_time = 3
        self.begin_time = 0
        self.music_started = False

    def start(self):
        """
        Initial configurations
        """

        self.begin_time = Timer.get_current_time()

    def update(self):
        # Starting the game music
        if Timer.get_current_time() > self.begin_time + self.wait_time and not self.music_started:
            SoundPlayer.play_music(Music.main_scene, -1)
            self.music_started = True

    def draw(self):
        pass
