from enum import Enum
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    @staticmethod
    def filter_by_color(products: List[Product], color: Color):
        for p in products:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(products: List[Product], size: Size):
        for p in products:
            if p.color == size:
                yield p

    @staticmethod
    def filter_by_color_and_size(products: List[Product], color: Color, size: Size):
        for p in products:
            if p.color == color and p.size == size:
                yield p

# Проблема: появление ещё одного критерия для фильтра потребует реализации большого количества функций;
# будет наблюдаться дублирование кода
