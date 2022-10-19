# В данной реализации возвращается ссылка на один и тот же объект, однако
# метод __init__ вызывается при каждом создании объекта, что, вероятно, не то, что вы хотите

import random


class Database:
    initialized = False

    def __init__(self):
        self.id = random.randint(1, 101)
        print(self.id)

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1.id, d2.id)
    print(d1 == d2)
