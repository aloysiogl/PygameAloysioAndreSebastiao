#!/usr/bin/python3


class Transform:

    def __init__(self, position, rotation=0, scale=1, layer=0):
        """
        The transform defines spatial orientation parameters
        :param position: the position
        :param rotation: the rotation in degrees
        :param scale: the scale (1 is 100%)
        :param layer: the layer for rendering
        """
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.layer = layer
