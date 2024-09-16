"""Random math examples.

Author: Daberger Jiri <j_daberger@utb.cz>
Description: Counting response of user on easy math examples
"""

import sys
import MathFunctions
import random
from time import perf_counter


def randomExample():
    """For creating random math examples.

    Parameters:
        operator (int): random number for operator [1; 2; 3; 4]
        a (int): random number <-10, 10>
        b (int): random number <10, 10>

    Returns: result of math expression
    """
    operator = random.randint(1, 4)
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    if operator == 4:
        MathFunctions.divider(a, b)

        result = MathFunctions.division(a, b)
        if result is False:
            return randomExample()

    # part of code for multiply
    elif operator == 3:
        MathFunctions.multipler(a, b)

        result = MathFunctions.multiply(a, b)

    # part of code for substraction
    elif operator == 2:
        MathFunctions.minus(a, b)

        result = MathFunctions.subtraction(a, b)

    # part of code for sum
    elif operator == 1:
        MathFunctions.plus(a, b)

        result = MathFunctions.sum(a, b)

    return result


def startProgram(param):
    """Start this method will generate examples.

    Args:
        param: Gets info from user

    Returns: Result of user
    """
    points = 0
    i = 0
    times = list()
    repetition = 5

    while i < repetition:
        start = perf_counter()

        pc = randomExample()
        if param == 'user':
            user = input("Enter answer: ")
        else:
            user = param

        stop = perf_counter()
        times.append(stop - start)

        if MathFunctions.points(pc, user):
            points += 1
        else:
            print(f"Your answer is wrong! Right answer is {pc}")

        i += 1

    print(f"\nYou got {points} of {repetition} points")
    print(f"Average time is {MathFunctions.average(times)} seconds")


print("Welcome to my generator of math examples! \n")
usr = sys.argv
if 'start' not in usr:
    """This will start program with a default value set to 5."""
    startProgram(5)
else:
    startProgram('user')
