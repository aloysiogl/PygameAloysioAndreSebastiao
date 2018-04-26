#!/usr/bin/python3

from frame import *
from structure.game_objects.main_objects.MainShot import MainShot
from assets.GameSounds import Sound
from frame.core.Representations import Screen

class Player(GameObject):

    def __init__(self, initial_pos):
        """
        The Player is the main character of the game
        :param initial_pos: the position of the character
        """
        super().__init__(Transform(initial_pos))
        self.mesh = PolygonalMesh([Vector2(0,-200), Vector2(40,-200), Vector2(55,-250),Vector2(60,-200),Vector2(80, -70),
                                   Vector2(130, -300), Vector2(160,00),Vector2(130,250), Vector2(80,0),Vector2(40,150),
                                   Vector2(0, 50), Vector2(-40,150), Vector2(-80,0), Vector2(-130,250), Vector2(-160,0),
                                   Vector2(-130,-300), Vector2(-80, -70), Vector2(-60, -200), Vector2(-55,-250), Vector2(-40,-200),
                                   Vector2(0,-200)], Material(Color.white))
        self.mesh2 = PolygonalMesh([Vector2(0,-40), Vector2(20,-150), Vector2(40,-40), Vector2(20,150), Vector2(0,40)], Material(Color.yellow))
        self.mesh3 = PolygonalMesh([Vector2(0, -40), Vector2(-20, -150), Vector2(-40, -40)], Material(Color.yellow))
        self.mesh4 = PolygonalMesh([Vector2(20,-100),Vector2(40,-80),Vector2(40,-50),Vector2(-40,-50), Vector2(-40,-80),
                                    Vector2(-20,-100)], Material(Color.black))

        # Flow control parameters

        self.wait = 0
        self.mesh.set_center_pivot()
        self.collider = MeshCollider(self.mesh, self.transform, [])

        # Player parameters

        self.transform.scale = 0.1
        self.speed = 500
        self.shoot_delay = 0.2
        self.turret = "right"

        self.texto = "sadasds"

        self.font_mesh = TextMesh(self.texto, Font.space_font, Material(Color.black))

    def start(self):
        """
        Adding the collider to the scene
        """

        self.add_collider(self.collider)

    def update(self):
        """
        Running movement and shoot
        """

        self.font_mesh.text = str(Timer.get_current_time())

        self.detect_movement()

        self.detect_shoot()

    def draw(self):
        """
        Rendering its meshes
        """

        self.mesh2.render(self.transform)
        self.mesh3.render(self.transform)
        self.mesh.render(self.transform)
        self.mesh4.render(self.transform)

    def detect_movement(self):
        """
        This method detects the movement
        """

        if EventHandler.key_up:
            self.transform.position -= Timer.get_dt() * self.speed * Vector2(0, 1)
        if EventHandler.key_down and self.transform.position.y < Screen.height:
            self.transform.position += Timer.get_dt() * self.speed * Vector2(0, 1)
        if EventHandler.key_left:
            self.transform.position -= Timer.get_dt() * self.speed * Vector2(1, 0)
        if EventHandler.key_right:
            self.transform.position += Timer.get_dt() * self.speed * Vector2(1, 0)

    def detect_shoot(self):
        """
        This method detects if the shoot button is pressed and reacts ot it
        """

        if EventHandler.key_space and self.wait < Timer.get_current_time():

            # Selecting the right turret

            sound = Sound.get_sound('blaster')
            sound.set_volume(0.3)
            sound.play()

            if self.turret == "right":
                SceneManager.get_current_scene().add_game_object(
                    MainShot(Transform(Vector2(self.transform.position + Vector2(10,0)), 0, 1, 0)))
                self.turret = "left"

            elif self.turret == "left":
                SceneManager.get_current_scene().add_game_object(
                    MainShot(Transform(Vector2(self.transform.position + Vector2(-10, 0)), 0, 1, 0)))
                self.turret = "right"

            self.wait = Timer.get_current_time() + self.shoot_delay
