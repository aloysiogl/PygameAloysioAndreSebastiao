#!/usr/bin/python3

from frame import *
from random import randint


class Meteor1(GameObject):

    def __init__(self, transform):
        """
        The Meteor is the obstacles that de Player have to avoid
        :param initial_pos: the position of the character
        """
        super().__init__(transform)
        self.mesh = PolygonalMesh([Vector2(0, -300), Vector2(200, -250), Vector2(300, 0), Vector2(100, 150),
                                   Vector2(0, 100), Vector2(-150,300), Vector2(-250,0)],
                                  Material(Color.white))

        self.collider = MeshCollider(self.mesh, self.transform)

        self.wait = 0

        self.vectx = randint(0, 0)
        self.vecty = randint(1, 5)
        self.radius = randint(10, 70)
        self.transform.scale= randint(3, 10) * 0.01

        self.rotation_speed = randint(1, 10)
        self.transform.rotation = randint (0, 180)

    def start(self):
        self.add_collider(self.collider)

    def update(self):
        self.transform.rotation += self.rotation_speed * Timer.get_dt() * 25
        self.transform.position += Vector2(self.vectx, self.vecty)

        #if self.transform.position.y - self.radius < 0:
        #    self.destroy()

        if self.transform.position.y + self.radius > 640:
            self.destroy()

        if self.transform.position.x - self.radius < 0:
            self.vectx = -self.vectx

        if self.transform.position.x + self.radius > 640:
            self.vectx = -self.vectx

        for x in self.collider.collisions_list:
            if x.__class__.__name__ == "Player":
                self.destroy()

            if x.__class__.__name__ == "MainShot":
                x.destroy()
                next(x for x in SceneManager.get_current_scene().game_objects_list if x.__class__.__name__ == "CurrentScore").add_score(30)
                self.destroy()

            if x.__class__.__name__ == "Meteor1" and self.wait < Timer.get_current_time():
                self.vectx = -self.vectx
                self.vecty = -self.vecty
                self.wait = Timer.get_current_time() + 0.05

    def draw(self):
        self.mesh.render(self.transform)


