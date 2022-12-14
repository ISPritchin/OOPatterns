# Проблема: при создании точек в разных системах координат разрастается конструктор.

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

# Предлагается создавать точки иначе
