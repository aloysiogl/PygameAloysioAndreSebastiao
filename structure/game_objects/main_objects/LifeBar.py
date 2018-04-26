from frame import *

class LifeBar(GameObject):

    def __init__(self, transform, player):
        super().__init__(Transform(transform))
        # Red bar
        self.mesh = PolygonalMesh([Vector2(5, 8), Vector2(295, 8), Vector2(295, 38), Vector2(5, 38)],
                                   Material(Color.red))

        self.player = player

    def start(self):
        pass

    def update(self):
        for x in self.player.collider.collisions_list:
            if x.__class__.__name__ == "Enemy1" or x.__class__.__name__ == "Enemy2" or x.__class__.__name__ == "Enemy3" or x.__class__.__name__ == "Meteor1" or x.__class__.__name__ == "Meteor2":
                self.transform.position -= Vector2(1, 0)
        if self.transform.position[0] < -290:
            self.transform.position = (0, 0)

    def draw(self):
        self.mesh.render(self.transform)
