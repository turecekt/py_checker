"""
Program pro zjištění minima, maxima prvku v poli.

A jeho setřídění 3 různými třídícími algoritmy.
"""


import sys
import random


# Funkce pro zjištění nejmenšího prvku v poli
def min(nums):
    """Return minimum value in given array."""
    min_value = None
    for value in nums:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


# Funkce pro zjištění největšího prvku v poli
def max(nums):
    """Return maximum value in given array."""
    max_value = nums[0]
    for value in nums:
        if value > max_value:
            max_value = value
    return max_value


# Výpis nejmenšího a největšího prvku v poli s jeho indexem
def min_max(mylist):
    """Print outputs."""
    minVal = min(mylist)
    maxVal = max(mylist)
    minIdx = mylist.index(minVal)
    maxIdx = mylist.index(maxVal)
    (print("Nejmenší prvek v seznamu má hodnotu: "
     + str(minVal) + " a nachazi se na indexu: "
     + str(minIdx)))
    (print("Největší prvek v seznamu má hodnotu: "
     + str(maxVal) + " a nachazi se na indexu: "
     + str(maxIdx)))
    return str(minVal), str(maxVal), str(minIdx), str(maxIdx)


# Quicksort třídící algoritmu
def quick_sort(arr):
    """Sort the array by using quicksort."""
    left = []
    middle = []
    right = []
    if len(arr) > 1:
        # Rozdělení vstupu podle pivota na levou, pravou a střední část
        pivot = arr[0]
        for x in arr:
            # Umístění všech prvků menších než je pivot nalevo od něj
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            elif x > pivot:
                right.append(x)
        return quick_sort(left)+middle+quick_sort(right)  # Spojení částí pole
    else:
        return arr


# Insertionsort třídící algoritmus
def insertion_sort(arr):
    """Sorting the array using insertionsort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Mergesort třídící algoritmus
def merge_sort(arr):
    """Sort the array using mergesort."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Rekurzivní volání druhé poloviny
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        # Iterátor kořenového listu
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Zbývající hodnoty
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# Switch na zvolení typu řadícího algortimu
def sort_choice(mylist, x):
    """
    Return min, max value and sorted array.

    Using specific sort chosen by a user.
    """
    if x == '1':
        sorted_array = quick_sort(mylist)
        print("Sorted array: ", sorted_array)
        return sorted_array
    elif x == '2':
        sorted_array = insertion_sort(mylist)
        print("Sorted array: ", sorted_array)
        return sorted_array
    elif x == '3':
        sorted_array = merge_sort(mylist)
        print("Sorted array: ", sorted_array)
        return sorted_array
    else:
        raise Exception("Nevalidní hodnota.")


# Generovaní pole při zavolání funkce uživatele bez argumentů
def generate_array():
    """Return generated array if program is called without argumets."""
    mylist = []
    while len(mylist) < 20:
        r = random.randint(-100, 100)
        if r not in mylist:
            mylist.append(r)
    return mylist


def read_file():
    """Read text file line by line and return array."""
    output = []
    row_data = []
    # file = open(sys.argv[1], "r")
    file = open("soubor-s-cisly.txt", "r")
    lines = file.read().splitlines()
    file.close()
    for line in lines:
        row_data = line.split()
        for num in row_data:
            output.append(int(num))
    return output


# Hlavní funkce:
def main():
    """Run main driver function of the program."""
    # mylist = []
    print("Jaký řadící algortimus chcete použít?")
    x = str(input("Quicksort[1], Insertionsort[2], Mergesort[3]"))
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        if argument[-3:] == 'txt':
            mylist = read_file()
            print("Input Array: ", mylist)
            min_max(mylist)
            sort_choice(mylist, x)
            # print("Sorted Array: ", mylist)
        else:
            mylist = []
            for i in sys.argv[1:]:
                mylist.append(int(i))
            print("Input Array: ", mylist)
            min_max(mylist)
            sort_choice(mylist, x)
            # print("Sorted Array: ", mylist)
    else:
        mylist = generate_array()
        print("Input Array: ", mylist)
        min_max(mylist)
        sort_choice(mylist, x)


# Unittesty
def test_min():
    """Min test."""
    test_list = [1, 2, 3, -4, -2]
    assert(min(test_list)) == -4


def test_max():
    """Max test."""
    test_list = [1, 2, 3, -4, -2]
    assert(max(test_list)) == 3


# Unittest Quicksortu
def test_quicksort():
    """Quicksort Unittest."""
    test_arr = [7, 13, 5]
    assert(quick_sort(test_arr)) == [5, 7, 13]
    # test nahodných vstupů
    # test_rArr = [random.sample(range(100), 10)]
    # test_rArrCopy = test_rArr.copy()
    # quick_sort(test_rArr, 0, len(test_rArr)-1)
    # test_rArrCopy.sort()
    # assert (test_rArr) == test_rArrCopy


# Unittest Mergesortu
def test_mergesort():
    """Mergesort Unittest."""
    test_arr = [37, 41, 73, 13, 7, 101]
    assert(merge_sort(test_arr)) == [7, 13, 37, 41, 73, 101]


# Unittest Insertionsortu
def test_insertionsort():
    """Insertionsort Unittest."""
    test_arr = [37, 41, 73, 13, 7, 101]
    assert(insertion_sort(test_arr)) == [7, 13, 37, 41, 73, 101]


def test_readfile():
    """Test reading values in a text file."""
    test_arr = read_file()
    assert test_arr == [57, 21, 63, 3, 15, 7, 68, 46, 20, 58, 48, 41]


def test_generateRandom():
    """
    Test array generate_array function.

    By checking their resulting lengths.
    """
    test_arr = generate_array()
    test_arr2 = generate_array()
    assert len(test_arr) == len(test_arr2)


def test_sort_choice1():
    """Test switch if user inserts choice no. 1."""
    test_arr = [57, 21, 63, 15]
    assert sort_choice(test_arr, '1') == [15, 21, 57, 63]


def test_sort_choice2():
    """Test switch if user inserts choice no. 2."""
    test_arr = [57, 21, 63, 15]
    assert sort_choice(test_arr, '2') == [15, 21, 57, 63]


def test_sort_choice3():
    """Test switch if user inserts choice no. 3."""
    test_arr = [57, 21, 63, 15]
    assert sort_choice(test_arr, '3') == [15, 21, 57, 63]


def test_min_max():
    """Test min_max function."""
    res = min_max([57, 21, 63, 15])
    assert res[0] == '15'
    assert res[1] == '63'
    assert res[2] == '3'
    assert res[3] == '2'
    # test_minmax = min_max([57, 21, 63, 15])
    # assert test_minmax == ['15', '63', '3', '2']


if __name__ == "__main__":
    main()
