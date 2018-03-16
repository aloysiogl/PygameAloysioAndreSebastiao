from frame import *
from pygame.math import Vector2


class Test2(GameObject):

    def __init__(self, transform):
        super().__init__(transform)
        self.mesh = CircularMesh(10, Material(Color.yellow))
        self.collider = MeshCollider(self.mesh, self.transform)

    def start(self):
        self.add_collider(self.collider)

    def update(self):
        self.transform.position -= Vector2(0, 1) * Timer.get_dt() * 1000
        if self.transform.position.y < 0:
            self.destroy()

    def draw(self):
        self.mesh.render(self.transform)
