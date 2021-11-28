"""MiniMax AP1VS.

Zaverecny projekt v Pythonu - Adam Karas
"""
import random
# import time


def createRandomArray():
    """Create an array of random integers.

    Values of an array are between -100 and 100
    Number of array elements = 20

    Returns:
        - array - an unsorted array of random integers
    """
    random_array = random.sample(range(-100, 100), 20)
    return random_array


def findMinValue(array):
    """Find a min value of array.

    Returns:
        - min_value - minimal value of array
    """
    min_value = min(array)
    return min_value


def findMaxValue(array):
    """Find a max value of array.

    Returns:
        - max_value - maximal value of array
    """
    max_value = max(array)
    return max_value


def findMinIndex(array, min_value):
    """Find an index of min value in array.

    Returns:
        - min_index - position of minimal value in array.
    """
    min_index = array.index(min_value)
    return min_index


def findMaxIndex(array, max_value):
    """Find an index of max value in array.

    Returns:
        - max_index - position of maximal value in array.
    """
    max_index = array.index(max_value)
    return max_index


def selectionSort(array):
    """Sorting algorithm: Selection Sort."""
    n = len(array)
    for i in range(n):
        # Initially, assume the first element
        # of the unsorted part as the minimum.
        minimum = i

        for j in range(i+1, n):
            if (array[j] < array[minimum]):
                # Update position of minimum element
                # if a smaller element is found.
                minimum = j
        # Swap the minimum element with the first element of the unsorted part.
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array


def bubbleSort(array):
    """Sorting algorithm: Bubble Sort."""
    n = len(array)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1,
            # swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def insertionSort(array):
    """Sorting algorithm: Insertion Sort."""
    # traverse through 1 to len(array)
    for i in range(1, len(array)):
        key = array[i]
        # move elements of array [0..i-1], that are greater than key,
        # to one position ahed of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def sortMenu(array):
    """User menu for sorting function."""
    sortingWay = int(input("Enter 1 for Selection Sort\n"
                           "Enter 2 for Bubble Sort\n"
                           "Enter 3 for Insertion Sort\n"))
    if sortingWay == 1:
        print("Selection Sort:")
        selectionSort(array)
        print(array)

    elif sortingWay == 2:
        print("Bubble Sort:")
        bubbleSort(array)
        print(array)

    elif sortingWay == 3:
        print("Insertion Sort:")
        insertionSort(array)
        print(array)

    else:
        print("Wrong input!!")


def test_GenerateRandomArray():
    """Generate Random Array test."""
    test_array = createRandomArray()
    temp = [0]*20
    for i in range(0, 20):
        if -1000 < test_array[i] < 1000:
            temp[i] = 1
        assert temp[i] == 1


def main():
    """Hlavni cast programu."""
    print("")
    array = createRandomArray()
    print(array)
    print("")
    min_value = findMinValue(array)
    print("Minimal value of array: ", min_value)
    min_index = findMinIndex(array, min_value)
    print("Index of min value is: ", min_index)
    max_value = findMaxValue(array)
    print("Maximal value of array: ", max_value)
    max_index = findMaxIndex(array, max_value)
    print("Index of max value is: ", max_index)
    print("")
    sortMenu(array)
    print("")


def test_SelectionSort():
    """Selection Sort algorithm - unit test."""
    test_array = [97, -83, -2, 21, 20]
    sorted_array = [-83, -2, 20, 21, 97]
    assert selectionSort(test_array) == sorted_array


def test_BubbleSort():
    """Bubble Sort algorithm - unit test."""
    test_array = [97, -83, -2, 21, 20]
    sorted_array = [-83, -2, 20, 21, 97]
    assert bubbleSort(test_array) == sorted_array


def test_InsertionSort():
    """Insertion Sort algorithm - unit test."""
    test_array = [97, -83, -2, 21, 20]
    sorted_array = [-83, -2, 20, 21, 97]
    assert insertionSort(test_array) == sorted_array


def test_MinValue():
    """Function findMinValue - unit test."""
    test_array = [97, -83, -2, 21, 20]
    assert findMinValue(test_array) == -83


def test_MinValueIndex():
    """Function findMinIndex - unit test."""
    test_array = [97, -83, -2, 21, 20]
    min_value = -83
    assert findMinIndex(test_array, min_value) == 1


def test_MaxValue():
    """Function findMaxValue - unit test."""
    test_array = [97, -83, -2, 21, 20]
    assert findMaxValue(test_array) == 97


def test_MaxIndex():
    """Function findMaxIndex - unit test."""
    test_array = [97, -83, -2, 21, 20]
    max_value = 97
    assert findMaxIndex(test_array, max_value) == 0


if __name__ == "__main__":
    main()
