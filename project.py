""".

SEMESTRALNI PROJEKT DO AP1VS

project.py

version:    1.0

Author: Jiri Kantor https://github.com/kantorj

---------------------------------------------------

This algorithm is used to define if a
value entered by the user is a prime number

---------------------------------------------------

This project was made for educational purpose only.

"""
import unittest


def prvocislo(val):  # program pro urceni prvocisla
    """Check the val."""
    if isinstance(val, int):  # checks if 'val' is of type 'int'

        if val > 1:  # pro cislo > 1
            for i in range(2, val):
                if (val % i) == 0:  # cislo nedává zbytek po dělení
                    print(val, ' neni prvocislo.')
                    print(i, ' * ', val // i, ' = ', val)  # důkaz dělitelnosti
                    print('(Pro vypocet byla pouzita deterministicka metoda.)')
                    return 2
            else:  # cislo dává zbytek po dělení
                print(val, ' je prvocislo.')
                print('(Pro vypocet byla pouzita deterministicka metoda.)')
                return 99
        elif val < 0:  # pro cislo <= 1
            print('Zadane cislo musi byt > 0.')
            return 0
        elif val == 1:
            print('Cislo 1 neni prvocislo dle definice.')
            return 1
        else:
            print(val, ' neni prvocislo.')  # cislo mezi 0 a 1
            print('(Pro vypocet byla pouzita deterministicka metoda.)')
            return 10
    else:
        print('Zadana hodnota musi byt cele cislo.')
        return 22


# unit testy:
class TestPrvocislo(unittest.TestCase):
    """Class docstring."""

    def test_is_one(self):
        """Use this function to check the entered value 1."""
        assert prvocislo(1) == 1  # from return

    def test_is_not_val(self):
        """Check if the entered value is not of the type 'int'."""
        assert prvocislo('a') == 22

    def test_small_not_primes(self):
        """Check if the entered low values aren't a prime number."""
        for i in range(4, 100, 2):
            assert prvocislo(i) == 2

    def test_small_primes(self):
        """Use this function to check the small prime values."""
        numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(0, (len(numbers) - 1)):
            assert prvocislo(numbers[i]) == 99

    def test_big_primes(self):
        """Use this function to check the big prime values."""
        numbers = [104677, 104681, 104683, 104693, 104701,
                   104707, 104711, 104717, 104723, 104729]
        for i in range(0, (len(numbers) - 1)):
            assert prvocislo(numbers[i]) == 99

    def test_is_between(self):
        """Check the entered value is between 0 and 1."""
        assert prvocislo(0) == 10


if __name__ == '__main__':
    print('===Program pro posouzeni cisla / prvocisla===')
    cislo = input('Zadejte libovolne cele cislo k posouzeni: ')
    prvocislo(cislo)
