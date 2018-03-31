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

        self.direction = True

        # Animation parameters

        self.alpha = 0

        self.speed = 70

    def start(self):
        pass

    def update(self):
        """
        Running blinking animation
        """

        if self.direction:
            self.alpha +=self.speed*Timer.get_dt()
            self.speed *= 1.01
            if self.alpha >=250:
                self.alpha = 250
                self.direction = not self.direction
        else:
            self.alpha -= self.speed * Timer.get_dt()
            self.speed /= 1.01
            if self.alpha <= 40:
                self.alpha = 40
                self.direction = not self.direction
        pass

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh_text.render(Transform(Vector2(self.transform.position+Vector2(-240, 0)), 0, self.transform.scale),
                                alpha=self.alpha)
