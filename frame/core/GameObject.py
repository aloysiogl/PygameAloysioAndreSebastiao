#!/usr/bin/python3

import abc


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
