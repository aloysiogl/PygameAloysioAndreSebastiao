#!/usr/bin/python3


from frame import *
from frame.core.Representations import Screen

from structure.game_objects.score_objects.ScoreText import ScoreText
from structure.game_objects.score_objects.ScoreController import ScoreController


def get_score_scene():
    """
    This method creates a score scene
    :return: The score scene
    """

    score_text = ScoreText(Vector2(Screen.width/2, Screen.height/8))
    score_controller = ScoreController()

    return Scene([score_text, score_controller], Material(Color.black))
