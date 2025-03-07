from enum import Enum

from pygame import QUIT

class Mode(Enum):
    MANUAL = "manual"
    AUTONOMOUS = "autonomous"
    QUIT = "quit"