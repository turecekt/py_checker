"""Defined methods."""


def getInput(input):
    """Get input."""
    # Wait for user input
    # inputArgument = input("Enter number to check if its a prime... ")
    return start(input)


def start(inputArgument):
    """Start."""
    # If input is 'exit', exit program
    if (inputArgument == ''):
        print("Not valid input")
        return
    if (inputArgument == 0):
        print('0 is not a valid input')
        return

    # Check if number is an integer
    isNumber = isInteger(inputArgument)
    if (isNumber is True):
        number = int(inputArgument)
        if (number < 100):
            if (number > 1):
                # for each number till my number
                for i in range(2, number):
                    # if mod is 0 -> no rest, number is divisible -> not prime
                    if (number % i) == 0:
                        return isNotPrimeAndRepeat(number, "Deterministic")
                # if mod is always different from 0 -> prime
                return isPrimeAndRepeat(number, "Deterministic")
            else:
                # if number is 1 -> not prime
                return isNotPrimeAndRepeat(number, "Deterministic")
        else:
            # root number is enough to check (int(number ** (0.5)))
            # +1 process every/last/root number
            for i in range(2, int(number ** (0.5)) + 1):
                # if mod is 0 -> no rest, number is divisible -> not prime
                if (number % i) == 0:
                    return isNotPrimeAndRepeat(number, "Heuristic")
            return isPrimeAndRepeat(number, "Heuristic")


def isPrimeAndRepeat(number, approach):
    """Is prime answer."""
    print(number, "is a prime number.", approach, "approach.")
    return 'PRIME'


def isNotPrimeAndRepeat(number, approach):
    """Is not prime answer."""
    print(number, "is not a prime number.", approach, "approach.")
    return 'NOT PRIME'


def isInteger(input):
    """Check if number is an integer."""
    try:
        int(input)
        return True
    except ValueError:
        print(input, "is not an integer")
        return False
