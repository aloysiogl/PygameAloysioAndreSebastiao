#!/usr/bin/python3

from frame import *
from frame.core.Representations import Screen
from random import randint


class ReverseStar(GameObject):

    def __init__(self, transform):
        """
        The star is the basic element of the background animation
        :param transform: the transform relations for the star
        """
        super().__init__(transform)

        self.mesh = PolygonalMesh([Vector2(0, 0), Vector2(0, 150), Vector2(2, 150), Vector2(2, 0)], Material(Color.white))

        self.mesh.set_center_pivot()

        self.speed = randint(5, 20)

        self.alpha = 255

        self.factor = randint(1, 10)

    def start(self):
        pass

    def update(self):
        """
        Update for moving star (high speed animation)
        """

        self.speed *= 1 + self.factor*0.01

        if 0 < self.transform.position.y/640*255 < 255:
            self.alpha = (640-self.transform.position.y)/640*255

        self.transform.layer = -10

        self.transform.position += Timer.get_dt() * self.speed * Vector2(0, 1)

        if self.transform.position.y > Screen.height:
            self.destroy()

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh.render(self.transform, mode='Filled', alpha=self.alpha)
