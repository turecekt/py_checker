"""Toto je program pro nacteni bodu trojuhelniku v 2d prostoru.

Overi zda lze setrojit.
Jakou ma delku stran.
Jaky je jeho obvod a obsah.
Zda je nebo neni pravouhly.

"""
import math
import sys


def nacteni_bodu():
    """Nacteni Bodu.

    Funkce nacitajici body z konzole,
    ktera nasledne vola FCI vypis
    """
    while(True):
        vstup = input("Spustit program trojuhelnik A/N?: ")
        if(vstup == 'A' or vstup == 'a'):
            print("Zadej souradnice bodu x a y")
            xA = int(input("Zadaj souradnici x bodu A: "))
            yA = int(input("Zadaj souradnici y bodu A: "))
            xB = int(input("Zadaj souradnici x bodu B: "))
            yB = int(input("Zadaj souradnici y bodu B: "))
            xC = int(input("Zadaj souradnici x bodu C: "))
            yC = int(input("Zadaj souradnici y bodu C: "))
            vypis(xA, yA, xB, yB, xC, yC)
        elif(vstup == 'N' or vstup == 'n'):
            sys.exit()
        else:
            print("Zadaj Y alebo N")


def vypocet_strany(x0, y0, x1, y1):
    """Vypocet strany.

    Vypocita delku strany ze souradnic
    dvou zadanych bodu
    >>> vypocet_strany(1, 3, 3, 5)
    2.828
    """
    S = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
    return round(S, 3)


def sestrojitelny(Sa, Sb, Sc):
    """Test sestrojitelnosti.

    Overi zde je trojuhelnik mozne sestrojit
    >>> sestrojitelny( 4.243, 5.099, 2.828)
    Trojuhelnik lze setrojit
    True
    >>> sestrojitelny( 0, 5.099, 2.828)
    Trojuhelnik nelze setrojit
    False
    >>> 5+2 > 3
    True
    >>> 7+2 > 10
    False
    """
    if Sa + Sb > Sc and Sa + Sc > Sb and Sb + Sc > Sa:
        print("Trojuhelnik lze setrojit")
        return True
    else:
        print("Trojuhelnik nelze setrojit")
        return False


def obvod(Sa, Sb, Sc):
    """Vypocet obvodu trojuhelniku.

    Vypocita obvod trojuhelniku ze zadanych stran
    >>> obvod(1, 1, 1)
    3
    """
    return round(Sa+Sb+Sc, 3)


def obsah(Sa, Sb, Sc):
    """Vypocet osahu trojuhelniku.

    >>> obsah(4.243, 5.099, 2.828)
    6
    >>> obvod(4.243, 5.099, 2.828)/2
    6.085
    """
    s = obvod(Sa, Sb, Sc)/2
    return round(math.sqrt(s*(s-Sa)*(s-Sb)*(s-Sc)))


def pravouhly(Sa, Sb, Sc):
    """Test zda se jedna o pravouhly trojuhelnik.

    Overi zda nektery z uhlu je pravouhly
    >>> pravouhly(4.243, 5.099, 2.828)
    True
     >>> pravouhly(2.243, 5.099, 2.828)
     False
     >>> round(4**2 + 2**2)
     20
     >>> round(2**2 + 3**2)
     13
     >>> 2**2
     4
    """
    if ((round(Sc**2) == round(Sa**2 + Sb**2))
        or (round(Sa**2) == round(Sb**2 + Sc**2))
            or (round(Sb**2) == round(Sa**2 + Sc**2))):
        return True
    else:
        return False


def vypis(xA, yA, xB, yB, xC, yC):
    """Vypis hodnot do terminalu.

    >>> vypis(0, 0, 0, 0, 0, 0)
    Trojuhelnik nelze setrojit
    >>> vypis(1, 3, 3, 5, 6, 2)
    Trojuhelnik lze setrojit
    Delka strany a je:  4.243
    Delka strany b je:  5.099
    Delka strany c je:  2.828
    Obvod trojuhelniku je:  12.17
    Obsah trojuhelniku je:  6
    Trojuhelnik je pravouhly
    """
    Sa = vypocet_strany(xB, yB, xC, yC)
    Sb = vypocet_strany(xA, yA, xC, yC)
    Sc = vypocet_strany(xA, yA, xB, yB)
    check = sestrojitelny(Sa, Sb, Sc)

    if check is True:
        print("Delka strany a je: ", round(Sa, 3))
        print("Delka strany b je: ", round(Sb, 3))
        print("Delka strany c je: ", round(Sc, 3))
        print("Obvod trojuhelniku je: ", round(obvod(Sa, Sb, Sc), 3))
        print("Obsah trojuhelniku je: ", obsah(Sa, Sb, Sc))
        if pravouhly(Sa, Sb, Sc) is True:
            print("Trojuhelnik je pravouhly")
        else:
            print("Trojuhelnik neni pravouhly")
            pass
    else:
        pass


if __name__ == '__main__':
    """ Hlavni telo programu."""

    nacteni_bodu()


def test_obsah():
    """Testovani Funkce obsahu."""
    assert obsah(4.243, 5.099, 2.828) == 6
