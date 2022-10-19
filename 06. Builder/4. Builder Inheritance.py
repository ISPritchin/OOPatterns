class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None
        self.hobbies = []

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}\n' \
               f'hobbies: {" ".join(self.hobbies)}'


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


class PersonHobbyBuilder(PersonBirthDateBuilder):
    def add_hobby(self, hobby):
        self.person.hobbies.append(hobby)
        return self


if __name__ == '__main__':
    pb = PersonHobbyBuilder()
    me = pb \
        .called('Ivan') \
        .works_as_a('teacher') \
        .born('09/12/1994') \
        .add_hobby("piano") \
        .add_hobby("programming") \
        .build()
    print(me)
