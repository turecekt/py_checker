""".

<PRVOČÍSLO>
In this code I take input from the user, check if it meets certain
requirements and then based on the amount of digits, I use
an algorithm to determine whether a given n is a prime or not.
I also included a timer to easily compare effectiveness.
"""


def checkIn(n):
    """Sieve letters.

    Check if input 'n' contains any letters.

    >>> checkIn('111')
    False
    >>> checkIn('1a1')
    True
    >>> checkIn('aaa')
    True
    """
    return any(char.isalpha() for char in n)


def getNum():
    """Get input.

    Gets input from the user. Checks if the input is an integer.
    Input must be a whole number and can't contain '.', ',' or any letters.
    Returns the number as int since input() creates a string.
    """
    n = input("Please enter any integer: ")
    while checkIn(n) or (n.find(",") != -1) or not float(n).is_integer():
        n = input("Please enter any integer: ")
    return int(n)


def isPrime(n):
    """Deterministic aproach to finding primes.

    I consider this approach to be deterministic because the only "shortcut"
    we take, is ruling out numbers equal to or smaller than 1, whitch is
    a pretty obvious assumption when finding primes.
    Determines if given number n in prime or not.
    First rule out any numbers equal to or smaller than 1 because by
    definition primes are greater than 1.
    Initialize a for loop from 2(including) to n(not including).
    On each cycle checks if the remainder after dividing n by i is zero.
    If false, move on to next i.
    If true, return False -> n is not a prime.
    If false, but the for loop has finished, return True -> n is a prime.

    >>> isPrime(5)
    True
    >>> isPrime(6)
    False
    >>> isPrime(-5)
    False
    """
    if(n <= 1):
        return False

    for i in range(2, n):
        if (n % i) == 0:
            return False
    else:
        return True


def optimizedIsPrime(n):
    """Heuristic aproach to finding primes.

    I consider this approach to be heuristic because I take advatage of several
    facts about primes to avoid checking every number up to n, the difference
    in computational speed, compared to isPrime(), becomes significant with
    numbers that have 7(variable) or more digits.
    Source to method used: https://en.wikipedia.org/wiki/Primality_test
    On wikipedia I found that all primes are of the form 6k ± 1, with the
    exception of 2 and 3.
    This is because:
    integers can be expressed as (6k + i) so any int k AND i = 0, 1, 2, 3, 4;
    2 divides any (6k + 0), (6k + 2), (6k + 4);
    3 divides (6k + 3).
    So a heuristic method is to test if n is divisible by 2 or 3, then to check
    through all the numbers of form 6k ± 1.
    First we rule out any number equal to or smaller than 1
    Then we check if the number is 2 or 3, if so => number is a prime
    If the we got this far we know that n is larger than 3, therefore if it's
    divisible by 2 or 3 without a remainder => number is not a prime.
    From this point we only check n against numbers 6k±1,
    where k starts at 5 and increments by 6.

    >>> optimizedIsPrime(5)
    True
    >>> optimizedIsPrime(6)
    False
    >>> optimizedIsPrime(-5)
    False
    """
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def pickAlg(n):
    """Pick and run algorithm.

    Based on users choice, algorithm is picked, ran and timed.
    Results are then printed.
    """
    if len(str(n)) > 7:
        if (optimizedIsPrime(n)):
            print('''A heuristic method was used to determine that
{0} is a prime number'''.format(n))
            return 1
        else:
            print('''A heuristic method was used to determine that
{0} is not a prime number'''.format(n))
            return 0

    if len(str(n)) <= 7:
        if (isPrime(n)):
            print('''A deterministic method was used to determine that
{0} is a prime number'''.format(n))
            return 1
        else:
            print('''A deterministic method was used to determine that
{0} is not a prime number'''.format(n))
            return 0


if __name__ == "__main__":
    """.

    Here I save user input in variable n. Then I call the pickAlg()
    function and give it n as argument
    """
    n = getNum()
    pickAlg(n)


def test_checkIn():
    """.

    First n contains a letter so checkIn returns true
    Second n doesn't contains a letter so checkIn returns false

    >>> checkIn('1a')
    True
    >>> checkIn('1')
    False
    """
    n = '1a'
    assert checkIn(n)

    n = '1'
    assert not checkIn(n)


def test_isPrime():
    """.

    -5 is not a prime number because it's negativem,
    isPrime() returns False
    5 is a prime number because it has exactly two distinct factors,
    isPrime() returns True
    6 is not a prime number because it has more that 2 distinct factors,,
    isPrime() returns False

    >>> isPrime(-5)
    False
    >>> isPrime(5)
    True
    >>> isPrime(6)
    False
    """
    assert not isPrime(-5)
    assert isPrime(5)
    assert not isPrime(6)


def test_optimizedIsPrime():
    """.

    -5 is not a prime number because it's negative,
    isPrime() returns False
    5 is a prime number because it has exactly two distinct factors,
    isPrime() returns True
    6 is not a prime number because it has more that 2 distinct factors,,
    isPrime() returns False

    >>> optimizedIsPrime(-5)
    False
    >>> optimizedIsPrime(5)
    True
    >>> optimizedIsPrime(6)
    False
    """
    assert not optimizedIsPrime(-5)
    assert optimizedIsPrime(5)
    assert not optimizedIsPrime(6)


def test_pickAlg():
    """Test for pickAlg() function.

    Saves n as 5, and output is the expected output.
    Then asserts that output from pickAlg() matches the expected one
    """
    n = 5
    o = 1
    ao = pickAlg(n)
    assert ao == o
