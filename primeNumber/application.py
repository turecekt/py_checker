from prime_number import is_prime_number

"""
//
//
//
"""

user_input = input("Zadej cislo: ")
print("\n")

try:
    """Ahoj."""
    num = int(user_input)
    is_prime_number(num)

except ValueError:
    try:
        """Ahoj."""
        num = float(user_input)
        is_prime_number(num)

    except ValueError:
        print("Toto neni cislo")
