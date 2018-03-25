#!/usr/bin/python3

import copy

from frame.core.Renderer import Renderer
from frame.core.Representations import Color
from ..Collider import Collider
from ..Material import Material


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

    @staticmethod
    def __get_transformed_polygon(transform, polygon_mesh):
        """
        Gets a polygon points considering pivot and rotation
        :param transform: the transform relations
        :param polygon_mesh: the mesh containing the points
        :return: a list of transformed points
        """

        points_list = []

        for point in polygon_mesh.points:
            distance_from_origin_local = point - polygon_mesh.pivot

            scaled_distance = distance_from_origin_local * transform.scale

            rotated_distance = scaled_distance.rotate(transform.rotation)

            points_list.append(rotated_distance + transform.position)

        return points_list

    @staticmethod
    def __edge_ray_trace(point, edge1, edge2):
        """
        Detects trace collision
        :param point: point to be tested
        :param edge1: first edge point
        :param edge2: second edge point
        :return: if the ray traced to the left intersects the edge
        """

        minn = edge1
        maxx = edge2

        if edge2.y < edge1.y:
            minn = edge2
            maxx = edge1

        line_edges = maxx - minn

        test_line = point - minn

        if minn.y < point.y < maxx.y and line_edges.cross(test_line) > 0:
            return True
        return False

    def __full_ray_trace(self, point, other_points):
        """
        Detects if a point is inside a polygon
        :param point: point to check if is inside
        :param other_points: points describing polygon
        :return: if the point is inside the polygon
        """

        cross_count = 0

        if self.__edge_ray_trace(point, other_points[-1], other_points[0]):
            cross_count += 1

        for i in range(len(other_points) - 1):
            if self.__edge_ray_trace(point, other_points[i], other_points[i + 1]):
                cross_count += 1
        if cross_count % 2 == 1:
            return True
        return False

    def is_colliding(self, collider):
        """
        Detects collisions to other colliders
        :param collider: the collider to check collision with
        :return: if there was a collision
        """

        if collider.__class__.__name__ == 'MeshCollider':
            if self.mesh.__class__.__name__ == 'CircularMesh':
                if collider.mesh.__class__.__name__ == 'CircularMesh':
                    dist = self.mesh.radius * self.transform.scale + collider.mesh.radius * collider.transform.scale
                    if self.transform.position.distance_to(collider.transform.position) < dist:
                        return True
                    return False

                elif collider.mesh.__class__.__name__ == 'PolygonalMesh':
                    return collider.is_colliding(self)

            elif self.mesh.__class__.__name__ == 'PolygonalMesh':
                if collider.mesh.__class__.__name__ == 'PolygonalMesh':
                    # Safe distance check
                    dist = self.mesh.safe_dist * self.transform.scale + collider.mesh.safe_dist * collider.transform.scale
                    center_vector = self.transform.position + \
                                    (self.mesh.center - self.mesh.pivot).rotate(self.transform.rotation) \
                                    * self.transform.scale
                    collider_center_vector = collider.transform.position + \
                                    (collider.mesh.center - collider.mesh.pivot).rotate(collider.transform.rotation)\
                                    * collider.transform.scale
                    if center_vector.distance_to(collider_center_vector) > dist:
                        return False

                    # Getting points after apply transform

                    my_points = self.__get_transformed_polygon(self.transform, self.mesh)
                    other_points = self.__get_transformed_polygon(collider.transform, collider.mesh)

                    # Checking collision for each point in the polygon

                    for point in my_points:
                        if self.__full_ray_trace(point, other_points):
                            return True
                    for point in other_points:
                        if self.__full_ray_trace(point, my_points):
                            return True
                    return False

                elif collider.mesh.__class__.__name__ == 'CircularMesh':
                    # Safe distance check
                    dist = self.mesh.safe_dist * self.transform.scale + collider.mesh.radius * collider.transform.scale
                    center_vector = self.transform.position + \
                                    (self.mesh.center - self.mesh.pivot).rotate(self.transform.rotation) \
                                    * self.transform.scale
                    if center_vector.distance_to(collider.transform.position) > dist:
                        return False

                    # Getting my points after apply transform

                    my_points = self.__get_transformed_polygon(self.transform, self.mesh)

                    reference_distance = collider.mesh.radius * collider.transform.scale

                    # Checking vertexes

                    for point in my_points:
                        dist = point - collider.transform.position

                        if dist.length() < reference_distance:
                            return True

                    # Checking edges

                    edge = my_points[0] - my_points[-1]

                    translated_point = collider.transform.position - my_points[-1]

                    if abs(translated_point.cross(edge) / edge.length()) < reference_distance:
                        if 0 < translated_point.dot(edge) < edge.length() ** 2:
                            return True

                    for i in range(len(my_points) - 1):
                        translated_point = collider.transform.position - my_points[i]
                        edge = my_points[i + 1] - my_points[i]

                        if abs(translated_point.cross(edge) / edge.length()) < reference_distance:
                            if 0 < translated_point.dot(edge) < edge.length() ** 2:
                                return True

                    # Checking inside

                    if self.__full_ray_trace(collider.transform.position, my_points):
                        return True

                    return False

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
