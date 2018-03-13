#!/usr/bin/python3

import pygame
from .Renderer import Renderer
from .Scene import Scene
from .SceneManager import SceneManager
from ..components import Material
from .Representations import Color
from .Representations import Screen
from structure.Test import Test


class Core:
    @classmethod
    def start(cls, name, scenes_list):
        """
        Start the game (initialize pygame)
        :param name:
        :param scenes_list:
        """

        pygame.init()
        cls.game_display = pygame.display.set_mode((Screen.width, Screen.height))
        pygame.display.set_caption(name)

        Renderer.set_display(cls.game_display)

        # Test code TODO
        SceneManager.add_scene(Scene([], Material(Color.red)))
        obj = Test()
        SceneManager.get_current_scene().add_game_object(obj)
        SceneManager.run_current_scene()

    @classmethod
    def quit(cls):
        """
        Quits the game
        """

