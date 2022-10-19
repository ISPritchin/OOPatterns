# Решение заключается в разделении функционала на несколько классов: первый отвечает
# за работу с записями, второй - за работу с сохранением и загрузкой журнала

# Всё делается для того, чтобы не создавать классов (God classes), в которых собрана вся функциональность
# для взаимодействия с ним.

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


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    @staticmethod
    def load_from_file(journal, filename):
        pass

    @staticmethod
    def load_from_web(journal, filename):
        pass
