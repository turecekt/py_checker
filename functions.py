"""Funkce."""

# Import knihovny math pro matematické funkce
import math


# Funkce pro otestování vstupu, zda je vstupní hodnota od uživatele číslo
def soJeCi(xA, xB, xC, yA, yB, yC):
    """Proměnná pro vrácení hodnoty funkce."""
    zkouskaSouradnic = 0
    # Zkouška jestli jsou vstupní hodnoty číslo.
    try:
        xA = float(xA.replace(',', '.'))
        yA = float(yA.replace(',', '.'))
        xB = float(xB.replace(',', '.'))
        yB = float(yB.replace(',', '.'))
        xC = float(xC.replace(',', '.'))
        yC = float(yC.replace(',', '.'))
        zkouskaSouradnic = 1
    except ValueError:
        zkouskaSouradnic = 0

    """Podmínka, která vrátí hodnotu 1, když vstupní hodnoty jsou čísla."""
    if zkouskaSouradnic == 1:
        return 1
    else:
        return 0


# Funkce pro výpočet délky strany AB trojúhelníku
def delkaStranyAB(xA, xB, yA, yB):
    """Funkce vrátí velikost délky strany AB."""
    return math.sqrt(((xB-xA)**2)+(yB-yA)**2)


# Funkce pro výpočet délky strany BC trojúhelníku
def delkaStranyBC(xB, xC, yB, yC):
    """Funkce vrátí velikost délky strany BA."""
    return math.sqrt(((xC-xB)**2)+(yC-yB)**2)


# Funkce pro výpočet délky strany AC trojúhelníku
def delkaStranyAC(xA, xC, yA, yC):
    """Funkce vrátí velikost délky strany AC."""
    return math.sqrt(((xC-xA)**2)+(yC-yA)**2)


# Funkce pro výpočet obvodu trojůhelníku
def obvodTroj(xA, xB, xC, yA, yB, yC):
    """Deklarace proměnných a vložení hodnot."""
    stranaAB = math.sqrt(((xB-xA)**2)+(yB-yA)**2)
    stranaBC = math.sqrt(((xC-xB)**2)+(yC-yB)**2)
    stranaAC = math.sqrt(((xC-xA)**2)+(yC-yA)**2)
    """Funkce vráti délku obvodu."""
    return stranaAB + stranaBC + stranaAC


# Funkce pro výpočet obsahu trojůhelníku
def obsahTroj(xA, xB, xC, yA, yB, yC):
    """Deklarace proměnných a vložení hodnot."""
    strAB = math.sqrt(((xB-xA)**2)+(yB-yA)**2)
    strBC = math.sqrt(((xC-xB)**2)+(yC-yB)**2)
    strAC = math.sqrt(((xC-xA)**2)+(yC-yA)**2)
    """Výpočet poloviny obvodu"""
    pulO = (strAB + strBC + strAC) / 2
    """Funkce vrátí velikost obsahu."""
    return math.sqrt(pulO * (pulO - strAB) * (pulO - strBC) * (pulO - strAC))


# Funkce pro zkoušku, jestli je trojúhelník pravoúhlý
def zkPravouhlosti(xA, xB, xC, yA, yB, yC):
    """Deklarace proměnných a vložení hodnot."""
    strAB = math.sqrt(((xB-xA)**2)+(yB-yA)**2)
    strBC = math.sqrt(((xC-xB)**2)+(yC-yB)**2)
    strAC = math.sqrt(((xC-xA)**2)+(yC-yA)**2)
    """Podmínka, která zjistí, která strana trojúhelníku je přepona."""
    if strAB > strBC and strAB > strAC:
        """Vypočítání odmocnin součtu odvěsen podle pythagorova vzorce"""
        odvesnyBCAC = math.sqrt((strBC**2) + (strAC**2))
        """Podmínka jestli je trojúhelník pravoúhlý."""
        if strAB == odvesnyBCAC:
            """Funkce vrátí hodnotu 1 pokud je pravoúhlý."""
            return 1
        else:
            """Funkce vrátí hodnotu 0 pokud není pravoúhlý"""
            return 0
    elif strBC > strAB and strBC > strAC:
        """Vypočítání odmocnin součtu odvěsen podle pythagorova vzorce"""
        odvesnyABAC = math.sqrt((strAB**2) + (strAC**2))
        """Podmínka jestli je trojúhelník pravoúhlý."""
        if strBC == odvesnyABAC:
            """Funkce vrátí hodnotu 1 pokud je pravoúhlý."""
            return 1
        else:
            """Funkce vrátí hodnotu 0 pokud není pravoúhlý"""
            return 0
    else:
        """Vypočítání odmocnin součtu odvěsen podle pythagorova vzorce"""
        odvesnyABBC = math.sqrt((strAB**2) + (strBC**2))
        """Podmínka jestli je trojúhelník pravoúhlý."""
        if strAC == odvesnyABBC:
            """Funkce vrátí hodnotu 1 pokud je pravoúhlý."""
            return 1
        else:
            """Funkce vrátí hodnotu 0 pokud není pravoúhlý"""
            return 0
