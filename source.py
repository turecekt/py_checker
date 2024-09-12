"""Import knihovny math."""
import math
from Bod import Bod


def vrat_bod(bod, debug=False):
    """Zajistuje vstup od uzivatele ve forme bodu.

    Args:
        - bod - vstup funkce
        - debug - testovací důvod

    Returns:
        - vystup - zadane parametry uzivatelem
    """
    x = 0
    y = 0
    if(not debug):
        n = f'Zadej bod {bod} souradnici'
        while True:
            try:
                x = float(input(f'{n} x: ').strip())
                break
            except TypeError:
                print('Je treba zadat ciselnou hodnotu')

        while True:
            try:
                y = float(input(f'{n} y: ').strip())
                break
            except TypeError:
                print('Je treba zadat ciselnou hodnotu')

    return Bod(x, y)


def pythagorova_veta(bod):
    """Funkce pocita pythagorovu vetu pomoci bodu.

    Args:
        - bod - vstup funkce

    Returns:
        - vystup - vysledek pythagorovy vety
    """
    x = math.sqrt((bod.x*bod.x)+(bod.y*bod.y))
    return x


def secteni_souradnic(bod1, bod2):
    """Secte souradnice bodu zadanych uzivatelem.

    Args:
        - bod1, bod2 - vstup funkce

    Returns:
        - vystup - vysledek souctu dvou bodu
    """
    return Bod(abs(bod1.x - bod2.x), abs(bod1.y - bod2.y))


def delka_strany(bod1, bod2):
    """Spocita delku strany z bodu zadanych uzivatelem.

    Args:
        - bod1, bod2 - vstup funkce

    Returns:
        - vystup - vysledek delky strany
    """
    return pythagorova_veta(secteni_souradnic(bod1, bod2))


def sestrojitelny(a, b, c):
    """Overi zda je trojuhelnik sestrojitelny na zaklade delek stran.

    Args:
        - a, b, c - vstup funkce

    Returns:
        - vystup - vysledek boolean vysledku sestrojitelnosti
    """
    return (a + b > c and b + c > a and a + c > b)


def obvod(a, b, c):
    """Spocita obvod trojuhelnik pomoci delek stran.

    Args:
        - a, b, c - vstup funkce

    Returns:
        - vystup - vysledek obvodu trojuhelniku
    """
    return a + b + c


def obsah(a, b, c):
    """Spocita obsah trojuhelnik pomoci delek stran.

    Args:
        - a, b, c - vstup funkce

    Returns:
        - vystup - vysledek obsahu trojuhelniku
    """
    s = (a + b + c)/2
    return math.sqrt(s * ((s - a) * (s - b) * (s - c)))


def pravouhly(a, b, c):
    """Overi zda je trojuhelnik pravouhly.

    Args:
        - a, b, c - vstup funkce

    Returns:
        - vystup - vysledek boolean vysledku pravouhlosti
    """
    tmp_r = c
    tmp_l1 = a
    tmp_l2 = b
    if(a > tmp_r):
        tmp_l1 = tmp_r
        tmp_r = a
    if(b > tmp_r):
        tmp_l2 = tmp_r
        tmp_r = b

    right = math.pow(tmp_r, 2)
    left = (math.pow(tmp_l1, 2) + math.pow(tmp_l2, 2))
    return right == left


if __name__ == '__main__':
    a = vrat_bod('A')
    b = vrat_bod('B')
    c = vrat_bod('C')

    ab = delka_strany(a, b)
    bc = delka_strany(b, c)
    ac = delka_strany(a, c)
    print()
    if (sestrojitelny(ab, bc, ac)):
        print("Trojuhelnik je sestrojitelny")
    else:
        print("Trojuhelnik neni sestrojitelny")
    print()
    print(f"Strana a: {bc}\n\rStrana b: {ac}\n\rStrana c: {ab}")
    print()
    print(f"Obvod: {obvod(ab,ac,bc)}\n\rObsah: {obsah(ab,ac,bc)}")
    print()
    if (pravouhly(ab, bc, ac)):
        print("Trojuhelnik je pravouhly")
    else:
        print("Trojuhelnik neni pravouhly")


def test_pythagorova_veta():
    """Test Pythagorovy vety."""
    assert round(pythagorova_veta(Bod(3, 4)), 2) == 5.0


def test_pythagorova_veta2():
    """Test Pythagorovy vety."""
    assert round(pythagorova_veta(Bod(3, 3)), 2) == 4.24


def test_secteni_souradnic():
    """Test souctu souradnic."""
    bod = secteni_souradnic(Bod(3, -2), Bod(-1, -2))
    assert bod.x == 4.0 and bod.y == 0.0


def test_secteni_souradnic2():
    """Test souctu souradnic."""
    bod = secteni_souradnic(Bod(4, 2), Bod(-2, -0))
    assert bod.x == 6.0 and bod.y == 2.0


def test_delka_strany():
    """Test delky stran."""
    assert delka_strany(Bod(2, 2), Bod(-1, -2)) == 5.0


def test_delka_strany2():
    """Test delky stran."""
    assert round(delka_strany(Bod(3, 2), Bod(0, -1)), 2) == 4.24


def test_sestrojitelny():
    """Test sestrojitelnosti."""
    assert sestrojitelny(3, 4, 5)


def test_sestrojitelny2():
    """Test sestrojitelnosti."""
    assert sestrojitelny(10, 6, 8)


def test_obvod():
    """Test obvodu."""
    assert obvod(3, 4, 5) == 12.0


def test_obvod2():
    """Test obvodu."""
    assert obvod(10, 6, 8) == 24.0


def test_obsah():
    """Test obsahu."""
    assert obsah(3, 4, 5) == 6.0


def test_obsah2():
    """Test obsahu."""
    assert obsah(10, 8, 6) == 24.0


def test_vrat_bod():
    """Test vraceni bodu."""
    assert vrat_bod('B', True)


def test_pravouhly():
    """Test pravouhlosti."""
    assert pravouhly(3, 4, 5)


def test_pravouhly2():
    """Test pravouhlosti."""
    assert pravouhly(8, 10, 6)
