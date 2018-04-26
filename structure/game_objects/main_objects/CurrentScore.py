from frame import *

class CurrentScore(GameObject):

    def __init__(self, vector):
        """
        The game name
        :param : the starting position for the player
        """
        super().__init__(Transform(vector, 0, scale=50))
        self.real_score = 0
        self.mesh_score = TextMesh("Score: ", Font.space_font, Material(Color.white))
        self.mesh_points = TextMesh(str(self.real_score), Font.space_font, Material(Color.white))
        self.transform.layer = 2
        self.transform.scale = 30
        self.wait = 0

    def start(self):
        pass

    def add_score(self, value):
        self.real_score += value

    def update(self):
        self.mesh_points = TextMesh(str(self.real_score), Font.space_font, Material(Color.white))

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh_score.render(Transform(Vector2(self.transform.position), 0, self.transform.scale))
        self.mesh_points.render(Transform(Vector2(self.transform.position + Vector2(150, 0)), 0, self.transform.scale))
