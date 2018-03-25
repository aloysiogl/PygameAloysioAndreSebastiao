#!/usr/bin/python3

from ..Mesh import Mesh
from frame.core.Renderer import Renderer
from pygame.math import Vector2


class PolygonalMesh(Mesh):

    def __init__(self, points, material, pivot=Vector2(0,0)):
        super().__init__(points, material)
        """
        A polygon is defined by its points and material
        :param points: the points of the polygon
        :param material: the material of the polygon
        :param pivot: the pivot point for rotation and scaling
        """
        self.pivot = pivot

        # Storing center

        self.center = Vector2(0, 0)

        for point in self.points:
            self.center += point

        self.center = self.center/len(self.points)

        # Storing safe distance for collisions

        self.safe_dist = 0

        for point in self.points:
            vect = point - self.center
            if vect.length() > self.safe_dist:
                self.safe_dist = vect.length()

    def render(self, transform, mode='Filled'):
        """
        This method uses simple polygon render functionality
        :param mode: mode for rendering if supported
        :param transform: transform for rendering
        """
        Renderer.render_simple_polygon(self, transform, mode)

    def set_center_pivot(self):
        """
        This method sets the pivot to the geometric center
        """

        self.pivot = self.center
