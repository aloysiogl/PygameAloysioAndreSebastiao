#!/usr/bin/python3

from ..Mesh import Mesh
from frame.core.Renderer import Renderer


class CircularMesh(Mesh):

    def __init__(self, radius, material):
        super().__init__(None, material)
        """
        The circle is defined by its radius and material
        :param radius:
        :param material:
        """
        self.radius = radius

    def render(self, transform):
        """
        This method uses simple circle render functionality
        :param transform:
        """
        Renderer.render_simple_circle(self, transform)

