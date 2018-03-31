#!/usr/bin/python3

from frame import *
from random import randint


class Meteor2(GameObject):

    def __init__(self, initial_pos):
        """
        The Meteor is the obstacles that de Player have to avoid
        :param initial_pos: the position of the character
        """
        super().__init__(Transform(initial_pos))
        self.mesh = PolygonalMesh([Vector2(0, -150), Vector2(200, -100),
                                   Vector2(0,400), Vector2(-400, 150), Vector2(-100,20)],
                                   Material(Color.white))

        self.collider = MeshCollider(self.mesh, self.transform)

        self.wait = 0

        self.vectx = randint(-5, 5)
        self.vecty = randint(-5, 5)
        self.radius = randint(10, 70)
        self.transform.scale=0.08

    def start(self):
        self.add_collider(self.collider)

    def update(self):
        self.transform.position += Vector2(self.vectx, self.vecty)

        if self.transform.position.y - self.radius < 0:
            self.vecty = -self.vecty

        if self.transform.position.y + self.radius > 640:
            self.vecty = -self.vecty

        if self.transform.position.x - self.radius < 0:
            self.vectx = -self.vectx

        if self.transform.position.x + self.radius > 640:
            self.vectx = -self.vectx

        for x in self.collider.collisions_list:
            if x.__class__.__name__ == "MainShot":
                x.destroy()
                self.destroy()
            if x.__class__.__name__ == "Meteor2" and self.wait < Timer.get_current_time():
                self.vectx = -self.vectx
                self.vecty = -self.vecty
                self.wait = Timer.get_current_time() + 0.05

    def draw(self):
        self.mesh.render(self.transform)


