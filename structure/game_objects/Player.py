from frame import *

class Player(GameObject):

    def __init__(self, initial_pos):
        super().__init__(Transform(initial_pos))
        self.mesh = PolygonalMesh([Vector2(0,100), Vector2(10,100), Vector2()])


        #self.mesh = PolygonalMesh([Vector2(0, 0), Vector2(100, 0), Vector2(100, 100), Vector2(0, 100)],
                                  Material(Color.blue))
        self.wait = 0
        self.mesh2 = CircularMesh(100, Material(Color.black))
        self.mesh.set_center_pivot()
        self.mesh3 = CircularMesh(100, Material(Color.blue))
        self.collider = MeshCollider(self.mesh3, self.transform, [])
        self.buddy = Buddy(self.transform, self)

    def start(self):
        SceneManager.get_current_scene().add_game_object(self.buddy)
        self.add_collider(self.collider)

    def update(self):
        if EventHandler.key_up:
            self.transform.position -= Timer.get_dt() * 500 * Vector2(0, 1)
            self.transform.scale += 0.005
            self.buddy.mesh.material.color = Color.green
            self.mesh.material.color = Color.red
        if EventHandler.key_down:
            self.transform.position += Timer.get_dt() * 500 * Vector2(0, 1)
            self.transform.scale -= 0.005
            self.mesh.material.color = Color.green
            self.buddy.mesh.material.color = Color.red
        if EventHandler.key_left:
            self.transform.position -= Timer.get_dt() * 500 * Vector2(1, 0)
            self.transform.rotation += 5
        if EventHandler.key_right:
            self.transform.position += Timer.get_dt() * 500 * Vector2(1, 0)
            self.transform.rotation -= 5
        if EventHandler.key_space and self.wait < Timer.get_current_time():
            SceneManager.get_current_scene().add_game_object(
                Test2(Transform(Vector2(self.transform.position), 0, 2, 1)))
            self.wait = Timer.get_current_time() + 0.2

    def draw(self):
        self.mesh2.render(self.transform)
        self.mesh.render(self.transform)
        self.collider.render_colliding_outline()