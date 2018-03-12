from frame.core.GameObject import GameObject
from frame.components.meshes.CircularMesh import CircularMesh
from frame.components.Material import Material
from frame.core.Representations import Color
from frame.components.Transform import Transform
from pygame.math import Vector2


class Test(GameObject):

    def __init__(self):
        super().__init__(Transform(Vector2(100, 33), 1, 1, 0))
        self.mesh = CircularMesh(100, Material(Color.white))

    def start(self):
        pass

    def update(self):
        self.transform.position+=Vector2(0, 1)
        pass

    def draw(self):
        self.mesh.render(self.transform)
