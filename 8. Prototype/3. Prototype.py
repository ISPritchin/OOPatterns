# В языке программирования python имеется функция deepcopy для решения данной проблемы
# Можно получить глубокую копию.

import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person("John", Address("123 London Road", "London", "UK"))
jane = copy.deepcopy(john)
jane.name = "Jane"
jane.address.street_address = "1 London Road"
print(john)
print(jane)
