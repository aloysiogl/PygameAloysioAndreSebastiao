#!/usr/bin/python3

from frame import *


class MenuText(GameObject):

    def __init__(self, vector):
        """
        The game name
        :param : the position for the text
        """
        super().__init__(Transform(vector, 0, scale=50))

        self.mesh_infinity = TextMesh("Infinity", Font.space_font, Material(Color.white))
        self.mesh_shooter = TextMesh("Shooter", Font.space_font, Material(Color.white))

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh_infinity.render(Transform(Vector2(self.transform.position+Vector2(-240, 0)), 0, self.transform.scale*2))
        self.mesh_shooter.render(Transform(Vector2(self.transform.position+Vector2(-160, 70)), 0, self.transform.scale))
