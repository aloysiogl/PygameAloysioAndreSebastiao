#!/usr/bin/python3

import pygame
from .Renderer import Renderer
from .SceneManager import SceneManager
from .Representations import Screen


class Core:
    @classmethod
    def start(cls, name):
        """
        Start the game (initialize pygame)
        :param name: the game name
        """

        pygame.init()
        cls.game_display = pygame.display.set_mode((Screen.width, Screen.height))
        pygame.display.set_caption(name)

        Renderer.set_display(cls.game_display)

        SceneManager.run_current_scene()
