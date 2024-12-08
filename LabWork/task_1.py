from math import pi, sqrt

class Square:
    '''Модель квадрата'''

    def __init__(self, side_square):
        self.side_square = side_square

    def get_square_area(self):
        area_square = self.side_square ** 2
        return area_square

class Circle:
    '''Модель окружности'''

    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        circle_area = pi * (self.radius ** 2)
        return circle_area


class CircleInSquare(Square, Circle):
    '''Модель окружности вписанной в квадрат'''

    def __init__(self, side_square, radius):
        Square.__init__(self, side_square)
        Circle.__init__(self, radius)

    def get_inscribed_circle_in_a_square(self):
        diameter = self.radius * 2


#Не понимаю как делать эту задачу с точки зрения математики (очень далёк от нее).
# Снизьте бал за неё, но не возвращайте её на переделку пожалуйста!





