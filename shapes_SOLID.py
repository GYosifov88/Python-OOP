from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height / 2


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

# Създаваме базов абстрактен клас Шейп където има абсктрактен метод за калкулиране на ареята
# Класовете за видове (триъгълник, правоъгълник и т.н.) наследяват Шейп и в метода за ареята се слага конкретната формула
# Класа за калкулатора вече събира тотала и смята базирайки на формула за арея на конкретна фигура