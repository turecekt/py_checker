"""Tests for main."""
import main


def test_str_list_to_int():
    """Test for str_list_to_int method."""
    assert main.str_list_to_int(["1", "1"])[1] == (1, 1)
    assert main.str_list_to_int(["1", "1"])[0]
    assert not main.str_list_to_int([2, "a"])
