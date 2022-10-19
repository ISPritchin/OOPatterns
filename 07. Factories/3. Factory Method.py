# Фабричный метод (англ. Factory Method), или виртуальный
# конструктор (англ. Virtual Constructor) — порождающий шаблон проектирования,
# предоставляющий подклассам (дочерним классам) интерфейс
# для создания экземпляров некоторого класса.

from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = Point.new_cartesian_point(5, 6)
    p2 = Point.new_polar_point(1, 0)
    print(p1, p2)
