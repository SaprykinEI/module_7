class Square:
    '''Модель квадрата'''

    def __init__(self, side_square):
        self.side_square = side_square

class Circle:
    '''Модель окружности'''

    def __init__(self, diameter):
        self.diameter = diameter


class CircleInSquare(Square, Circle):
    '''Модель окружности вписанной в квадрат'''

    def __init__(self, side_square, diameter):
        Square.__init__(self, side_square)
        Circle.__init__(self, diameter)

    def get_inscribed_circle_in_a_square(self):
        '''Проверка вписанной окружности'''

        if self.diameter == self.side_square:
            return print("Окружность вписана")
        else:
            return print("Окружность не вписана")


square_1 = Square(5)
circle_1 = Circle(2)

circle = CircleInSquare(square_1, circle_1)
circle.get_inscribed_circle_in_a_square()


