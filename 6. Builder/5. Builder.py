class Animal:
    """
    Абстрактное Животное
    """
    legs = 0
    tail = False
    roar = ''


class Mutator:
    """
    Ответственный за размножение
    """

    def mutate(self):
        self.animal = Animal()


class Cat(Mutator):
    """
    Кошка
    """

    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = 'meowww!'


class Dog(Mutator):
    """
    Собака
    """

    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = 'woffff!'


class AnimalOwner:
    """
    Владелец питомника
    """
    _mutator = ''

    def set_animal(self, mutator):
        self._mutator = mutator

    def create_an_animal_for_me(self):
        self._mutator.mutate()
        self._mutator.create_legs()
        self._mutator.create_tail()
        self._mutator.create_roar()

    def get_animal(self):
        return self._mutator.animal


c = Cat()
ao = AnimalOwner()
ao.set_animal(c)
ao.create_an_animal_for_me()
animal = ao.get_animal()
print(animal.roar)  # meowww!
