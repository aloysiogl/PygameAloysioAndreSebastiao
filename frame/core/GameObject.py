#!/usr/bin/python3

import abc
from .SceneManager import SceneManager


class GameObject:

    def __init__(self, transform):
        """
        Every game object must be associated with a position rotation and scale
        :param transform:
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
        """

        SceneManager.get_current_scene().colliders_map[self] = collider

    def destroy(self):
        """
        This code destroys the game object
        """

        SceneManager.get_current_scene().game_objects_list.remove(self)
        if hasattr(self, 'collider'):
            del SceneManager.get_current_scene().colliders_map[self]
