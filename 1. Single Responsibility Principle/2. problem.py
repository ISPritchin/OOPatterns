# Расширим функционал для сохранения данных из файла и в файл

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    def save_to_file(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load_from_file(self, filename):
        pass

    def load_from_web(self, filename):
        pass

# Проблема: класс выполняет действия как по работе с записями, так и по сохранению и чтению из сохранения.
# Он стал выполнять несколько обязанностей
