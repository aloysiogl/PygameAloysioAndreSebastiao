#!/usr/bin/python3

from frame import *


class ScoreText(GameObject):

    def __init__(self, vector):
        """
        The score text
        :param : the position for the text
        """
        super().__init__(Transform(vector, 0, scale=40))

        self.mesh_scores = TextMesh("Scores", Font.space_font, Material(Color.white))

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh_scores.render(Transform(Vector2(self.transform.position+Vector2(-210, 0)), 0, self.transform.scale*2))
