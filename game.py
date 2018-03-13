from frame.core import Core
from frame import SceneManager

from structure.scenes.MainScene import main_scene

# Adding the scene to the game

SceneManager.add_scene(main_scene)

# Starting the game

Core.start("Game name")