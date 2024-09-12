"""Import math library."""
import math


def delkaStrany(x1, y1, x2, y2):
    """Calculate the length of a side of a triangle.

    Return the length of the side rounded to 2 decimal places
    >>> delkaStrany(10, 10, 5, 5) == 7.07
    True
    >>> delkaStrany(6, 4, 2, 3)
    4.12
    """
    str1 = x2-x1
    str2 = y2-y1
    str1 = math.pow(str1, 2)
    str2 = math.pow(str2, 2)
    st = round(math.sqrt(str1+str2), 2)
    return st


def getObvod(a, b, c):
    """Calculate the perimeter of a triangle.

    Return the perimeter of the triangle
    >>> getObvod(5, 10, 20) == 35
    True
    >>> getObvod(1, 2, 3)
    6
    """
    o = a + b + c
    return o


def getObsah(a, b, c):
    """Calculate the area of a triangle.

    Return the area of the triangle rounded to 2 decimal places
    (if possible to calculate)
    >>> getObsah(6, 4, 5) == 9.92
    True
    >>> getObsah(1, 1, 23) >= 0
    False
    >>> getObsah(5, 5, 5)
    10.83
    >>> getObsah(2, 4, 8)
    -1
    """
    s = (a + b + c) / 2
    m = s * (s - a) * (s - b) * (s - c)
    if m >= 0:
        obs = round(math.sqrt(m), 2)
    else:
        obs = -1
    return obs


def jeSestrojitelny(a, b, c):
    """Calculate if a triangle is valid.

    Return true or false based on the validity of the triangle
    >>> jeSestrojitelny(50, 100, 1)
    False
    >>> jeSestrojitelny(12, 13, 14)
    True
    """
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


def jePravouhly(a, b, c):
    """Calculate if a triangle is a right triangle.

    Return true if the triangle is a right triangle or false if it is not
    >>> jePravouhly(3, 5, 4)
    True
    >>> jePravouhly(4, 3, 5)
    True
    >>> jePravouhly(5, 3, 4)
    True
    >>> jePravouhly(74, 73, 72)
    False
    """
    cond1 = math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2)
    cond2 = math.pow(b, 2) == math.pow(c, 2) + math.pow(a, 2)
    cond3 = math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2)
    if cond1 or cond2 or cond3:
        return True
    else:
        return False


def jeRovnostranny(a, b, c):
    """Calculate if a triangle is Equilateral.

    Return true if the triangle is equilateral or false if it is not
    >>> jeRovnostranny(0.4, 7.8, 1.6)
    False
    >>> jeRovnostranny(1.7, 1.7, 1.7)
    True
    """
    if a == b == c:
        return True
    else:
        return False


def jeRovnoramenny(a, b, c):
    """Calculate if a triangle is Isosceles.

    Return true if the triangle is isosceles or false if it is not
    >>> jeRovnoramenny(9.9, 10.1, 12.3)
    False
    >>> jeRovnoramenny(1.2, 2.3, 2.3)
    True
    """
    if a == b or b == c or c == a:
        return True
    else:
        return False


def trojuhelnik():
    """Calculate various properties of a triangle.

    Calculate the length of the sides, the perimeter and
    the area (if possible to calculate) of a triangle based on the entered
    coordinates of its three vertices.
    Also calculate if the triangle is valid and if it is a right triangle.
    """
    ax = float(input("Zadejte souřadnice pro bod A na ose X: "))
    ay = float(input("Zadejte souřadnice pro bod A na ose Y: "))
    bx = float(input("Zadejte souřadnice pro bod B na ose X: "))
    by = float(input("Zadejte souřadnice pro bod B na ose Y: "))
    cx = float(input("Zadejte souřadnice pro bod C na ose X: "))
    cy = float(input("Zadejte souřadnice pro bod C na ose Y: "))
    stra = delkaStrany(cx, cy, bx, by)
    print("Délka strany a: " + str(stra) + " cm")
    strb = delkaStrany(ax, ay, cx, cy)
    print("Délka strany b: " + str(strb) + " cm")
    strc = delkaStrany(bx, by, ax, ay)
    print("Délka strany c: " + str(strc) + " cm")
    if jeSestrojitelny(stra, strb, strc):
        print("Trojúhelník je sestrojitelný")
    else:
        print("Trojúhelník není sestrojitelný")
    print("Obvod trojúhelníku je " + str(getObvod(stra, strb, strc)) + " cm")
    obsah = getObsah(stra, strb, strc)
    if obsah >= 0:
        print("Obsah trojúhelníku je " + str(obsah) + " cm")
    else:
        print("Obsah nelze vypočítat (záporné číslo pod odmocninou)")
    if jePravouhly(stra, strb, strc):
        print("Trojúhelník je pravoúhlý")
    else:
        print("Trojúhelník není pravoúhlý")
    if jeRovnostranny(stra, strb, strc):
        print("Trojúhelník je rovnostranný")
    else:
        print("Trojúhelník není rovnostranný")
    if jeRovnoramenny(stra, strb, strc):
        print("Trojúhelník je rovnoramenný")
    else:
        print("Trojúhelník není rovnoramenný")


def test_delkaStrany():
    """Unit test for delkaStrany() function."""
    assert delkaStrany(14, 8, 3, 65) == 58.05
    assert (delkaStrany(47, 65, 3, 12) == 68.88) is True
    assert (delkaStrany(78, 63, 23, 14) == 0) is False


def test_getObvod():
    """Unit test for getObvod() function."""
    assert getObvod(23.45, 32.01, 41.34) == 96.8
    assert (getObvod(1.01, 2.35, 9.87) == 13.23) is True
    assert (getObvod(1.48, 7.63, 12.48) == 0) is False


def test_getObsah():
    """Unit test for getObsah() function."""
    assert getObsah(14, 17, 23) == 118.49
    assert (getObsah(8, 15, 34) >= 0) is False
    assert (getObsah(8, 15, 14) >= 0) is True
    assert (getObsah(8, 15, 14) == 55.31) is True


def test_jeSestrojitelny():
    """Unit test for jeSestrojitelny() function."""
    assert jeSestrojitelny(1, 88, 55) is False
    assert jeSestrojitelny(33, 3, 77) is False
    assert jeSestrojitelny(7777, 777, 7) is False
    assert jeSestrojitelny(76, 67, 55) is True


def test_jePravouhly():
    """Unit test for jePravouhly() function."""
    assert jePravouhly(25, 16, 9) is False
    assert jePravouhly(1, 7, 3) is False
    assert jePravouhly(78, 87, 123) is False
    assert jePravouhly(5, 3, 4) is True
    assert jePravouhly(3, 4, 5) is True
    assert jePravouhly(4, 5, 3) is True


def test_jeRovnostranny():
    """Unit test for jeRovnostranny() function."""
    assert jeRovnostranny(5, 4, 5) is False
    assert jeRovnostranny(7, 2, 3) is False
    assert jeRovnostranny(26, 58, 257) is False
    assert jeRovnostranny(5, 5, 5) is True
    assert jeRovnostranny(3, 3, 3) is True
    assert jeRovnostranny(25, 25, 25) is True


def test_jeRovnoramenny():
    """Unit test for jeRovnoramenny() function."""
    assert jeRovnoramenny(5, 1, 8) is False
    assert jeRovnoramenny(1, 2, 3) is False
    assert jeRovnoramenny(55, 88, 222) is False
    assert jeRovnoramenny(5, 5, 2) is True
    assert jeRovnoramenny(8, 4, 8) is True
    assert jeRovnoramenny(10, 10, 25) is True


if __name__ == "__main__":
    test_delkaStrany()
    test_getObvod()
    test_getObsah()
    test_jeSestrojitelny()
    test_jePravouhly()
    test_jeRovnostranny()
    test_jeRovnoramenny()
    trojuhelnik()
