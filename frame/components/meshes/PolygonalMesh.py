#!/usr/bin/python3

from ..Mesh import Mesh
from frame.core.Renderer import Renderer
from pygame.math import Vector2


class PolygonalMesh(Mesh):

    def __init__(self, points, material, pivot=Vector2(0,0)):
        super().__init__(points, material)
        """
        A polygon is defined by its points and material
        :param points:
        :param material:
        :param pivot:
        """
        self.pivot = pivot

    def render(self, transform, mode='Filled'):
        """
        This method uses simple polygon render functionality
        :param mode:
        :param transform:
        """
        Renderer.render_simple_polygon(self, transform, mode)

    def set_center_pivot(self):
        """
        This method sets the pivot to the center
        """

        center = Vector2(0, 0)

        for point in self.points:
            center += point

        self.pivot = center/len(self.points)
