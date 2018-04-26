#!/usr/bin/python3

from frame import *
from random import randint
from structure.game_objects.main_objects.enemies.BasicEnemy import BasicEnemy
from structure.game_objects.main_objects.enemies.Enemy1 import Enemy1
from structure.game_objects.main_objects.enemies.Enemy2 import Enemy2
from structure.game_objects.main_objects.enemies.Enemy3 import Enemy3
from structure.game_objects.main_objects.enemies.Meteor1 import Meteor1
from structure.game_objects.main_objects.enemies.Meteor2 import Meteor2

class EnemyGenerator(GameObject):
    def __init__(self):
        """

        :param transform:
        """
        super().__init__(Transform(Vector2(0, 0)))

        self.wait = 0
        self.wait2 = 0
        self.wait3 = 0
        self.wait4 = 0
        self.wait5 = 0

    def start(self):
        pass

    def update(self):
        a = randint(40, 600)
        b = -70
        c = randint(55, 510)
        d = -90
        e = randint(55, 510)
        f = -60
        if self.wait < Timer.get_current_time():

            SceneManager.get_current_scene().add_game_object(Enemy1(Transform(Vector2(a, b))))
            SceneManager.get_current_scene().add_game_object(Enemy1(Transform(Vector2(a + 30, b + 30))))
            SceneManager.get_current_scene().add_game_object(Enemy1(Transform(Vector2(a + 60, b + 60))))
            SceneManager.get_current_scene().add_game_object(Enemy1(Transform(Vector2(a + 90, b + 90))))
            SceneManager.get_current_scene().add_game_object(Enemy1(Transform(Vector2(a + 120, b + 120))))
            SceneManager.get_current_scene().add_game_object(Enemy1(Transform(Vector2(a + 150, b + 150))))
            self.wait = Timer.get_current_time() + randint(1, 2) * 5

        if Timer.get_current_time()> 6:
            if self.wait2 < Timer.get_current_time():
                SceneManager.get_current_scene().add_game_object(Enemy2(Transform(Vector2(c, d))))
                SceneManager.get_current_scene().add_game_object(Enemy2(Transform(Vector2(c + 40, d - 40))))
                SceneManager.get_current_scene().add_game_object(Enemy2(Transform(Vector2(c - 40, d - 40))))
                self.wait2 = Timer.get_current_time() + randint(1, 2) * 3


        if Timer.get_current_time() > 10:
            if self.wait3 < Timer.get_current_time():
                SceneManager.get_current_scene().add_game_object(Enemy3(Transform(Vector2(e, f))))
                SceneManager.get_current_scene().add_game_object(Enemy3(Transform(Vector2(e + 50, f + 50))))
                self.wait3 = Timer.get_current_time() + randint(1, 2) * 3

        if self.wait4 < Timer.get_current_time():
            SceneManager.get_current_scene().add_game_object(Meteor1(Transform(Vector2(randint(55, 510), b))))
            self.wait4 = Timer.get_current_time() + randint(1, 2) * 3

        if self.wait5 < Timer.get_current_time():
            SceneManager.get_current_scene().add_game_object(Meteor2(Transform(Vector2(randint(55, 510), b))))
            self.wait5 = Timer.get_current_time() + randint(1, 2) * 3

    def draw(self):
        pass
