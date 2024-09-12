"""Číselné soustavy."""

# Imports
import sys

__author__ = 'Marek Dolanský'
__version__ = '1.0.0'
__email__ = 'm1_dolansky@utb.cz'
__status__ = 'Work in progress'


def numberSelection():
    """Zadání čísla.

    Uživatel zadá číslo, které chce
    převést do jíné číselné soustavy
    """
    global n
    print('Zadejte kladné celé číslo v desítkové soustavě '
          '(Pro ukončení zadejte \"exit\"):')
    n = input()

    if n == 'exit':
        sys.exit('Program byl ukončen')

    while not str(n).isnumeric():
        print('Zadali jste neplatnou hodnotu:', n)
        print('Musíte zadat kladné celé číslo '
              '(Pro ukončení zadejte \"exit\"):')
        n = input()
        if n == 'exit':
            sys.exit('Program byl ukončen')

    while int(n) < 0:
        print('Zadali jste neplatnou hodnotu:', n)
        print('Musíte zadat kladné celé číslo '
              '(Pro ukončení zadejte \"exit\"):')
        n = input()
        if n == 'exit':
            sys.exit('Program byl ukončen')


def systemSelection():
    """Výběr cílové soustavy.

    Uživatel zadá číslo soustavy,
    do které chce převést dříve zadanou hodnotu
    """
    global s
    print('Vyberte soustavu, do které chcete číšlo převést '
          '(Pro ukončení zadejte \"exit\"):')
    print('1 - Dvojková')
    print('2 - Osmičková')
    print('3 - Šestnáctková')
    s = input()

    if s == 'exit':
        sys.exit('Program byl ukončen')

    while not str(s).isnumeric():
        print('Zadali jste neplatnou hodnotu:', s)
        print('Vyberte soustavu, do které chcete číšlo převést '
              '(Pro ukončení zadejte \"exit\"):')
        print('1 - Dvojková')
        print('2 - Osmičková')
        print('3 - Šestnáctková')
        s = input()
        if s == 'exit':
            sys.exit('Program byl ukončen')

    while not 1 <= int(s) <= 3:
        print('Zadali jste neplatnou hodnotu:', s)
        print('Vyberte soustavu, do které chcete číšlo převést '
              '(Pro ukončení zadejte \"exit\"):')
        print('1 - Dvojková')
        print('2 - Osmičková')
        print('3 - Šestnáctková')
        s = input()
        if s == 'exit':
            sys.exit('Program byl ukončen')


def decimalToBinary(decimal):
    """Převod do dvojkové soustavy.

    Unittest:
    >>> decimalToBinary(32)
    32 je ve dvojkové soustavě: 100000

    >>> decimalToBinary(37)
    37 je ve dvojkové soustavě: 100101

    >>> decimalToBinary(127)
    127 je ve dvojkové soustavě: 1111111
    """
    print(decimal, 'je ve dvojkové soustavě:', bin(decimal)[2:])


def decimalToOctal(decimal):
    """Převod do osmičkové soustavy.

    Unittest:
    >>> decimalToOctal(547)
    547 je v osmičkové soustavě: 1043

    >>> decimalToOctal(215)
    215 je v osmičkové soustavě: 327

    >>> decimalToOctal(7)
    7 je v osmičkové soustavě: 7
    """
    print(decimal, 'je v osmičkové soustavě:', oct(decimal)[2:])


def decimalToHexadecimal(decimal):
    """Převod do šestnáctkové soustavy.

    Unittest:
    >>> decimalToHexadecimal(255)
    255 je v šestnáctkové soustavě: ff

    >>> decimalToHexadecimal(847)
    847 je v šestnáctkové soustavě: 34f

    >>> decimalToHexadecimal(30412)
    30412 je v šestnáctkové soustavě: 76cc
    """
    print(decimal, 'je v šestnáctkové soustavě:', hex(decimal)[2:])


def switch(selection, n):
    """Metoda pro výběr soustavy.

    Unittest:
    >>> switch(1, 37)
    37 je ve dvojkové soustavě: 100101

    >>> switch(2, 24)
    24 je v osmičkové soustavě: 30

    >>> switch(3, 847)
    847 je v šestnáctkové soustavě: 34f
    """
    if selection == 1:
        decimalToBinary(n)
    elif selection == 2:
        decimalToOctal(n)
    elif selection == 3:
        decimalToHexadecimal(n)


def main():
    """Spuštění programu."""
    numberSelection()
    systemSelection()
    switch(int(s), int(n))


if __name__ == "__main__":
    main()
