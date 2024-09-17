"""Module prime number checker.

This module is use for checking the input, supplies  functions:
isPrimeNumber(), printDivisors()

"""


# Author:   Barbana Klimekova <b_klimekova@utb.cz>
#           Lucia Kubaskova <l_kubaskova@utb.cz>
#           Tomas_Prikasky <t_prikasky@utb.cz>
#
# Description:  Create a program to evaluate whether the entered number
#               is a prime number.
#               Prime numbers have exactly two divisors, are divisible
#               by only 1 and by themselves.


def isPrimeNumber(number):
    """Count number of dividers.

    Parameters:
        - dividers (int[]): List of integers - dividers
        - counter (int): number of dividers
    Returns:
        - output (int): number of dividors (counter) and
        printed list of dividors
    """
    # logic of prime number evaluation
    isPrimeNumber = True
    for divisor in range(2, number):
        if number % divisor == 0:
            isPrimeNumber = False
            break
    return isPrimeNumber


def getDivisors(number):
    """Count number of dividers and print them.

    Parameters:
        - dividers (int[]): List of integers - dividers
        - counter (int): number of dividers
    Returns:
        - output (int): number of dividors (counter) and
        printed list of dividors
    """
    # inicialize and define number of divisers as 0 at the beginning

    divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors


def main():
    """Execute all functions.

    Parameters:
        - number - input from console
    Returns:
        - output (int): print statements into console
    """
    try:
        number = int(input("Vlož číslo: "))
        if number < 0:
            print("Nebylo zadáno kladne číslo")
            return 1
        if isPrimeNumber(number):
            print(f"Číslo {number} je prvočíslo")
        else:
            print(f"Číslo {number}  nie je prvočíslo")
        divisors = getDivisors(number)
        print("Delitele: ", end="")
        print(*divisors, sep=", ")
        print('Počet deliteľov:', len(divisors))
    except Exception:
        print("Nebylo zadáno číslo")


if __name__ == "__main__":
    main()

# print documentation using pydoc.

# print documentation for class
# print(PrimeNumber.__doc__)
# print documentation for function isPrimeNumber
# print(isPrimeNumber.__doc__)
# print documentation for function printDivisors
# print(printDivisors.__doc__)
