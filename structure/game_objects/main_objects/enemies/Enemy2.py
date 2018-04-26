#!/usr/bin/python3

from frame import *
from random import randint


class Enemy2(GameObject):

    def __init__(self, transform):
        """
        The Enemy is the character that the Player have to destroy
        :param initial_pos: the position of the character
        """
        super().__init__(transform)
        self.mesh = PolygonalMesh([Vector2(0,540), Vector2(540,0), Vector2(-540, 0)], Material(Color.blue))

        self.mesh2 = PolygonalMesh([Vector2(0,380), Vector2(380,0), Vector2(-380,0)], Material(Color.medium_blue))
        self.mesh3 = PolygonalMesh([Vector2(300, 120), Vector2(270, 120), Vector2(270, -20), Vector2(300,-20),
                                    Vector2(300,120)], Material(Color.white))
        self.mesh4 = PolygonalMesh([Vector2(-300, 120), Vector2(-270, 120), Vector2(-270, -20), Vector2(-300, -20),
                                    Vector2(-300, 120)], Material(Color.white))
        self.mesh5 = PolygonalMesh([Vector2(50,300),Vector2(100,220), Vector2(100,150), Vector2(-100,150),
                                    Vector2(-100,220), Vector2(-50,300)], Material(Color.light_blue))

        self.collider = MeshCollider(self.mesh, self.transform)

        self.wait = 0

        self.vectx = 1.5
        self.vecty = 2
        self.radius = randint(10, 70)
        self.transform.scale=0.055

    def start(self):
        self.add_collider(self.collider)

    def update(self):
        self.transform.position += Vector2(self.vectx, self.vecty)

        #if self.transform.position.y - self.radius < 0:
        #    self.destroy()

        if self.transform.position.y + self.radius > 640:
            self.destroy()

        if self.transform.position.x - self.radius < 0:
            self.vectx = -self.vectx

        if self.transform.position.x + self.radius > 640:
            self.vectx = -self.vectx

        for x in self.collider.collisions_list:
            if x.__class__.__name__ == "Player":
                self.destroy()

            if x.__class__.__name__ == "MainShot":
                x.destroy()
                next(x for x in SceneManager.get_current_scene().game_objects_list if x.__class__.__name__ == "CurrentScore").add_score(15)
                self.destroy()

            if x.__class__.__name__ == "Enemy2" and self.wait < Timer.get_current_time():
                self.vectx = -self.vectx
                self.vecty = -self.vecty
                self.wait = Timer.get_current_time() + 0.05

    def draw(self):
        self.mesh.render(self.transform)
        self.mesh2.render(self.transform)
        self.mesh3.render(self.transform)
        self.mesh4.render(self.transform)
        self.mesh5.render(self.transform)

