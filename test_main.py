"""Testy k hlavnimu scriptu main."""

from main import min_max, bubblesort, selectionsort, shellsort, main, run


def test_min_max():
    """Test funkce min_max."""
    assert(min_max(
        [12, 5, 9, 54, 1, 3, 98, 13]) ==
        "Min number:1, Index:4\nMax number:98, Index:6")
    assert(min_max(
        [52, 15, 91, 5, 187, 23, 99, 53]) ==
        "Min number:5, Index:3\nMax number:187, Index:4")


def test_bubblesort():
    """Test algoritmu bubblesort."""
    assert(bubblesort(
        [12, 5, 9, 54, 1, 3, 98, 13]) == [1, 3, 5, 9, 12, 13, 54, 98])
    assert(bubblesort(
        [52, 15, 91, 5, 187, 23, 99, 53]) == [5, 15, 23, 52, 53, 91, 99, 187])


def test_selectionsort():
    """Test algoritmu selectionsort."""
    assert(selectionsort(
        [12, 5, 9, 54, 1, 3, 98, 13]) == [1, 3, 5, 9, 12, 13, 54, 98])
    assert(selectionsort(
        [52, 15, 91, 5, 187, 23, 99, 53]) == [5, 15, 23, 52, 53, 91, 99, 187])


def test_shellsort():
    """Test algoritmu shellsort."""
    assert(shellsort(
        [12, 5, 9, 54, 1, 3, 98, 13]) == [1, 3, 5, 9, 12, 13, 54, 98])
    assert(shellsort(
        [52, 15, 91, 5, 187, 23, 99, 53]) == [5, 15, 23, 52, 53, 91, 99, 187])


def test_main():
    """Test funkce main."""
    assert(main() is not None)


def test_run(monkeypatch):
    """Test run funkce."""
    monkeypatch.setattr('builtins.input', lambda _: "a")
    i = input("Bubble = 1, Selection = 2, Shell = 3: ")
    assert i == "a"
    assert(run() == print("Incorrect input!"))
