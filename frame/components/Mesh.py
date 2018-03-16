#!/usr/bin/python3

import abc


class Mesh:

    def __init__(self, points, material):
        """
        A mesh is defined by a list of points
        :param points: the points which define the mesh
        """
        self.points = points
        self.material = material

    @abc.abstractmethod
    def render(self, transform):
        """
        This method is responsible for rendering a mesh
        """
        pass
