#!/usr/bin/python3

import abc
from .SceneManager import SceneManager


class GameObject:

    def __init__(self, transform):
        """
        Every game object must be associated with a position rotation and scale
        :param transform: the transform quantities for the object
        """
        self.transform = transform

    @abc.abstractmethod
    def start(self):
        """
        This method runs once the object is instantiated
        """
        pass

    @abc.abstractmethod
    def update(self):
        """
        This method runs each frame
        """
        pass

    @abc.abstractmethod
    def draw(self):
        """
        This codes draws the game object in the screen
        """
        pass

    def add_collider(self, collider):
        """
        This code places the collider in the scene
        :param collider: the collider to be added in the scene
        """

        SceneManager.get_current_scene().colliders_map[self] = collider

    def destroy(self):
        """
        This code destroys the game object
        """
        if self in SceneManager.get_current_scene().game_objects_list:
            SceneManager.get_current_scene().game_objects_list.remove(self)
        if hasattr(self, 'collider'):
            if self in SceneManager.get_current_scene().colliders_map:
                del SceneManager.get_current_scene().colliders_map[self]
