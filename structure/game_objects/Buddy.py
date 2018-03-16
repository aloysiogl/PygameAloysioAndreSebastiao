from frame import *
from .Test2 import Test2


class Buddy(GameObject):
    def __init__(self, transform, pai):
        self.parent_transform = transform
        self.dx = Vector2(100,0)
        super().__init__(Transform(self.parent_transform.position+self.dx))
        self.mesh = CircularMesh(20, Material(Color.green))
        self.pai = pai
        self.wait = 0
        self.collider = MeshCollider(self.mesh, self.transform)

    def start(self):
        self.add_collider(self.collider)

    def update(self):
        self.dx = self.dx.rotate(100.0*Timer.get_dt())
        self.transform.position = self.parent_transform.position+self.dx
        if EventHandler.key_space and self.wait < Timer.get_current_time():
            SceneManager.get_current_scene().add_game_object(Test2(Transform(Vector2(self.transform.position), 0,1,3)))
            self.wait = Timer.get_current_time()+0.1

    def draw(self):
        self.mesh.render(self.transform)
        pass