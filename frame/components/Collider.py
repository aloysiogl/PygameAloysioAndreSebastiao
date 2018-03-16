#!/usr/bin/python3

import abc


class Collider:
    def __init__(self, transform, collisions_list):
        """
        The collider needs a transform and a list of collisions
        :param transform: the transform of the collider
        :param collisions_list: the list of game objects colliding to my collider
        """

        self.transform = transform
        self.collisions_list = collisions_list

    @abc.abstractmethod
    def is_colliding(self, collider):
        """
        Says if a collider is colliding with another collider
        :param collider: the collider to test the collision
        :return: if it's colliding
        """

        pass
