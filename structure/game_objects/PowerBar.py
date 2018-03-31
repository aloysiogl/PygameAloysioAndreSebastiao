from frame import *

class PowerBar(GameObject):

    def __init__(self, transform, player):
        super().__init__(Transform(transform))
        # Red bar
        self.mesh = PolygonalMesh([Vector2(5, 8), Vector2(295, 8), Vector2(295, 38), Vector2(5, 38)],
                                  Material(Color.blue))

        self.player = player

    def start(self):
        pass

    def update(self):
        if self.player.turret is not 'right':
            self.transform.position += Timer.get_dt() * Vector2(30, 0)

    def draw(self):
        self.mesh.render(self.transform)
