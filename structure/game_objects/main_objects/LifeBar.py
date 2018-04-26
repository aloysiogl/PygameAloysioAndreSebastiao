from frame import *

class LifeBar(GameObject):

    def __init__(self, transform, player):
        super().__init__(Transform(transform))
        # Red bar
        self.mesh = PolygonalMesh([Vector2(5, 8), Vector2(295, 8), Vector2(295, 38), Vector2(5, 38)],
                                   Material(Color.red))

        self.player = player
        self.transform.layer = 3

    def start(self):
        pass

    def update(self):
        for x in self.player.collider.collisions_list:
            if x.__class__.__name__ == "Enemy1":
                self.transform.position -=  Vector2(29, 0)
            elif x.__class__.__name__ == "Enemy2":
                self.transform.position -= Vector2(2*29, 0)
            elif x.__class__.__name__ == "Enemy3":
                self.transform.position -= Vector2(3*29, 0)
            elif x.__class__.__name__ == "Meteor1":
                self.transform.position -= Vector2(4*29, 0)
            elif x.__class__.__name__ == "Meteor2":
                self.transform.position -= Vector2(4*29, 0)

        if self.transform.position[0] < -290:
            self.transform.position = (0, 0)
            SceneManager.next_scene()

    def draw(self):
        self.mesh.render(self.transform)
