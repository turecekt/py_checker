"""
Trojuholnik.

Program si vyziada suradnice 3 bodov,
nasledne zisti dlzky stran, zostrojitelnost, pravouhlost, obvod a obsah
"""
import math
import sys


def vypocetStrany(x1, y1, x2, y2):
    """Vypocita vzdialenost dvoch bodov.

    >>> vypocetStrany(0, 0, 0, 2)
    2.0
    """
    strana = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return strana


def zostrojitelnost(a, b, c):
    """
    Zisti zostrojitelnost trojuholnika zo zadanych 3 stran.

    >>> zostrojitelnost(5, 6, 7)
    True
    """
    if((a+b > c) and (a+c) > b and (b+c) > a):
        return True
    else:
        return False


def pravouhlost(a, b, c):
    """Zisti pravouhlost trojuholnika zo zadanych troch stran."""
    if((a > 0 and b > 0 and c > 0)
       and (a**2 == b**2+c**2 or b**2 == c**2+a**2 or c**2 == a**2+b**2)):
        return "Je pravouhly"
    else:
        return "Nie je pravouhly"


def obvod(a, b, c):
    """
    Vrati obvod trojuholnika.

    >>> obvod(4, 5, 8)
    17
    """
    return a + b + c


def obsah(a, b, c):
    """
    Vypocita obsah trojuholnika.

    Pouzijeme Heronov vzorec.
    """
    if(zostrojitelnost(a, b, c)):
        p = (a + b + c) / 2
        obsah = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 3)
        return obsah


def vstup():
    """
    Komunikacia s uzivatelom.

    Uzivatel ma na vyber vypocet alebo ukoncenie programu.
    V pripade volby vypoctu, program vyzve uzivatela,
    aby zadal suradnnice 3 bodov
    """
    while(True):
        vstup = input("Vypocitat trojuholnik [Y/N]: ")
        if(vstup == 'Y'):
            print("Zadaj suradnice 3 bodov: ")
            x1 = int(input("Zadaj x1: "))
            y1 = int(input("Zadaj y1: "))
            x2 = int(input("Zadaj x2: "))
            y2 = int(input("Zadaj y2: "))
            x3 = int(input("Zadaj x3: "))
            y3 = int(input("Zadaj y3: "))
            vypis(x1, y1, x2, y2, x3, y3)
        elif(vstup == 'N'):
            sys.exit()
        else:
            print("Zadaj Y alebo N")


def vypis(x1, y1, x2, y2, x3, y3):
    """
    Vypise vypocitane hodnoty a vlastnosti potencialneho trojuholnika.

    Dlzky stran, Zostrojitelnost, Obvod, Obsah, Pravouhlost

    >>> vypis(0, 0, 1, 1, 2, 2)
    Dlzky stran:
    1.41
    1.41
    2.83
    Trojuholnik sa neda zostrojit

    >>> vypis(0, 0, 1, 0, 0, 1)
    Dlzky stran:
    1.00
    1.41
    1.00
    Trojuholnik sa da zostrojit
    Obvod:
    3.41
    Obsah:
    0.50
    Nie je pravouhly
    """
    a = vypocetStrany(x1, y1, x2, y2)
    b = vypocetStrany(x2, y2, x3, y3)
    c = vypocetStrany(x3, y3, x1, y1)
    print("Dlzky stran:")
    print("{:.2f}".format(a))
    print("{:.2f}".format(b))
    print("{:.2f}".format(c))
    if(zostrojitelnost(a, b, c)):
        print("Trojuholnik sa da zostrojit")
        print("Obvod:")
        print("{:.2f}".format(obvod(a, b, c)))
        print("Obsah:")
        print("{:.2f}".format(obsah(a, b, c)))
        print(pravouhlost(a, b, c))
    else:
        print("Trojuholnik sa neda zostrojit")


if __name__ == '__main__':
    vstup()


def test_obvod():
    """Testuje funkciu obvod."""
    assert obvod(6, 3, 4) == 13


def test_obsah():
    """Testuje funkciu obsah."""
    assert obsah(1.00, 1.41, 1.0) == 0.50


def test_pravouhlost():
    """Testuje funkciu pravouhlost."""
    assert pravouhlost(1.00, 1.41, 2) == "Nie je pravouhly"
