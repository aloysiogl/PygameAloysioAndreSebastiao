#!/usr/bin/python3

import pygame
import sys


class SceneManager:

    scenes_list = []
    current_scene_index = 0

    @classmethod
    def add_scene(cls, scene):
        """
        Add a scene in the scenes list
        :param scene:
        """

        cls.scenes_list.append(scene)

    @classmethod
    def next_scene(cls):
        """
        Go to next scene
        """

        if cls.current_scene_index < len(cls.scenes_list):
            cls.get_current_scene().end()
            cls.current_scene_index += 1
            cls.run_current_scene()

        else:
            cls.exit_game()

    @classmethod
    def get_current_scene(cls):
        """
        Gives the current running scene
        :return:
        """

        return cls.scenes_list[cls.current_scene_index]

    @classmethod
    def run_current_scene(cls):
        """
        Go to next scene
        """

        current_scene = cls.get_current_scene()

        current_scene.start()
        exit_code = current_scene.loop()

        if exit_code == "exit_game":
            cls.exit_game()

    @classmethod
    def exit_game(cls):
        """
        Finishes the game
        """

        pygame.quit()
        sys.exit()
