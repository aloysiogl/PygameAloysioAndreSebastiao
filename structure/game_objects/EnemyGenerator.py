#!/usr/bin/python3

from frame import *
from random import randint
from .BasicEnemy import BasicEnemy


class EnemyGenerator(GameObject):
    def __init__(self):
        """

        :param transform:
        """
        super().__init__(Transform(Vector2(0, 0)))

        self.wait = 0

    def start(self):
        pass

    def update(self):

        if self.wait < Timer.get_current_time():
            SceneManager.get_current_scene().add_game_object(BasicEnemy(Transform(Vector2(randint(55, 510), randint(55, 320)))))

            self.wait = Timer.get_current_time() + randint(1, 2)*0.5

    def draw(self):
        pass
