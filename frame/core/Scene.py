#!/usr/bin/python3

import pygame

from .Renderer import Renderer
from .EventHandler import EventHandler
from .Timer import Timer


class Scene:

    def __init__(self, game_objects_list, bg_material):
        """
        The most important role for the scene is to contain the game objects
        :param game_objects_list:
        """
        self.game_objects_list = game_objects_list
        self.colliders_map = {}
        self.bg_material = bg_material
        self.scene_over = False

    def start(self):
        """
        This method starts the game objects, timer and event manager
        """

        # Running all the starts

        for game_object in self.game_objects_list:
            game_object.start()

        EventHandler.handle_events(pygame.event.get())
        Timer.register_frame()
        Renderer.render_background(self.bg_material)

    def update(self):
        """
        This method runs all the updates in a frame
        """

        # Running all updates

        Renderer.render_background(self.bg_material)

        self.game_objects_list.sort(key=lambda gm_obj: gm_obj.transform.layer)

        EventHandler.handle_events(pygame.event.get())

        # Running collisions

        for game_object in self.colliders_map:
            collider = self.colliders_map[game_object]
            collider.collisions_list = [gm_obj for gm_obj in self.colliders_map if self.colliders_map[gm_obj]
                                        is not collider and collider.is_colliding(self.colliders_map[gm_obj])]

        # Running draws and updates

        for game_object in self.game_objects_list:
            game_object.update()
            game_object.draw()

        Timer.register_frame()

        pygame.display.flip()

        # Exception for too much game objects in the scene

        if len(self.game_objects_list) >= 3000:
            raise Exception("Too many game objects in the scene.")
        if len(self.colliders_map) >= 100:
            raise Exception("Too many colliders in the scene")

    def loop(self):
        """
        This is the game loop for each scene
        """

        while not self.scene_over:
            self.update()

            if EventHandler.quit:
                self.exit()
                return "exit_game"

        self.exit()

    def add_game_object(self, game_object):
        """
        This method add a game object to the game object list
        :param game_object:
        """

        game_object.start()

        self.game_objects_list.append(game_object)

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
