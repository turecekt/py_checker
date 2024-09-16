"""Program pro převod čísla z desítkové soustavy.

Program obsahuje 1 funkci: prevod()
"""
# -*- coding: utf-8 -*-
import math as m


def prevod(c, s):
    """Funkce prevod převádí zadané číslo z 10-ové soustavy na zvolenou soustavu.

    Args:
        - c - kladné celé číslo v desítkové soustavě
        - s - 2, 8, 12 nebo 16 - cílová soustava, do které chceme převést
        číslo c

    Returns:
        - output - řetězec vracející číslo v cílové číselné soustavě
    """
    # vytvoření prázdného řetězce "vysledek" pro uložení výsledné hodnoty
    vysledek = ""
    # cyklus, ve kterém číslo dělíme soustavou, dokud se nerovná 0
    while(c/s != 0):
        # ukládání zbytku po dělení do proměnné "zbytek"
        zbytek = c % s
        # podmínka pro odlišné ukládání zbytku pro 16-ovou soustavu
        if zbytek < 10:
            vysledek = vysledek + str(zbytek)
        elif zbytek == 10:
            vysledek = vysledek + "A"
        elif zbytek == 11:
            vysledek = vysledek + "B"
        elif zbytek == 12:
            vysledek = vysledek + "C"
        elif zbytek == 13:
            vysledek = vysledek + "D"
        elif zbytek == 14:
            vysledek = vysledek + "E"
        elif zbytek == 15:
            vysledek = vysledek + "F"

        # přepsání hodnoty do proměnné "c" po vydělení a zaokrouhlení
        c = m.floor(c/s)

    # Výsledek otočen a vypsán
    return vysledek[::-1]
