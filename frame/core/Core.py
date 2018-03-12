#!/usr/bin/python3

import pygame
from .Renderer import Renderer
from .Scene import Scene
from ..components import Material
from .Representations import Color


class Core:
    width = 640
    heigth = 640

    @classmethod
    def start(cls, name, scenes_list):
        """
        Start the game (initialize pygame)
        :param name:
        :param scenes_list:
        """

        pygame.init()
        cls.game_display = pygame.display.set_mode((cls.width, cls.heigth))
        pygame.display.set_caption(name)

        Renderer.set_display(cls.game_display)

        # Test code TODO
        scene = Scene([], Material(Color.red))
        scene.start()
        scene.loop()

    @classmethod
    def quit(cls):
        """
        Quits the game
        """

