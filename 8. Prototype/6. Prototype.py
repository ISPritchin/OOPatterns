import copy
from abc import ABC


class Prototype(ABC):
    def clone(self):
        return copy.deepcopy(self)


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person(Prototype):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person("John", Address("123 London Road", "London", "UK"))
jane = john.clone()
jane.name = "Jane"
jane.address.street_address = "1 London Road"
print(john)
print(jane)
