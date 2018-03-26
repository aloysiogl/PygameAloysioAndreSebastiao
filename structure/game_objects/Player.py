from frame import *


class Player(GameObject):

    def __init__(self, initial_pos):
        """
            A Player is the principal caracter of the game
            :param initicial_pos: the position of the caracter
        """
        super().__init__(Transform(initial_pos))
        self.mesh = PolygonalMesh([Vector2(0,-200), Vector2(40,-200), Vector2(55,-250),Vector2(60,-200),Vector2(80, -70),
                                   Vector2(130, -300),Vector2(160,00),Vector2(130,250), Vector2(80,0),Vector2(40,150),
                                   Vector2(0, 50), Vector2(-40,150), Vector2(-80,0), Vector2(-130,250), Vector2(-160,0),
                                   Vector2(-130,-300), Vector2(-80, -70), Vector2(-60, -200), Vector2(-55,-250), Vector2(-40,-200),
                                   Vector2(0,-200)], Material(Color.black))
        self.mesh2 = PolygonalMesh([Vector2(0,-40), Vector2(20,-150), Vector2(40,-40), Vector2(20,150), Vector2(0,40)], Material(Color.yellow))
        self.mesh3 = PolygonalMesh([Vector2(0, -40), Vector2(-20, -150), Vector2(-40, -40)], Material(Color.yellow))

        self.wait = 0
        self.mesh.set_center_pivot()
        self.collider = MeshCollider(self.mesh, self.transform, [])

    def start(self):
        self.add_collider(self.collider)

    def update(self):
        if EventHandler.key_up:
            self.transform.position -= Timer.get_dt() * 500 * Vector2(0, 1)
            self.transform.scale += 0.005
            self.mesh.material.color = Color.red
        if EventHandler.key_down:
            self.transform.position += Timer.get_dt() * 500 * Vector2(0, 1)
            self.transform.scale -= 0.005
            self.mesh.material.color = Color.green
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
        self.mesh3.render(self.transform)
        self.mesh.render(self.transform)
        self.collider.render_colliding_outline()