"""Math functions with tests."""


def sum(a, b) -> int:
    """Sum function.

    Args:
        a: int
        b: int

    Returns: sum of two numbers (int)
    >>> sum(2, 2)
    4
    """
    return a + b


def subtraction(a, b) -> int:
    """Subtraction function.

    Args:
        a: int
        b: int

    Returns: difference of two numbers (int)
    >>> subtraction(5, 3)
    2
    """
    return a - b


def multiply(a, b) -> int:
    """Multiply function.

    Args:
        a: int
        b: int

    Returns: multiple of two numbers (int)
    >>> multiply(4, 8)
    32
    """
    return a * b


def division(a, b) -> float:
    """Division function.

    Args:
        a: int
        b: int

    Returns: division of two numbers (double)
    >>> division(8, 0)
    False
    >>> division(0, 1)
    0.0
    """
    if b == 0:
        return False
    return round((a / b), 2)


def average(times) -> float:
    """For counting average time of user reply.

    Args:
        times: List of times
    Returns: Average time (double)
    >>> average([1, 2, 6])
    3.0
    """
    av = 0
    for x in times:
        av += x
    av /= len(times)
    return round(av, 2)


def compareResults(pc, user) -> bool:
    """Compare results function.

    Function which compare two values,
    right result of math example and user answer

    Args:
        pc: Right result of math example
        user: Answer of user

    Returns: True or False
    >>> compareResults(7, 7)
    True
    >>> compareResults(7, 5)
    False
    >>> compareResults(7, 's')
    False
    """
    try:
        if float(pc) == float(user):
            return True
    except ValueError:
        return False
    return False


def divider(a, b):
    """Divide operator function.

    Args:
        a: int
        b: int

    Returns: Print for user
    >>> divider(4, 2)
    4/2
    >>> divider(4, -2)
    4/(-2)
    """
    if b < 0:
        print(f"{a}/({b})")
    else:
        print(f"{a}/{b}")


def multipler(a, b):
    """Multiple operator function.

    Args:
        a: int
        b: int

    Returns: Print for user
    >>> multipler(4, 2)
    4*2
    >>> multipler(4, -2)
    4*(-2)
    """
    if b < 0:
        print(f"{a}*({b})")
    else:
        print(f"{a}*{b}")


def minus(a, b):
    """Subtraction operator function.

    Args:
        a: int
        b: int

    Returns: Print for user
    >>> minus(4, 2)
    4-2
    >>> minus(4, -2)
    4+2
    """
    if b < 0:
        print(f"{a}+{b * (-1)}")
    elif b >= 0:
        print(f"{a}-{b}")


def plus(a, b):
    """Sum operator function.

    Args:
        a: int
        b: int

    Returns: Print for user
    >>> plus(4, 2)
    4+2
    >>> plus(4, -2)
    4-2
    """
    if b < 0:
        print(f"{a}{b}")
    elif b >= 0:
        print(f"{a}+{b}")


def points(pc, user):
    """Points function.

    Args:
        pc: int
        user: int

    Returns: True or False
    >>> points(5, 5)
    True
    >>> points(4, 8)
    False
    """
    if compareResults(pc, user):
        return True
    else:
        return False
