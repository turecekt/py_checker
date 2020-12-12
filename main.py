"""V�pis morseovy abecedy."""

morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.'}
"""
text -> prom�nn�, do kter� si ulo��me
originaln� text k p�elo�en�
cyklus for -> p�eklad� pismeno ve zpr�v�
podminka if    -> pokud pismeno nen� ve zpr�v� mezera,
najdu si v poli morse_code
odpovidaj�c� znak k pismenu a p�id�m mezeru
        else   -> pokud pismeno
        ve zpr�v� je mezera, p�id�m mezeru
"""


def zasifrovat(zprava):
    """Funkce zasifrovat -> slou�� k za�ifrov�n� zpr�vy pomoc�.

    morseovy abecedy funkce vrac� za�ifrovan� text.
    """
    text = ''
    for pismeno in zprava:
        if pismeno != ' ':
            text += morse_code[pismeno] + ' '
        else:
            text += ' '
    return text


"""
zprava -> p�idan� mezery na konec zpr�vy k p�istupu
posledn�mu znaku morseovy abecedy
 ve zprave protoze index zacina na 0
prelozeny_text -> promenna
ve ktere je ulozeny finalni text z morseovy abecedy
i -> promenna
ktera nam kontroluje kolik je mezer ve zprave
podminka if     -> pokud ve zprave neni mezera
do promenne prelozit_text
pridam pismena z morseovy abecedy
         else   -> pokud ve zprave je mezera,
         pokud je i = 1 tak to znamena ze je ve zprave novy znak
         if     -> pokud i = 2 znamena to ze je ve
         zprave nove slovo a pridam do promenne prelozeny_text mezeru
"""


def odsifrovat(zprava):
    """Funkce odsifrovat -> slouzi k odsifrovani zpravy.

    pomoci morseovy abecedy funkce vraci odsifrovany text.
    """
    zprava += ' '

    prelozit_text = ''
    prelozeny_text = ''

    for pismeno in zprava:

        if (pismeno != ' '):
            i = 0

            prelozit_text += pismeno

        else:
            i += 1

            if i == 2:
                prelozeny_text += ' '

            else:

                prelozeny_text += list(morse_code.keys())[
                    list(morse_code.values()).index(prelozit_text)]
                prelozit_text = ''

    return prelozeny_text


def testzasifrovat():
    """Unit test funkce zasifrovat."""
    zprava = "Ahoj svete"
    assert zasifrovat(zprava.upper()) == ".- .... --- .---  ... ...- . - . "


def testodsifrovat():
    """Unit test funkce odsifrovat."""
    zprava = ".- .... --- .---  ... ...- . - ."
    assert odsifrovat(zprava) == "AHOJ SVETE"


def main():
    """Funkce main je hlavni funce ktera nam umozni cely program spustit."""
    print("Zadejte ��slo 1 pro �ifrov�n� nebo ��slo 2 pro de�ifrov�n�: ")
    vyber = input()
    if vyber == "1":
        print("Zadejte text pro za��frov�n�: ")
        zprava = input()
        vysledek = zasifrovat(zprava.upper())
        print(vysledek)
    if vyber == "2":
        print("Zadejte text pro de��frov�n� a mezi "
              "jednotliv�mi p�smeny morseovy abecedy d�vejte mezery: ")
        zprava = input()
        vysledek = odsifrovat(zprava)
        print(vysledek)


"""Provede hlavni funkci."""
if __name__ == '__main__':
    main()
