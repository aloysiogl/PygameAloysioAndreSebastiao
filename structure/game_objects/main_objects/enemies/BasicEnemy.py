#!/usr/bin/python3

from frame import *
from random import randint


class BasicEnemy(GameObject):
    def __init__(self, transform):
        """

        :param transform:
        """
        super().__init__(transform)

        self.vectx = randint(-5, 5)
        self.vecty = randint(-5, 5)

        self.radius = randint(10, 70)

        self.mesh = CircularMesh(self.radius, Material(Color.yellow))

        self.collider = MeshCollider(self.mesh, self.transform)

        self.wait = 0

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
            if x.__class__.__name__ == "BasicEnemy" and self.wait < Timer.get_current_time():
                self.vectx = -self.vectx
                self.vecty = -self.vecty
                self.wait = Timer.get_current_time() + 0.05

    def draw(self):
        self.mesh.render(self.transform)