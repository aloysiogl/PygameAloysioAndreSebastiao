#!/usr/bin/python3

import pygame
import sys

from .Renderer import Renderer
from .EventHandler import EventHandler


class Scene:

    def __init__(self, game_objects_list, bg_material):
        """
        The most important role for the scene is to contain the game objects
        :param game_objects_list:
        """
        self.game_objects_list = game_objects_list
        self.bg_material = bg_material
        self.scene_over = False

    def start(self):
        #TODO setup timer and event manager
        """
        This method starts the game objects, timer and event manager
        """

        # Running all the starts

        for game_object in self.game_objects_list:
            game_object.start()

        EventHandler.handle_events(pygame.event.get())
        Renderer.render_background(self.bg_material)

    def update(self):
        """
        This method runs all the updates in a frame
        """

        # Running all updates

        for game_object in self.game_objects_list:
            game_object.update()

        EventHandler.handle_events(pygame.event.get())
        Renderer.render_background(self.bg_material)

    def loop(self):
        """
        This is the game loop for each scene
        """

        while not self.scene_over:
            self.update()
            pygame.display.flip()

            #TODO remove this
            if EventHandler.quit:
                pygame.quit()
                sys.exit()

        self.exit()

    def end(self):
        """
        This method gets the scene ready to be over
        """

        self.scene_over = True

    def exit(self):
        """
        This is the destructor for the scene
        """

        self.game_objects_list = []
