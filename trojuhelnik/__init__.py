"""Výpočet vlastností trojuhelníka."""
import math
import sys


def ask(prompt, default):
    """Funkce pro zachycení souřadnic zadaných uživatele."""
    vstup = input(prompt)
    try:
        val = int(vstup)
    except ValueError:
        print("Špatně zadaná hodnota.")
        print("Použije se defaultní hodnota - ", default)
        val = default
    return val


def sestrojitelnost(Triangle):
    """Funkce sestrojitelnost vyhodnotí je-li trojuhelník sestrojitelný."""
    return True


def delky_stran(Triangle):
    """Funkce delky_stran vrací list délek stran trojuhelníku."""
    A = Triangle[0]
    B = Triangle[1]
    C = Triangle[2]
    a = abs(math.sqrt((B[0] - C[0])**2+(B[1] - C[1])**2))
    b = abs(math.sqrt((C[0] - A[0])**2+(C[1] - A[1])**2))
    c = abs(math.sqrt((A[0] - B[0])**2+(A[1] - B[1])**2))
    sides = [a, b, c]
    return sides


def informace(Triangle):
    """Funkce vypíše nejdelší a nejkratší stranu."""
    sides = delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))
    max = a
    min = a
    # Nejdelsi strana
    if b > max:
        max = b
    if c > max:
        max = c
    # Nejkratsi strana
    if b < min:
        min = b
    if c < min:
        min = c
    # Vypis max
    if (max == a):
        print("Nejdelsi strana: a = "+str(max))
    if (max == b):
        print("Nejdelsi strana: b = "+str(max))
    if (max == c):
        print("Nejdelsi strana: c = "+str(max))
    # Vypis min
    if (min == a):
        print("Nejkratsi strana: a = "+str(min))
    if (min == b):
        print("Nejkratsi strana: b = "+str(min))
    if (min == c):
        print("Nejkratsi strana: c = "+str(min))
    return (min, max)


def obvod(Triangle):
    """Funkce obvod vrací obvod trojuhelníku."""
    sides = delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    obvod = a + b + c
    print("Obvod: "+str(obvod))
    return obvod


def obsah(Triangle):
    """Funkce obsah vrací obsah trojuhelníku."""
    sides = delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    Obvod = a + b + c
    s = Obvod / 2
    S = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Obsah: "+str(S))
    return S


def parvouhlost(Triangle):
    """Funkce pravouhlost vyhodnotí je-li daný trojuhelník pravoúhlý."""
    sides = delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (c == math.sqrt(a**2 + b**2)):
        print("Trojuhelnik je pravouhly")
        return False
    else:
        print("Trojuhelnik neni pravouhly")
        return True


"""Zaznamenat vstup z konzole"""
print("Zadejte souřadnice trojuhelníku\n")
A = (0, 0)
B = (3, 0)
C = (0, 4)


if len(sys.argv) > 1:   # Zadal-li uživatel právě jeden argument = "input"
    print(sys.argv[1])  # pak se přepne do interaktivního módu
    if sys.argv[1] == "input":
        A = (ask("bod A - souřadnice x:", 0), ask("bod A - souřadnice y:", 0))
        B = (ask("bod B - souřadnice x:", 3), ask("bod B - souřadnice y:", 0))
        C = (ask("bod C - souřadnice x:", 0), ask("bod C - souřadnice y:", 4))

Triangle = [A, B, C]
print("\nZadali jste trojuhelník se souřadnicemi:")
print("A: ", A)
print("B: ", B)
print("C: ", C)
