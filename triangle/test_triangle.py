"""Tests for triangle module."""
from triangle import Triangle


def test_side_lenght():
    """Test for side_lenght method."""
    assert Triangle([1, 0], [0, 1], [1, 1]).side_lenght()[1] == 1.0
    assert Triangle([1, 0], [0, 1], [1, 1]).side_lenght()[2] == 1.0
    assert round(Triangle([1, 0], [0, 1], [1, 1]).side_lenght()[0], 2) == 1.41


def test_is_able():
    """Test for is_able method."""
    assert Triangle([1, 0], [0, 1], [1, 1]).is_able()
    assert not Triangle([1, 1], [2, 2], [3, 3]).is_able()


def test_is_rectangular():
    """Test for is_rectangular method."""
    assert Triangle([1, 0], [0, 1], [1, 1]).is_rectangular()
    assert not Triangle([1, 0], [0, 5], [1, 1]).is_rectangular()


def test_perimeter():
    """Test for perimeter method."""
    assert round(Triangle([1, 0], [0, 1], [1, 1]).perimeter(), 2) == 3.41


def test_area():
    """Test for area method."""
    assert round(Triangle([1, 0], [0, 1], [1, 1]).area(), 2) == 0.5
