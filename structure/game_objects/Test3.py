from frame import *
from pygame.math import Vector2


class Test3(GameObject):

    def __init__(self, transform):
        super().__init__(Transform(transform))
        self.mesh = CircularMesh(100, Material(Color.yellow))
        self.collider = MeshCollider(self.mesh, self.transform)

    def start(self):
        SceneManager.get_current_scene().colliders_map[self] = self.collider
        pass

    def update(self):

        if len(self.collider.collisions_list) > 0:
            self.mesh.material.color = Color.red
        else:
            self.mesh.material.color = Color.blue
        self.collider.draw_colliding_outline()
    def draw(self):
        #self.mesh.render(self.transform)
        pass