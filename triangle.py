"""AP1VS  Triangle."""

import math


def sides(A, B, C):
    """
    Return side sizes from passed points coordinates.

    Parameters
    ----------
    A : Coordinates for point A
    B : Coordinates for point B
    C : Coordinates for point C

    Returns
    -------
    a, b, c : Calculated side sizes
    """
    a = math.sqrt(pow(abs(B[0] - C[0]), 2) + pow(abs(B[1] - C[1]), 2))
    b = math.sqrt(pow(abs(A[0] - C[0]), 2) + pow(abs(A[1] - C[1]), 2))
    c = math.sqrt(pow(abs(A[0] - B[0]), 2) + pow(abs(A[1] - B[1]), 2))
    return a, b, c


def assemblability(a, b, c):
    """
    Check assemblability of the triangle.

    Parameters
    ----------
    a : Side a
    b : Side b
    c : Side c

    Returns
    -------
    True, False
    """
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def squarness(a, b, c):
    """
    Check squarness of the triangle.

    Parameters
    ----------
    a : Side a
    b : Side b
    c : Side c

    Returns
    -------
    True, False
    """
    if round(pow(a, 2), 5) + round(pow(c, 2), 5) == round(pow(b, 2), 5):
        return True
    else:
        return False


def calculation(a, b, c):
    """
    Calculate perimeter and area of the triangle.

    Parameters
    ----------
    a : Side a
    b : Side b
    c : Side c

    Returns
    -------
    perimeter : perimeter of the triangle
    area : area of the triangle
    """
    perimeter = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return perimeter, area


def triangle():
    """
    Body of the triangle function.

    This function prints every calculated data of the triangle.
    Coordinates of the points are passed as user input.

    Parameters
    ----------
    None

    Returns
    -------
     None
    """
    print("""You will be prompted to enter coordinates
    for each points of triangle, enter two numbers
    with space between them""")

    try:
        A = input("A: ")
        A = tuple(map(int, A.split()))

        B = input("B: ")
        B = tuple(map(int, B.split()))

        C = input("C: ")
        C = tuple(map(int, C.split()))

        a, b, c = sides(A, B, C)
        print("Sides: a = %.2f, b = %.2f, c = %.2f" % (a, b, c))

        if assemblability(a, b, c):
            print("Triangle is assemblable")

            if squarness(a, b, c):
                print("Triangle is rectangular")
            else:
                print("Triangle is not rectangular")

            perimeter, area = calculation(a, b, c)
            print("Perimeter: %.2f  Area: %.2f" % (perimeter, area))
        else:
            print("Triangle is not assemblable")
    except Exception:
        print('You need to enter coordinates for each point')


if __name__ == "__main__":
    triangle()


"""Unit Tests."""


def inputTest(capsys):
    """Test input."""
    triangle(1, 1, 1)
    captured = capsys.readouterr()
    assert captured.out == 'You need to enter coordinates for each point'


def testSides1():
    """First testing of the sides function."""
    a, b, c = sides((2, 1), (5, 2), (4, 4))
    assert a == 2.23606797749979
    assert b == 3.605551275463989
    assert c == 3.1622776601683795


def testSides2():
    """Second testing of the sides function."""
    a, b, c = sides((14, 6), (12, 26), (56, 121))
    assert a == 104.69479452198185
    assert b == 122.42957159118053
    assert c == 20.09975124224178


def testSides3():
    """Third testing of the sides function."""
    a, b, c = sides((-4, 1), (23, -4), (-14, -2))
    assert a == 37.05401462729781
    assert b == 10.44030650891055
    assert c == 27.459060435491963


def testAssemblability1():
    """First testing of the assemblability function."""
    a, b, c = sides((2, 1), (5, 2), (4, 4))
    assert assemblability(a, b, c) is True


def testAssemblability2():
    """Second testing of the assemblability function."""
    a, b, c = sides((1, 2), (1, 2), (3, 3))
    assert assemblability(a, b, c) is False


def testSquarness1():
    """First testing of the squarness function."""
    a, b, c = sides((1, 3), (6, 3), (6, 8))
    assert squarness(a, b, c) is True


def testSquarness2():
    """Second testing of the squarness function."""
    a, b, c = sides((2, 1), (5, 2), (4, 4))
    assert squarness(a, b, c) is False


def testCalculation1():
    """First testing of the calculation function."""
    a, b, c = sides((2, 1), (5, 2), (4, 4))
    perimeter, area = calculation(a, b, c)
    assert perimeter == 9.00389691313216
    assert area == 3.500000000000002


def testCalculation2():
    """First testing of the calculation function."""
    a, b, c = sides((-3, 25), (17, 6), (121, 4))
    perimeter, area = calculation(a, b, c)
    assert perimeter == 257.3711125289721
    assert area == 968.0000000000007
