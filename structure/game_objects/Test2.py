from frame import *
from pygame.math import Vector2


class Test2(GameObject):

    def __init__(self, transform):
        super().__init__(transform)
        self.mesh = CircularMesh(10, Material(Color.yellow))

    def start(self):
        pass

    def update(self):
        self.transform.position-= Vector2(0,1)*Timer.get_dt()*1000
        if self.transform.position.y < 0:
            SceneManager.get_current_scene().game_objects_list.remove(self)


    def draw(self):
        self.mesh.render(self.transform)