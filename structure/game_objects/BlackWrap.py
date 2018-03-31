from frame import *

class BlackWrap(GameObject):

    def __init__(self, transform):
        super().__init__(Transform(transform))
        # Black wrap
        self.mesh1 = PolygonalMesh([Vector2(0, 3), Vector2(300, 3), Vector2(300, 8), Vector2(0, 8)],
                                   Material(Color.black))
        self.mesh2 = PolygonalMesh([Vector2(0, 8), Vector2(5, 8), Vector2(5, 38), Vector2(0, 38)],
                                   Material(Color.black))
        self.mesh3 = PolygonalMesh([Vector2(295, 8), Vector2(300, 8), Vector2(300, 38), Vector2(295, 38)],
                                   Material(Color.black))
        self.mesh4 = PolygonalMesh([Vector2(0, 38), Vector2(300, 38), Vector2(300, 43), Vector2(0, 43)],
                                   Material(Color.black))

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.mesh1.render(self.transform)
        self.mesh2.render(self.transform)
        self.mesh3.render(self.transform)
        self.mesh4.render(self.transform)