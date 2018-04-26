from frame import *

class CurrentScore(GameObject):

    def __init__(self, vector):
        """
        The game name
        :param : the starting position for the player
        """
        super().__init__(Transform(vector, 0, scale=50))
        self.points = 0
        self.mesh_score = TextMesh("Score: ", Font.space_font, Material(Color.white))
        #self.mesh_points = TextMesh(self.points, Font.space_font, Material(Color.white))
        self.transform.layer = 2
        self.transform.scale = 30

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        """
        Rendering its mesh
        """

        self.mesh_score.render(Transform(Vector2(self.transform.position), 0, self.transform.scale))
        #self.mesh_points.render(self.transform, 0)
