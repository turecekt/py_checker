"""
Calculate triangle.

>>> 1
1
"""
from math import sqrt, pow


class Triangle:
    """
    Class of the triangle.

    :ivar
        point_a, point_b, point_c:
            used for storing the points inserted by user
        a, b, c:
            used for storing the calculated sides
    """

    def __init__(self, point_a, point_b, point_c):
        """
        Define points and sides of the triangle.

        :param
            point_a, point_b, point_c:
                used for transfer points to self.points
        """
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.a, self.b, self.c = self.side_lenght()

    def side_lenght(self):
        """
        Take inserted points and calculate sides.

        :return: [float, float, float] -> list
        """
        sides = (self.point_a, self.point_b), \
                (self.point_a, self.point_c), \
                (self.point_b, self.point_c)

        return [
            sqrt(pow(i[0][0] - i[1][0], 2) + pow(i[0][1] - i[1][1], 2))
            for i in sides]

    def is_able(self):
        """
        Check if the triangle is able to construct.

        :return: True | False
        """
        a, b, c = self.a, self.b, self.c

        if a + b > c and a + c > b and c + b > a:
            return True
        else:
            return False

    def is_rectangular(self):
        """
        Check if there is 90 degrees corner in the triangle.

        :return: True | False
        """
        sides: list[float] = [self.a, self.b, self.c]
        sides.sort(reverse=True)

        if round(sides[0] * sides[0]) == sides[1] * sides[1] + sides[2] * \
                sides[2]:
            return True
        else:
            return False

    def perimeter(self):
        """
        Calculate the other contour of the triangle.

        :return: perimeter of the triangle (float)
        """
        return self.a + self.b + self.c

    def area(self) -> float:
        """
        Calculate the inner area of the triangle.

        :return: Area of the triangle (float)
        """
        s = self.perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
