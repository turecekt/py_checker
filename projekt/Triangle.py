"""Calculate triangle."""
import math


def lengthofside(jednaX, dveX, jednaY, dveY):
    """Calculate length of a side.

    >>> lengthofside(2, 5, -8, 3)
    11.40175425099138
    """
    sa = jednaX - dveX
    sb = jednaY - dveY
    vysledek = math.sqrt(sa * sa + sb * sb)
    return vysledek


def constructability(Jedna, Dva, Tri):
    """Return if the triangle can be constructed.

    >>> constructability(5, 4, 3)
    'Trojúhelník je sestrojitelný'
    >>> constructability(8, 5, 7)
    'Trojúhelník je sestrojitelný'
    >>> constructability(500, 4, 3)
    'Trojůhelník není sestrojitelný'
    """
    if Jedna + Dva > Tri and Dva + Tri > Jedna and Jedna + Tri > Dva:
        return 'Trojúhelník je sestrojitelný'
    else:
        return 'Trojůhelník není sestrojitelný'


def biggest(stranaJedna, stranaDva, stranaTri):
    """Return the biggest number.

    >>> biggest(1, 2, 3)
    3
    >>> biggest(50.1, 94.20, 4/2)
    94.2
    >>> biggest(-50, 3, 8)
    8
    >>> biggest(100, 0, -5)
    100
    >>> biggest(100,0,110)
    110
    """
    big = stranaJedna
    if big > stranaDva:
        if big > stranaTri:
            return big
        else:
            return stranaTri
    elif stranaDva > stranaTri:
        return stranaDva
    else:
        return stranaTri


def rightangle(C, A, B):
    """Check if the triangle has a right angle.

    >>> rightangle(5, 4, 3)
    'Trojúhelník je pravoúhlý'
    >>> rightangle(4, 5, 3)
    'Trojúhelník je pravoúhlý'
    >>> rightangle(3, 4, 5)
    'Trojúhelník je pravoúhlý'
    >>> rightangle(500, 2, 1)
    'Trojúhelník není pravoúhlý'
    """
    if C * C == A * A + B * B:
        return 'Trojúhelník je pravoúhlý'
    elif A * A == C * C + B * B:
        return 'Trojúhelník je pravoúhlý'
    elif B * B == C * C + A * A:
        return 'Trojúhelník je pravoúhlý'
    else:
        return 'Trojúhelník není pravoúhlý'


def perimeter(A, B, C):
    """Count the perimeter of triangle.

    >>> perimeter(2, 5, 3)
    10
    >>> perimeter(5,5,5)
    15
    """
    o = A + B + C
    return o


def area(A, B, C):
    """Calculate area of triangle.

    >>> area(2, 5, 4)
    3.799671038392666
    >>> area(8, 5, 3)
    0.0
    >>> area(8, 10, 3)
    9.921567416492215
    """
    s = (A + B + C) / 2
    S = math.sqrt(s*(s-(A))*(s-(B))*(s-(C)))
    return S


if __name__ == '__main__':
    print("Zadávané hodnoty oddělujte mezerníkem\n",
          "v pořadí A[x,y], B[x,y], C[x,y]\n",
          "ZADEJTE 6 HODNOT!")
    Ax, Ay, Bx, By, Cx, Cy = input("Zadejte pozice: ").split()
    a = lengthofside(float(Cx), float(Bx), float(Cy), float(By))
    b = lengthofside(float(Ax), float(Cx), float(Ay), float(Cy))
    c = lengthofside(float(Bx), float(Ax), float(By), float(Ay))
    print("Délka stran a:", a, "b:", b, "c:", c, "\n",
          constructability(a, b, c), "\n",
          rightangle(c, a, b),
          "\nObvod trojúhelníku je: ", perimeter(a, b, c),
          "\nObsah trojúhelníku je: ", area(a, b, c),
          "\nNejvětší strana má délku: ", biggest(a, b, c)
          )
