#!/usr/bin/python3

from frame import *


class StartText(GameObject):

    def __init__(self, vector):
        """
        The game name
        :param : the starting position for the player
        """
        super().__init__(Transform(vector, 0, scale=50))

        self.mesh_text = TextMesh("Press space!", Font.space_font, Material(Color.white))

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh_text.render(Transform(Vector2(self.transform.position+Vector2(-240, 0)), 0, self.transform.scale))
