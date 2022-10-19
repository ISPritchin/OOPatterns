from enum import Enum
from typing import List, Any
from abc import abstractmethod


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


class Specification:
    @abstractmethod
    def is_satisfied(self, item: Any) -> bool:
        pass


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Any) -> bool:
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Any) -> bool:
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, specs: List[Specification]):
        self.specs = specs

    def is_satisfied(self, item: Any) -> bool:
        for spec in self.specs:
            if not spec.is_satisfied(item):
                return False

        return True


def filter(items: List[Any], spec: Specification):
    for item in items:
        if spec.is_satisfied(item):
            yield item


products = [
    Product('Apple', Color.GREEN, Size.SMALL),
    Product('Tree', Color.GREEN, Size.LARGE),
    Product('House', Color.BLUE, Size.LARGE)
]

green = ColorSpecification(Color.GREEN)
print("Green products:")
for p in filter(products, green):
    print(f"- {p.name} is green")

large = SizeSpecification(Size.LARGE)
print("Large products:")
for p in filter(products, large):
    print(f"- {p.name} is large")

print("Large and green products:")
large_and_green = AndSpecification([large, green])
for p in filter(products, large_and_green):
    print(f"- {p.name} is large and green")
