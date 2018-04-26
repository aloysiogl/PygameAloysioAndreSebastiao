from frame.core import Core
from frame import SceneManager

from structure.scenes.MainScene import main_scene
from structure.scenes.MenuScene import get_menu_scene

# Adding the scene to the game

SceneManager.add_scene(get_menu_scene())
SceneManager.add_scene(main_scene)


# Starting the game

Core.start("Infinity Shooter")