from frame import *

class LifeBar(GameObject):

    def __init__(self, transform, test):
        super().__init__(Transform(transform))
        # Red bar
        self.mesh = PolygonalMesh([Vector2(5, 8), Vector2(295, 8), Vector2(295, 38), Vector2(5, 38)],
                                   Material(Color.red))

        self.test = test

    def start(self):
        pass

    def update(self):
        if len(self.test.collider.collisions_list) > 0:
            print("OI")
            self.transform.position -= Timer.get_dt() * 10 * Vector2(0.5, 0)


    def draw(self):
        self.mesh.render(self.transform)
