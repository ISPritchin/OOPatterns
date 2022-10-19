# Abstract Building
from abc import abstractmethod


class Building:
    def __init__(self) -> None:
        self.floor = None
        self.size = None
        self.build_floor()
        self.build_size()

    @abstractmethod
    def build_floor(self):
        raise NotImplementedError

    @abstractmethod
    def build_size(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return "Floor: {0.floor} | Size: {0.size}".format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self) -> None:
        self.floor = "One"

    def build_size(self) -> None:
        self.size = "Big"


class Flat(Building):
    def build_floor(self) -> None:
        self.floor = "More than One"

    def build_size(self) -> None:
        self.size = "Small"


class ComplexBuilding:
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self) -> str:
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self) -> None:
        self.floor = "One"

    def build_size(self) -> None:
        self.size = "Big and fancy"


def construct_building(cls) -> Building:
    building = cls()
    building.build_floor()
    building.build_size()
    return building


house = House()
print(house)

flat = Flat()
print(flat)

complex_house = construct_building(ComplexHouse)
print(complex_house)
