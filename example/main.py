"""Rimske cislice."""

__author__ = 'Soňa Palatá'
__version__ = '1.0.0'
__email__ = 's_palata@utb.cz'
__status__ = 'Done'


def parseToRomanNumeral(number):
    """Return parsed inserted int as Roman Numeral.

    Parameters:
    number (int): An input number

    Returns:
    result_string (str): Parsed number as Roman Numerals in string format
    """
    result_string = ""
    number_as_int = int(number)

    if number_as_int >= 1000:
        m_value = number_as_int / 1000
        for x in range(int(m_value)):
            result_string = result_string + "M"
            number_as_int -= 1000

    if number_as_int >= 500:
        if str(number_as_int).startswith('9'):
            result_string = result_string + "CM"
            number_as_int -= 900
        else:
            d_value = number_as_int / 500
            for x in range(int(d_value)):
                result_string = result_string + "D"
                number_as_int -= 500

    if number_as_int >= 100:
        if str(number_as_int).startswith('4'):
            result_string = result_string + "CD"
            number_as_int -= 400
        else:
            c_value = number_as_int / 100
            for x in range(int(c_value)):
                result_string = result_string + "C"
                number_as_int -= 100

    if number_as_int >= 50:
        if str(number_as_int).startswith('9'):
            result_string = result_string + "XC"
            number_as_int -= 90
        else:
            l_value = number_as_int / 50
            for x in range(int(l_value)):
                result_string = result_string + "L"
                number_as_int -= 50

    if number_as_int >= 10:
        if str(number_as_int).startswith('4'):
            result_string = result_string + "XL"
            number_as_int -= 40
        else:
            x_value = number_as_int / 10
            for x in range(int(x_value)):
                result_string = result_string + "X"
                number_as_int -= 10

    if number_as_int >= 5:
        if str(number_as_int).startswith('9'):
            result_string = result_string + "IX"
            number_as_int -= 9
        else:
            v_value = number_as_int / 5
            for x in range(int(v_value)):
                result_string = result_string + "V"
                number_as_int -= 5

    if number_as_int >= 1:
        if str(number_as_int).startswith('4'):
            result_string = result_string + "IV"
        else:
            i_value = number_as_int / 1
            for x in range(int(i_value)):
                result_string = result_string + "I"

    return result_string


def checkInputAndPrintRomanNumeral(input):
    """Check input and prints out Roman Numeral.

    Validates input and in case of invalid string
    that can't be parsed to int returns error.
    After validation prints out parsed Roman Numeral to console.

    Parameters:
    input (str): An input string
    """
    try:
        num = int(input)
        text = parseToRomanNumeral(num)
        print(text)
    except ValueError:
        print("Vyraz neni validni, nelze parsovat na int...")


def main():
    """Run main method.

    Requires an input as param for checkInputAndPrintRomanNumeral function
    """
    checkInputAndPrintRomanNumeral(input("Zadej cislo: "))


if __name__ == '__main__':
    main()
