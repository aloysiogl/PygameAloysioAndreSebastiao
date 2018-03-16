#!/usr/bin/python3

from ..Mesh import Mesh
from frame.core.Renderer import Renderer


class CircularMesh(Mesh):

    def __init__(self, radius, material):
        super().__init__(None, material)
        """
        The circle is defined by its radius and material
        :param radius: the radius of the circle
        :param material: the material of the circle
        """
        self.radius = radius

    def render(self, transform, mode='Filled'):
        """
        This method uses simple circle render functionality
        :param mode: the mode while rendering
        :param transform: the transform to render the circle
        """
        Renderer.render_simple_circle(self, transform, mode)

