#!/usr/bin/python3

from frame import *


class EnemyShot(GameObject):

    def __init__(self, transform):
        """
        The main shot is the most simple shot for the player
        :param transform: the transform relations for the shot
        """
        super().__init__(transform)

        self.mesh = PolygonalMesh([Vector2(0, 0), Vector2(0, 15), Vector2(5, 15), Vector2(5, 0)], Material(Color.pink))

        self.mesh.set_center_pivot()

        self.collider = MeshCollider(self.mesh, self.transform, [])

        self.speed = 1200

    def start(self):
        """
        Adding the collider to the scene
        """

        self.add_collider(self.collider)

    def update(self):
        """
        Update for moving the projectile
        """

        self.transform.position += Timer.get_dt() * self.speed * Vector2(0, 1)

        if self.transform.position.y > 640:
            self.destroy()

        for x in self.collider.collisions_list:
            if x.__class__.__name__ == "Player":
                self.destroy()

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh.render(self.transform)
