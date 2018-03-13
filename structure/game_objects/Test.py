from frame import *
from pygame.math import Vector2


class Test(GameObject):

    def __init__(self):
        super().__init__(Transform(Vector2(100, 33), 1, 1, 0))
        self.mesh = CircularMesh(100, Material(Color.blue))

    def start(self):
        pass

    def update(self):
        if EventHandler.key_up:
            self.transform.position -= Timer.get_dt()*500*Vector2(0, 1)
        if EventHandler.key_down:
            self.transform.position += Timer.get_dt()*500*Vector2(0, 1)
        if EventHandler.key_left:
            self.transform.position -= Timer.get_dt()*500*Vector2(1, 0)
        if EventHandler.key_right:
            self.transform.position += Timer.get_dt()*500*Vector2(1, 0)

    def draw(self):
        self.mesh.render(self.transform)
