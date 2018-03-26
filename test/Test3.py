from frame import *


class Test3(GameObject):

    def __init__(self, transform):
        super().__init__(Transform(transform))
        self.transform.scale = 10
        self.mesh = PolygonalMesh([Vector2(0, 0), Vector2(10,0), Vector2(10,10), Vector2(5,15)], Material(Color.yellow))
        self.collider = MeshCollider(self.mesh, self.transform)

    def start(self):
        self.add_collider(self.collider)
        pass

    def update(self):
        pass

    def draw(self):
        self.mesh.render(self.transform)
        self.collider.render_colliding_outline()