#!/usr/bin/python3


class Transform:

    def __init__(self, position, rotation=0, scale=1, layer=0):
        """
        The transform defines spatial orientation parameters
        :param position:
        :param rotation:
        :param scale:
        :param layer:
        """
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.layer = layer
