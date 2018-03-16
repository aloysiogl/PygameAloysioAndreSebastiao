from frame import *


class Test3(GameObject):

    def __init__(self, transform):
        super().__init__(Transform(transform))
        self.mesh = CircularMesh(100, Material(Color.yellow))
        self.collider = MeshCollider(self.mesh, self.transform)

    def start(self):
        self.add_collider(self.collider)
        pass

    def update(self):
        pass

    def draw(self):
        # self.mesh.render(self.transform)
        self.collider.render_colliding_outline()