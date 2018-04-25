#!/usr/bin/python3

from ..Mesh import Mesh
from frame.core.Renderer import Renderer


class TextMesh(Mesh):

    def __init__(self, text, font, material):
        super().__init__(None, material)
        """
        The text mesh is defined by its text, its font and its material 
        :param text: the text to be shown
        :param font: the font used
        :param material: the material of the mesh
        """
        self.text = text
        self.font = font

    def render(self, transform, alpha=255):
        """
        This method uses simple font render functionality
        :param alpha: the alpha t be rendered
        :param transform: the transform to render the circle
        """
        Renderer.render_simple_font(self, transform, alpha)

