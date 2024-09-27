"""
Projekt ČETNOST ZNAKŮ.

Autori:Petr Slavik, Radek Kratochvil.
"""


def PocetZnak(vstup):
    """Informace o celkovém počtu znaků."""
    endis = "#"
    if vstup.endswith(endis):
        data = (vstup.replace(" ", "")).upper()
        pocet_char = len(data)-1
        return(pocet_char)
    elif vstup.endswith('.txt'):
        with open(vstup) as text_file:
            data = text_file.read().upper().replace(" ", "")
            pocet_char = len(data)-1
            valid = data.endswith(endis)
            if valid:
                return(pocet_char)
            else:
                return(0)
    else:
        return(0)


def MaxZnak(vstup):
    """Informace o nejčastějším znaku."""
    endis = "#"
    if vstup.endswith(endis):
        charStore = {}
        data = (vstup.replace(" ", "")).upper()
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1
        resMax = max(charStore.values())
        res = [key for key in charStore if charStore[key] == resMax]
        return(res)
    elif vstup.endswith('.txt'):
        with open(vstup) as text_file:
            data = text_file.read().upper().replace(" ", "")
            valid = data.endswith(endis)
            if valid:
                charStore = {}
                for sChar in data:
                    if sChar in charStore:
                        charStore[sChar] += 1
                    else:
                        charStore[sChar] = 1
                resMax = max(charStore.values())
                res = [key for key in charStore if
                       charStore[key] == resMax]
                return(res)
            else:
                return(0)
    else:
        return(0)


def MinZnak(vstup):
    """Informace o nejméně častém znaku."""
    endis = "#"
    if vstup.endswith(endis):
        charStore = {}
        data = (vstup.replace(" ", "")).upper()
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1
        resMin = min(charStore.values())
        res = [key for key in charStore if charStore[key] == resMin]
        return(res)

    elif vstup.endswith('.txt'):
        with open(vstup) as text_file:
            data = text_file.read().upper().replace(" ", "")
            valid = data.endswith(endis)
            if valid:
                charStore = {}
                for sChar in data:
                    if sChar in charStore:
                        charStore[sChar] += 1
                    else:
                        charStore[sChar] = 1
                resMin = min(charStore.values())
                res = [key for key in charStore if
                       charStore[key] == resMin]
                return(res)
            else:
                return(0)
    else:
        return(0)


def PrumerKazdyZnak(vstup):
    """Informace o průměrné četnosti."""
    endis = "#"
    if vstup.endswith(endis):
        data = (vstup.replace(" ", "")).upper()
        pocet_char = len(data)
        alpha = ["A", "B", "C", "D", "E", "F", "G",
                 "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T", "U",
                 "V", "W", "X", "Y", "Z"]
        for iChar in alpha:
            pocet = data.count(iChar)/pocet_char*100
            if data.count(iChar) > 0:
                print(iChar, "vyskyt je", f"{pocet:.2f}", "%")
    elif vstup.endswith('.txt'):
        with open(vstup) as text_file:
            data = text_file.read().upper().replace(" ", "")
            pocet_char = len(data)
            valid = data.endswith(endis)
            if valid:
                alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                         "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                         "S", "T", "U", "V", "W", "X", "Y", "Z"]
                for iChar in alpha:
                    pocet = data.count(iChar)/pocet_char*100
                    if data.count(iChar) > 0:
                        print(iChar, "vyskyt je", f"{pocet:.2f}", "%")
            else:
                return(0)
    else:
        return(0)


def PocetKazdyZnak(vstup):
    """Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)."""
    endis = "#"
    if vstup.endswith(endis):
        data = (vstup.replace(" ", "")).upper()
        charStore = {}
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1
        return(charStore)
    elif vstup.endswith('.txt'):
        with open(vstup) as text_file:
            data = text_file.read().upper().replace(" ", "")
            valid = data.endswith(endis)
            if valid:
                charStore = {}
                for sChar in data:
                    if sChar in charStore:
                        charStore[sChar] += 1
                    else:
                        charStore[sChar] = 1
                return(charStore)
            else:
                return(0)
    else:
        return(0)
