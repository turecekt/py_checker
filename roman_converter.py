"""Arabic Numbers to Roman Numerals Converter V1.0.

Created on Sun Nov  1 14:14:51 2020

@author: Ladislav Tomecek

"""


def toRoman(iArabicNum):
    """Convert Arabic Numbers to Roman Numerals.

    Args:
        iArabicNum (int): an integer
    Returns:
        sRomanNum (str): a string of Roman Numerals

    >>> toRoman(10)
    'X'
    """
    value = [1000, 900, 500, 400,
             100, 90, 50, 40, 10,
             9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD",
              "C", "XC", "L", "XL", "X",
              "IX", "V", "IV", "I"]
    sRomanNum = ''
    i = 0
    while iArabicNum > 0:
        for x in range(iArabicNum // value[i]):
            sRomanNum += symbol[i]
            iArabicNum -= value[i]
        i += 1
    return sRomanNum


def test_toRoman():
    """Test convertion of Arabic Numbers to Roman Numerals."""
    # all basic symbols are used exactly once
    assert toRoman(1444) == "MCDXLIV"


if __name__ == "__main__":
    print("Převodník na římská čísla V1.0")
    vstup = int(input("Zadej celé číslo: "))
    print(toRoman(vstup))
