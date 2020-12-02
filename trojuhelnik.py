"""
VS PROJECT

This project contains methods for calculating triangle lengths,
perimeter and area. It also tells you whether specified triangle
can be constructed

All values are rounded to 3 decimal digits
"""

def getUserInput(message):
    """
    Method for getting input from user

    Args:
        message: prompt message

    Returns:
        X and Y coordinate
    """
    inp = input(message + "\n")
    while len(inp.split()) != 2:
        inp = input("Invalid input. Try it again. Example input: 1 2" + "\n")
    return inp.split()

def sqrt(n):
    """
    Square root calculation

    Args:
        n: Input number

    Returns:
        Square root of n
    """
    return round(n ** (1/2), 3)

def sqr(n):
    """
    Power of 2 calculation

    Args:
        n: Input number

    Returns:
        n multiplied by itself
    """
    return n * n

def calculatePerimeter(a, b, c):
    """
    Calculates triangle perimeter

    Args:
        a: a side length
        b: b side length
        c: c side length

    Returns:
        Perimeter of specified triangle
    """
    return round(a + b + c, 3)

def calculateArea(a, b, c):
    """
    Calculates triangle area using Heron's formula
    Heron's formula: s = (a + b + c) / 2

    Args:
        a: a side length
        b: b side length
        c: c side length

    Returns:
        Area of specified triangle
    """
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def isConstructable(a, b, c):
    """
    Checks if triangle can be constructed

    Args:
        a: a side length
        b: b side length
        c: c side length

    Returns:
        If triangle can be constructed
    """
    return a + b > c and a + c > b and b + c > a

def isRightAngled(a, b, c):
    """
    Checks if triangle is right angled using Pythagora's theorem
    c^2 = a^2 + b^2

    Args:
        a: a side length
        b: b side length
        c: c side length

    Returns:
        If triangle is right angled
    """
    sa = sqr(a)
    sb = sqr(b)
    sc = sqr(c)
    return sc == sa + sb or sb == sa + sc or sa == sb + sc

def test_sqrt():
    """
    Test for sqrt method
    """
    assert sqrt(81) == 9
    assert sqrt(9) == 3
    assert sqrt(16) == 4
    assert sqrt(144) == 12

def test_sqr():
    """
    Test for sqr method
    """
    assert sqr(4) == 16
    assert sqr(8) == 64
    assert sqr(3) == 9
    assert sqr(16) == 256

def test_calculatePerimeter():
    """
    Test for calculatePerimeter method
    """
    assert calculatePerimeter(15, 20, 25) == 60
    assert calculatePerimeter(10.5, 18, 14.5) == 43
    assert calculatePerimeter(15, 15, 15) == 45

def test_calculateArea():
    """
    Test for calculateArea method
    """
    assert calculateArea(15, 20, 25) == 150
    assert calculateArea(20, 20, 30) == 198.431
    assert calculateArea(15, 15, 15) == 97.428

def test_isConstructable():
    """
    Test for isConstructable method
    """
    assert isConstructable(15, 20, 25)
    assert isConstructable(20, 20, 30)
    assert isConstructable(15, 15, 15)

def test_isRightAngled():
    """
    Test for isRightAngled method
    """
    assert isRightAngled(12, 9, 15)

def test_round():
    """
    Test for round method
    """
    assert round(1.40123, 3) == 1.401
    assert round(1.04681, 3) == 1.047

if __name__ == "__main__":
    # Main function
    # First 3 steps are loading user input

    a = getUserInput("Enter A coordinate in 2D grid")
    b = getUserInput("Enter B coordinate in 2D grid")
    c = getUserInput("Enter C coordinate in 2D grid")

    # Convert to int coordinate array
    aCoord = [int(a[0]), int(a[1])]
    bCoord = [int(b[0]), int(b[1])]
    cCoord = [int(c[0]), int(c[1])]

    # Calculate lengths
    # a - BC
    # b - AC
    # c - AB
    al = sqrt(sqr(bCoord[0] - cCoord[0]) + sqr(bCoord[1] - cCoord[1]))
    bl = sqrt(sqr(aCoord[0] - cCoord[0]) + sqr(aCoord[1] - cCoord[1]))
    cl = sqrt(sqr(aCoord[0] - bCoord[0]) + sqr(aCoord[1] - bCoord[1]))
    print("Lengths: a =", al, ", b =", bl, ", c =", cl)

    if isConstructable(al, bl, cl):
        print("Triangle can be constructed")
        # Print triangle perimeter
        print("Triangle perimeter:", calculatePerimeter(al, bl, cl))
        # Print triangle area
        print("Triangle area:", calculateArea(al, bl, cl))
        # Print if triangle is right angled
        print("Is right angled:", isRightAngled(al, bl, cl))
    else:
        print("Triangle cannot be constructed")
