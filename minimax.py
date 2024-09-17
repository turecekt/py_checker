"""Minimax."""


import sys
import io
from random import randint


def inicializer(option=0):
    """Inicializing array via random generator / text file / user input."""
    array = []
    # Array is randomly generated.
    if len(sys.argv) == 1 or option == 1:
        for i in range(20):
            array.append(randint(-100, 100))
    # Inicialization from text file.
    elif (len(sys.argv) == 2 and
          sys.argv[1].isdigit() is False) or option == 2:
        with open(sys.argv[1], 'rt') as f:
            my_list = list(f)
        try:
            for line in my_list:
                for word in line.split():
                    array.append(int(word))
        except ValueError as exception:
            print('String contained in the file must be digits!' + exception)
    # Inicialization from user input.
    elif (len(sys.argv) >= 2 and sys.argv[1].isdigit() is True) or option == 3:
        try:
            for i in range(1, len(sys.argv)):
                array.append(int(sys.argv[i]))
        except ValueError as exception:
            print('User input must be digits!' + exception)
    return array


def bubble_sort(array):
    """Sorts elements of array."""
    for cycles in range(len(array)):
        sorted = True
        for index in range(0, len(array) - cycles - 1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                sorted = False
        if sorted is True:
            break
    return array


def insertion_sort(array):
    """Sorts elements of array."""
    for index in range(1, len(array)):
        element = array[index]
        position = index - 1
        while position >= 0 and array[position] > element:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = element
    return array


def quick_sort(array):
    """Sorts elements of array."""
    if len(array) < 2:
        return array
    lower, same, higher = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for element in array:
        if element < pivot:
            lower.append(element)
        elif element == pivot:
            same.append(element)
        elif element > pivot:
            higher.append(element)
    return quick_sort(lower) + same + quick_sort(higher)


def printer(array):
    """Print min() & max() of sorted array."""
    print(f'\nMin: {min(array)} Max: {max(array)} \nArray: {array}')


def choose_sorting_method(array, choice=0):
    """UI to choose sorting system."""
    if choice == 0:
        # Let user make choices until he is succesful.
        while choice not in [1, 2, 3]:
            try:
                choice = int(input('1: Bubble sort. \
                                \n2: Insertion sort \
                                \n3: Quick sort.\n'))
            except ValueError as exception:
                print('User input must be digits!' + exception)
    if choice == 1:
        printer(bubble_sort(array))
    elif choice == 2:
        printer(insertion_sort(array))
    elif choice == 3:
        printer(quick_sort(array))


def test_inicializer():
    """Test iniciliazer of array."""
    # Check random generated array.
    assert len(inicializer(1)) == 20
    # Check if inicialization from file works correctly.
    sys.argv[0] = 'minimax'
    if len(sys.argv) == 2:
        sys.argv[1] = 'test_text.txt'
        assert len(inicializer(2)) == 9
    elif len(sys.argv) == 1:
        sys.argv.append('test_text.txt')
        assert len(inicializer(2)) == 9
    # Check if array is inicialized via user input correctly.
    if len(sys.argv) == 2:
        sys.argv.pop()
        for i in range(1, 10):
            sys.argv.append(f'{i}')
        assert len(inicializer(3)) == 9
        assert inicializer(3) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bubble_sort():
    """Test bubble sort functionality."""
    assert bubble_sort([15, 9, -8, 0, 12, 5, -8, 1]) \
           == [-8, -8, 0, 1, 5, 9, 12, 15]
    assert bubble_sort([0]) == [0]
    assert bubble_sort([0, -1]) == [-1, 0]


def test_insertion_sort():
    """Test insertion sort functionality."""
    assert insertion_sort([15, 9, -8, 0, 12, 5, -8, 1]) \
           == [-8, -8, 0, 1, 5, 9, 12, 15]
    assert insertion_sort([0]) == [0]
    assert insertion_sort([0, -1]) == [-1, 0]


def test_quick_sort():
    """Test quick sort \
    functionality."""
    assert quick_sort([15, 9, -8, 0, 12, 5, -8, 1]) \
           == [-8, -8, 0, 1, 5, 9, 12, 15]
    assert quick_sort([0]) == [0]
    assert quick_sort([0, -1]) == [-1, 0]


def test_printer():
    """Test printer output."""
    printer_output = io.StringIO()
    sys.stdout = printer_output
    printer([-8, -8, 0, 1, 5, 9, 12, 15])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    # Check if printer works properly.
    # Searches for parts of printer output.
    assert string.find('Min: -8') != -1
    assert string.find('Max: 15') != -1
    assert string.find('[-8, -8, 0, 1, 5, 9, 12, 15]') != -1


def test_choose_sorting_method():
    """Test choice-maker for sorting systems."""
    # Test funcionality if choice equals 1 (Bubble sort).
    printer_output = io.StringIO()
    sys.stdout = printer_output
    choose_sorting_method([9, 8, 7, 6, 5, 4, 3, 2, 1], 1)
    printer([9, 8, 7, 6, 5, 4, 3, 2, 1])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    assert string.find('[9, 8, 7, 6, 5, 4, 3, 2, 1]') != -1
    # Test funcionality if choice equals 2 (Insertion sort).
    sys.stdout = printer_output
    choose_sorting_method([9, 8, 7, 6, 5, 4, 3, 2, 1], 2)
    printer([9, 8, 7, 6, 5, 4, 3, 2, 1])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    assert string.find('[9, 8, 7, 6, 5, 4, 3, 2, 1]') != -1
    # Test funcionality if choice equals 1 (Quick sort).
    sys.stdout = printer_output
    choose_sorting_method([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)
    printer([9, 8, 7, 6, 5, 4, 3, 2, 1])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    assert string.find('[9, 8, 7, 6, 5, 4, 3, 2, 1]') != -1


test_inicializer()
test_bubble_sort()
test_insertion_sort()
test_quick_sort()
test_printer()
test_choose_sorting_method()
# Code calling methods with additional arguments.
# Un-comment following code if you want to run this programm.
# choose_sorting_method(inicializer())
