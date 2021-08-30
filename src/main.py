from cube import Cube
from gui import Gui
from config import *
from presets import *
import sys

if __name__ == "__main__":
    init_config()
    cube = Cube(3)
    gui = Gui(cube)
    gui.run()
