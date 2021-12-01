"""Main.py - Checking if input number is prime number."""
import random


def main():
    """Get user input and check if the input is prime number. Return None."""
    print_input()
    text = input()

    while not check_number(text):
        text = input()
        pass

    number = int(text)

    if(check_higher_number(number)):
        print("Prvočíslo bude zjíštěno přes fermatovu metodu")
        if(fermat_test(number, 3)):
            print("Je prvočíslo")
        else:
            print("Není prvočíslo")
    else:
        print("Je použita obecná metoda")

        if(check_prime_number(int(text))):
            print("Je prvočíslo")
        else:
            print("Není prvočíslo")


def check_higher_number(number):
    """Check if number is higher then 100 to select best method."""
    if(number > 100):
        return True
    else:
        return False


def print_input():
    """Print sentece to user. Return None."""
    print('Zadejte číslo k zjíštění, zda je číslo prvočíslo')


def check_number(text: str):
    """If number is integer return true."""
    try:
        int(text)
        return True
    except ValueError:
        print('Zadaný vstup není celé číslo.')
        print_input()
        return False


def check_prime_number(number: int):
    """Test number if is prime then return true."""
    if(number <= 1):
        return False

    if(number == 2):
        return True

    i = 3
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def fermat_test(number, k):
    """Fermat test to test higher number. Return Boolean."""
    if number == 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(k):
        randomNumber = random.randint(1, number - 1)

        if (pow(randomNumber, number - 1) % number != 1):
            return False

    return True


if __name__ == '__main__':
    main()
