#!/usr/bin/python3

from frame import *
from assets.GameSounds import Music


class MenuController(GameObject):

    def __init__(self):
        """
        Controller for the game menu
        """
        super().__init__(Transform(Vector2(0, 0)))

    def start(self):
        """
        Menu initial configurations
        """

        SoundPlayer.play_music(Music.menu_scene, -1)

    def update(self):
        if EventHandler.key_space:
            SoundPlayer.fade_out()
            SceneManager.next_scene()

    def draw(self):
        pass
