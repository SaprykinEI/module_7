class Square:

    def __init__(self, side_square):
        self.side_square = side_square

    def get_square_area(self):
        square_area = self.side_square ** 2
        return square_area


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14


    def get_area_circle(self):
        circle_area = self.pi * (self.radius ** 2)
        return circle_area


class CircleInSquare(Square, Circle):
    def __init__(self, side_square):
        Square.__init__(self, side_square)
        radius = side_square / 2
        Circle.__init__(self, radius)

    def get_circle_in_square(self):
        return self.side / 2






