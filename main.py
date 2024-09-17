"""
Tento program zjistuje jestli lze sestrojit trojuhelnik.

Pokud ano, tak se vypocita delka jeho stran, obsah, obvod
a jestli je pravouhly.
Program prijima souradnice bodu A,B,C z konzole a vypisuje vysledky na konzoli.

Tvurce: Tomas Blaho
"""

from math import sqrt


# PyTest sekce ------------------------------
def test_obvod():
    """Test obvod()."""
    assert obvod(3, 4, 5) == 12
    assert obvod(5, 4, 3) == 12
    assert obvod(3, 5, 4) == 12


def test_obsah():
    """Test obsah()."""
    assert obsah(3, 4, 5) == 6
    assert obsah(5, 4, 3) == 6
    assert obsah(3, 5, 4) == 6


def test_pravouhelnost():
    """Test pravouhelnost()."""
    assert pravouhelnost(3, 4, 5) is True
    assert pravouhelnost(5, 4, 3) is True
    assert pravouhelnost(3, 5, 4) is True


def test_sestrojitelnost():
    """Test sestrojitelnost()."""
    assert sestrojitelnost(3, 4, 5) is True
    assert sestrojitelnost(5, 4, 3) is True
    assert sestrojitelnost(4, 5, 3) is True


def test_sAB():
    """Test sAB()."""
    assert sAB(9, 12, 12, 16) == 5


def test_sBC():
    """Test sBC()."""
    assert sBC(9, 12, 12, 16) == 5


def test_sCA():
    """Test sCA()."""
    assert sCA(9, 12, 12, 16) == 5
# PyTest konec -----------------------------


def sestrojitelnost(ab, bc, ca):
    """
    Funkce zjistuje jestli lze sestrojit trojuhelnik.

    Vraci:
    true = trojuhelnik lze sestrojit
    false = trojhelnik nelze sestrojit
    """
    lze = ab + bc > ca and bc + ca > ab and ab + ca > bc

    return lze


def obsah(ab, bc, ca):
    """
    Funkce pocita obsah trojuhelniku.

    Vraci:
    float s vypocitanou hodnotou
    """
    s = (ab + bc + ca) / 2

    return sqrt(s * (s - ab) * (s - bc) * (s - ca))


def obvod(ab, bc, ca):
    """
    Funkce pocita obvod trojuhelniku.

    Vraci:
    float s vypocitanou hodnotou
    """
    return ab + bc + ca


def pravouhelnost(ab, bc, ca):
    """
    Funkce zjistuje jesli je trojuhelnik pravouhly.

    Vraci:
    true = trojuhelnik je pravouhlu
    false = trojuhelnik neni pravouhlu
    """
    nejdelsi = max(ab, bc, ca)

    if nejdelsi == ca:
        je = float("{:.3f}".format(ca ** 2)) == \
             float("{:.3f}".format(ab ** 2 + bc ** 2))
    elif nejdelsi == bc:
        je = float("{:.3f}".format(bc ** 2)) == \
             float("{:.3f}".format(ab ** 2 + ca ** 2))
    elif nejdelsi == ab:
        je = float("{:.3f}".format(ab ** 2)) == \
             float("{:.3f}".format(bc ** 2 + ca ** 2))

    return je


def sAB(ax, ay, bx, by):
    """
    Funkce pocita delku strany AB.

    Vraci:
    float s vypocitanou hodnotou
    """
    return sqrt(((int(bx) - int(ax)) ** 2) + ((int(by) - int(ay)) ** 2))


def sBC(bx, by, cx, cy):
    """
    Funkce pocita delku strany BC.

    Vraci:
    float s vypocitanou hodnotou
    """
    return sqrt(((int(cx) - int(bx)) ** 2) + ((int(cy) - int(by)) ** 2))


def sCA(ax, ay, cx, cy):
    """
    Funkce pocita delku strany CA.

    Vraci:
    float s vypocitanou hodnotou
    """
    return sqrt(((int(ax) - int(cx)) ** 2) + ((int(ay) - int(cy)) ** 2))


if __name__ == '__main__':
    # Zkouska cisel jestli jsou ve spravnem tvaru.
    try:
        # Program pozaduje uzivatelsky vstup.
        Ax = int(input('Napis souradnici x bodu A: '))
        Ay = int(input('Napis souradnici y bodu A: '))
        Bx = int(input('Napis souradnici x bodu B: '))
        By = int(input('Napis souradnici y bodu B: '))
        Cx = int(input('Napis souradnici x bodu C: '))
        Cy = int(input('Napis souradnici y bodu C: '))
    except Exception:
        # Nejsou ve spravnem tvaru. Program skoci na konec.
        print('Cisla byla zadana ve spatnem tvaru! Zadej pouze cela cisla.')
    else:
        # Jsou ve spravnem tvaru.
        # Zde se pocita delka sran AB, BC, CA.
        AB = sAB(Ax, Ay, Bx, By)
        BC = sBC(Bx, By, Cx, Cy)
        CA = sCA(Ax, Ay, Cx, Cy)

        # Vystup pozadovany v zadani.
        if sestrojitelnost(AB, BC, CA):
            print('Trojuhelnik lze sestrojit.')

            print('Strana AB je dlouha: ', AB)
            print('Strana BC je dlouha: ', BC)
            print('Strana CA je dlouha: ', CA)

            print('Obsah je: ', obsah(AB, BC, CA),
                  ' a obvod je: ', obvod(AB, BC, CA))

            if pravouhelnost(AB, BC, CA):
                print('Trojuhelnik je pravouhly.')
            else:
                print('Trojuhelnik neni pravouhly.')
        else:
            print('Trojuhelnik nelze sestrojit.')

    # Konec. Zde program ceka na uzivatelsky vstup k ukonceni.
    input('Zmackni Enter k zavreni programu.')
