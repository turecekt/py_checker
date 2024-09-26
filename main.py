""".

Funkce římské číslice přebýrá celé číslo,
rozdělí ho na číslice definované v listu a přepíše je danou string hodnotu,
která je k číslu přiřazena, na konci vrací string list.

"""


def rimskeCislice(cislo):
    """Funkce s parametrem cislo je datového typu int."""
    # list, deklarovaný jako key:"value", o datových typech int:"string"
    numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
                90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    # proměnná typu list (Literal['']), uloží hodnotu v římských číslicích
    output = ""
    # i - počítadlo, cislice - nabývá hodnoty prvku z listu numerals
    # funkce sorted má dva argumenty: list, reverse - bool, určuje pořadí prvků
    # vrací nový list s prvky v sestupném pořadí, pokud je reverse = True
    for i, cislice in sorted(numerals.items(), reverse=True):
        # cyklus běží do doby, než zadané číslo je větší nebo rovno počítadlu
        while cislo >= i:
            # output je list, ukládá hodnoty z proměnné cislice typu string
            output += cislice
            # zadané číslo se snižuje o 1
            cislo -= i
    # funkce vrací list
    return output


rimskeCislice(55)
