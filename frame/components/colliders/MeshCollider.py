#!/usr/bin/python3

from ..Collider import Collider
from frame.core.Renderer import Renderer
from ..Material import Material
from frame.core.Representations import Color

import copy


class MeshCollider(Collider):
    def __init__(self, mesh, transform, collisions_list=[]):
        """
        The mesh collider is a collider defined by a mesh
        :param mesh: hte mesh collider needs a mesh
        :param transform: the transform for the collider
        :param collisions_list: list of objects colliding to my object
        """

        super().__init__(transform, collisions_list)

        self.mesh = mesh

    def is_colliding(self, collider):
        """
        Detects collisions to other colliders
        :param collider: the collider to check collision with
        :return: if there was a collision
        """

        if collider.__class__.__name__ == 'MeshCollider':
            if self.mesh.__class__.__name__ == 'CircularMesh':
                if collider.mesh.__class__.__name__ == 'CircularMesh':
                    dist = self.mesh.radius*self.transform.scale + collider.mesh.radius*collider.transform.scale
                    if self.transform.position.distance_to(collider.transform.position) < dist:
                        return True
                    return False

            elif self.mesh.__class__.__name__ == 'PolygonalMesh':
                pass

    def render_colliding_outline(self):
        """
        Draw the outside of a collider for debug reasons
        """

        outline_mesh = copy.copy(self.mesh)

        if len(self.collisions_list) > 0:
            outline_mesh.material = Material(Color.red)
        else:
            outline_mesh.material = Material(Color.medium_blue)

        if self.mesh.__class__.__name__ == 'CircularMesh':
            Renderer.render_simple_circle(outline_mesh, self.transform, mode='Outline')
        elif self.mesh.__class__.__name__ == 'PolygonalMesh':
            Renderer.render_simple_polygon(outline_mesh, self.transform, mode='Outline')
