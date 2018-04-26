#!/usr/bin/python3

from frame import *
from frame.core.Representations import Screen
from random import randint
from .ReverseStar import ReverseStar


class ReverseStarCreator(GameObject):
    def __init__(self):
        """
        Initializing base object class
        """
        super().__init__(Transform(Vector2(0, 0)))

        self.wait = 0

    def start(self):
        pass

    def update(self):

        if self.wait < Timer.get_current_time():
            SceneManager.get_current_scene().add_game_object(ReverseStar(Transform(Vector2(randint(10, Screen.width-10
                                                                                                  ), -200))))

            self.wait = Timer.get_current_time() + randint(1, 4)*0.05

    def draw(self):
        pass
