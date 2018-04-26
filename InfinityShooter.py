from frame.core import Core
from frame import SceneManager

from structure.scenes.MainScene import main_scene
from structure.scenes.MenuScene import get_menu_scene
from structure.scenes.ScoreScene import get_score_scene

# Adding the scene to the game

SceneManager.add_scene(get_score_scene())
SceneManager.add_scene(get_menu_scene())
SceneManager.add_scene(main_scene)


# Starting the game

Core.start("Infinity Shooter")
