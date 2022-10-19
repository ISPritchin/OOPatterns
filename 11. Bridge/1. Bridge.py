# Шаблон проектирования "Мост" о соединении компонентов посредством абстракций

from abc import abstractmethod


# Выполним создание отрисовщиков для векторной и пиксельной графики
class Renderer:
    @abstractmethod
    def render_circle(self, radius):
        pass

    @abstractmethod
    def render_rectangle(self, height, weight):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

    def render_rectangle(self, height, weight):
        print(f'Drawing a rectangle {height} * {weight}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')

    def render_rectangle(self, height, weight):
        print(f'Drawing pixels for rectangle {height} * {weight}')


# Создадим фигуру, конструктор принимает отрисовщик, опишем поведение фигуры
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def resize(self, factor): pass


# Делегируем отрисовку классу Renderer и его наследнику
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


class Rectangle(Shape):
    def __init__(self, renderer, height, weight):
        super().__init__(renderer)
        self.height = height
        self.weight = weight

    def draw(self):
        self.renderer.render_rectangle(self.height, self.weight)

    def resize(self, factor):
        self.height *= factor
        self.weight *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    rectangle = Rectangle(raster, 5, 2)
    rectangle.draw()
    rectangle.resize(2)
    rectangle.draw()
