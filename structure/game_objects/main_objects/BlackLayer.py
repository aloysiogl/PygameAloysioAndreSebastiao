from frame import *

class BlackLayer(GameObject):

    def __init__(self, transform):
        super().__init__(Transform(transform))
        # Black Layer
        self.mesh = PolygonalMesh([Vector2(0, 0), Vector2(300, 0), Vector2(300, 40), Vector2(0, 40)], Material(Color.black))
        self.transform.layer = 2

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.mesh.render(self.transform)